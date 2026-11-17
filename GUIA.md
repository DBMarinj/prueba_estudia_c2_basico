# 🧭 Guía: qué debes hacer

Esta guía te lleva de principio a fin. Si te pierdes, vuelve aquí.

## 🎯 Lo que vas a lograr

Al terminar habrás hecho lo mismo que hace un equipo de datos todos los días:

1. 🔍 **Revisar** el trabajo de otra persona con un comentario útil.
2. 🚀 **Proponer** un cambio propio con un pull request.
3. 💬 **Responder** a una revisión.

## 🧰 Antes de empezar

- ✅ Una **cuenta de GitHub**, con la sesión iniciada en el navegador.
- ✅ **Git** instalado. Compruébalo en la terminal: `git --version`.
- ✅ Si trabajas en la terminal, haber iniciado sesión con `gh auth login` (lo hiciste con la guía de instalación).

## 🛤️ El camino, en orden

### 💬 Paso 1 · Comenta un pull request (10 minutos)

Abre el PR [«Ejemplo: presentación del profesor»](https://github.com/JuanFeDS/prueba_estudia_c2_basico/pull/1) y deja un comentario en **una línea concreta** del archivo. El profesor dejó tres cosas por mejorar a propósito.

Instrucciones detalladas: [tareas/01-comentar-un-pr.md](tareas/01-comentar-un-pr.md)

🏁 **Terminaste cuando:** tu comentario aparece en el PR, firmado con tu usuario.

### 🍴 Paso 2 · Abre tu propio pull request (20 minutos)

Haz un fork de este repositorio, crea tu archivo `estudiantes/TU-USUARIO.md` en una rama nueva y abre un PR hacia este repositorio.

Instrucciones detalladas: [tareas/02-abre-tu-pr.md](tareas/02-abre-tu-pr.md)

🏁 **Terminaste cuando:** tu PR aparece en la pestaña **Pull requests** de este repositorio, con la plantilla completa.

### 📮 Paso 3 · Entrega

Pega en el chat de la clase el **enlace de tu PR**.

## 📏 Reglas

1. 🔒 **No pongas datos personales** (celular, correo, documento, dirección). Este repositorio es público.
2. 🚫 **No fusiones** nada. Aquí se comenta y se aprueba, pero solo el profesor fusiona.
3. 📁 **Trabaja solo en tu archivo**, `estudiantes/TU-USUARIO.md`.
4. 🤝 Comenta con **respeto y utilidad**: qué ves y qué cambiarías, sin juzgar a la persona.

## 🆘 Si algo falla

| Qué ves | Qué hacer |
|---|---|
| ❌ `git: command not found` | Git no está instalado. Sigue la guía de instalación de herramientas |
| 🔑 `Authentication failed` o `Permission denied` | Estás intentando subir al repositorio del profesor y no al tuyo. Revisa que clonaste **tu fork**, con tu usuario en la dirección |
| 🔎 `Repository not found` | La dirección está mal escrita, o falta cambiar `TU-USUARIO` por el tuyo |
| 🙈 No aparece el botón **Compare & pull request** | Entra a la pestaña **Pull requests** de tu fork y pulsa **New pull request**. Verifica que hiciste `git push` |
| 📄 Mi PR no muestra mi archivo | Se te olvidó `git add`, `git commit` o `git push`. Repítelos en ese orden |
| 🎯 Mi PR apunta a mi propio repositorio | En la pantalla del PR, cambia **base repository** a `JuanFeDS/prueba_estudia_c2_basico` |
| 🌿 `git push` dice que la rama no existe | Usa `git push -u origin nombre-de-tu-rama` |
| ⚔️ Aparecen marcas `<<<<<<<` en un archivo | Es un conflicto. Elige qué versión queda, borra las marcas, y haz commit. Pide ayuda si es tu primera vez |

💡 Si nada de esto resuelve tu caso, escribe al chat el **mensaje exacto** que ves.

## 📖 Vocabulario

| Palabra | Qué significa |
|---|---|
| 🍴 **Fork** | Tu copia personal de un repositorio ajeno, en tu cuenta |
| 📥 **Clonar** | Traer esa copia a tu computador |
| 🌿 **Rama (branch)** | Una línea de trabajo paralela, para no tocar la principal |
| 💾 **Commit** | Guardar una versión de tus cambios, con un mensaje |
| ⬆️ **Push** | Subir tus commits a GitHub |
| 📬 **Pull request (PR)** | Una propuesta para que tus cambios entren al repositorio original |
| 🔍 **Revisión (review)** | Los comentarios de otra persona sobre tu PR |
| 🔀 **Merge (fusionar)** | Aceptar el PR e integrar sus cambios. Aquí solo lo hace el profesor |
