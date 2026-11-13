"""Demo de las funcionalidades principales de pandas."""
from pathlib import Path

import numpy as np
import pandas as pd

CARPETA = Path(__file__).parent
RUTA_CSV = CARPETA / "ventas.csv"

pd.set_option("display.width", 120)
pd.set_option("display.max_columns", None)


def titulo(texto):
    """Imprime un encabezado de sección."""
    print(f"\n{'=' * 60}\n{texto}\n{'=' * 60}")


def crear_datos():
    """Crea un DataFrame de ventas de ejemplo con algunos valores faltantes."""
    generador = np.random.default_rng(seed=42)
    cantidad_filas = 20
    return pd.DataFrame({
        "fecha": pd.date_range("2026-01-01", periods=cantidad_filas, freq="W"),
        "ciudad": generador.choice(["Bogotá", "Medellín", "Cali"], cantidad_filas),
        "producto": generador.choice(["Café", "Té", "Chocolate"], cantidad_filas),
        "unidades": generador.integers(1, 50, cantidad_filas).astype(float),
        "precio": generador.choice([3500, 4200, 5000], cantidad_filas),
    }).assign(unidades=lambda df: df["unidades"].mask(df.index.isin([3, 11])))


def explorar(ventas):
    """Muestra la estructura y estadísticas básicas del DataFrame."""
    titulo("1. Exploración: head, shape, dtypes, describe")
    print(ventas.head())
    print(f"\nForma: {ventas.shape}")
    print(f"\nTipos:\n{ventas.dtypes}")
    print(f"\nEstadísticas:\n{ventas.describe()}")


def limpiar(ventas):
    """Detecta y rellena valores faltantes."""
    titulo("2. Limpieza: isna y fillna")
    print(f"Nulos por columna:\n{ventas.isna().sum()}")
    mediana = ventas["unidades"].median()
    limpio = ventas.fillna({"unidades": mediana})
    print(f"\nNulos rellenados con la mediana ({mediana})")
    return limpio


def transformar(ventas):
    """Crea columnas nuevas a partir de las existentes."""
    titulo("3. Columnas nuevas: operaciones vectorizadas, .dt y apply")
    ventas = ventas.assign(
        total=ventas["unidades"] * ventas["precio"],
        mes=ventas["fecha"].dt.month_name(),
        tamano_pedido=ventas["unidades"].apply(lambda u: "Grande" if u >= 25 else "Pequeño"),
    )
    print(ventas[["fecha", "unidades", "precio", "total", "mes", "tamano_pedido"]].head())
    return ventas


def seleccionar_y_filtrar(ventas):
    """Muestra selección con loc/iloc, filtros booleanos y query."""
    titulo("4. Selección y filtros: loc, iloc, máscaras, query")
    solo_cafe = ventas.loc[ventas["producto"] == "Café", ["ciudad", "total"]]
    bogota_grandes = ventas.query("ciudad == 'Bogotá' and total > 100000")
    print(f"iloc[0:3, 0:3]:\n{ventas.iloc[0:3, 0:3]}")
    print(f"\nloc con condición (Café):\n{solo_cafe}")
    print(f"\nquery (Bogotá y total > 100000):\n{bogota_grandes}")


def ordenar(ventas):
    """Ordena y obtiene el top de ventas."""
    titulo("5. Ordenamiento: sort_values y nlargest")
    ordenado = ventas.sort_values(["ciudad", "total"], ascending=[True, False])
    print(ordenado[["ciudad", "producto", "total"]].head())
    print(f"\nTop 3 ventas:\n{ventas.nlargest(3, 'total')[['fecha', 'ciudad', 'total']]}")


def agrupar(ventas):
    """Agrega información con groupby, agg y value_counts."""
    titulo("6. Agrupación: groupby, agg, value_counts")
    resumen = ventas.groupby("ciudad").agg(
        ventas_totales=("total", "sum"),
        unidades_promedio=("unidades", "mean"),
        pedidos=("total", "count"),
    )
    print(resumen.round(1))
    print(f"\nFrecuencia de productos:\n{ventas['producto'].value_counts()}")


def pivotear(ventas):
    """Construye una tabla dinámica ciudad x producto."""
    titulo("7. Tabla dinámica: pivot_table")
    tabla = ventas.pivot_table(
        index="ciudad", columns="producto", values="total",
        aggfunc="sum", fill_value=0, margins=True, margins_name="Total",
    )
    print(tabla)


def unir(ventas):
    """Combina las ventas con una tabla de metas usando merge."""
    titulo("8. Unión de tablas: merge")
    metas = pd.DataFrame({
        "ciudad": ["Bogotá", "Medellín", "Cali"],
        "meta": [1_500_000, 1_000_000, 800_000],
    })
    real = ventas.groupby("ciudad", as_index=False)["total"].sum()
    comparacion = real.merge(metas, on="ciudad", how="left")
    comparacion["cumplimiento_%"] = (comparacion["total"] / comparacion["meta"] * 100).round(1)
    print(comparacion)


def series_de_tiempo(ventas):
    """Agrega por mes con resample y calcula un acumulado."""
    titulo("9. Series de tiempo: resample y cumsum")
    mensual = ventas.set_index("fecha")["total"].resample("ME").sum().to_frame()
    mensual["acumulado"] = mensual["total"].cumsum()
    print(mensual)


def guardar_y_leer(ventas):
    """Exporta a CSV y lo vuelve a leer para verificar."""
    titulo("10. Entrada/salida: to_csv y read_csv")
    ventas.to_csv(RUTA_CSV, index=False)
    leido = pd.read_csv(RUTA_CSV, parse_dates=["fecha"])
    print(f"Guardado en {RUTA_CSV} — {len(leido)} filas leídas de vuelta")


def main():
    """Ejecuta el demo completo paso a paso."""
    ventas = crear_datos()
    explorar(ventas)
    ventas = limpiar(ventas)
    ventas = transformar(ventas)
    seleccionar_y_filtrar(ventas)
    ordenar(ventas)
    agrupar(ventas)
    pivotear(ventas)
    unir(ventas)
    series_de_tiempo(ventas)
    guardar_y_leer(ventas)


if __name__ == "__main__":
    main()
