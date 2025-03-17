
# 🚀 Pi Network Node Monitoring Script

Automatiza el monitoreo de tu nodo de **Pi Network** y recibe notificaciones en **Telegram** en tiempo real.

---

## 📋 Requisitos

Para ejecutar el script en **Windows**, asegúrate de tener lo siguiente:

### 🐍 1. Python Instalado

1. Descarga e instala Python desde [python.org](https://www.python.org/downloads/).
2. Durante la instalación, **marca la casilla** `"Add Python to PATH"`.
3. Verifica la instalación ejecutando en la terminal:

   ```bash
   python --version
   ```

✅ Debería mostrar algo como: `Python 3.x.x`.

---

### 📦 2. Librerías Requeridas

El script utiliza las siguientes librerías:

- ✅ `os`, `sys`, `json`, `datetime` (Incluidas por defecto en Python).
- ✅ `requests` (Se debe instalar manualmente).

Para instalar `requests`, ejecuta:

```bash
pip install requests
```

---

## 🚀 Primeros Pasos

### 📂 1. Clonar el Repositorio

Copia este repositorio a tu máquina local:

```bash
git clone https://github.com/AnaCorral-DevOps/monitoring_pi_network_node.git
```

---

## 🤖 2. Crear un Bot en Telegram (BotFather)

1. Abre **Telegram** y busca `@BotFather`.
2. Inicia una conversación y usa el comando:

   ```bash
   /newbot
   ```

3. Sigue las instrucciones:
   - Asigna un nombre a tu bot (e.g., `MyPythonBot`).
   - Elige un **nombre de usuario** que termine en `bot` (e.g., `MyPythonBot_bot`).

4. Guarda el **token de acceso** que te proporciona BotFather. 🚨

---

## 📌 3. Obtener el `TELEGRAM_CHAT_ID`

1. Escribe cualquier mensaje a tu bot (`/start` es suficiente).
2. Abre tu navegador e ingresa:

   ```
   https://api.telegram.org/bot<YOUR_TOKEN>/getUpdates
   ```

   Reemplaza `<YOUR_TOKEN>` con el token que te dio BotFather.

3. En la respuesta JSON, busca el campo `id` dentro del objeto `chat`.

✅ Ese es tu **`TELEGRAM_CHAT_ID`**.

---

## 🛠️ 4. Crear el Archivo de Configuración

1. Crea un archivo llamado **`config.json`** en el mismo directorio del script.
2. Añade el siguiente contenido (sustituye con tus valores):

```json
{
    "TELEGRAM_TOKEN": "YOUR_TOKEN",
    "TELEGRAM_CHAT_ID": "YOUR_CHAT_ID"
}
```

🔍 **Ejemplo:**

```json
{
    "TELEGRAM_TOKEN": "123456789:ABCdefGhIJKlmNoPQRstuVWXyz",
    "TELEGRAM_CHAT_ID": "987654321"
}
```

---

## 📜 5. Generar el Archivo `.bat`

Desde el directorio del repositorio clonado, ejecuta:

```bash
python create_monitor_docker.py
```

### ✅ ¿Qué hace este comando?

- Crea un archivo **`.bat`** que automatiza la ejecución del script.
- El archivo `.bat` contendrá:

```bash
@echo off
[Python Path] [Script Path]
```

Donde:

- **[Python Path]:** Ruta del intérprete de Python (detectado automáticamente).
- **[Script Path]:** Ruta al script `monitor_docker_pi.py`.

---

## 📅 6. Configurar en el Programador de Tareas de Windows

### 📌 Paso 1: Abrir el Programador de Tareas

1. Presiona `Win + S` y busca **"Programador de Tareas"**.
2. Haz clic en **Crear Tarea**.

---

### ⚙️ Paso 2: Configurar la Tarea

1. **General:**
   - Nombre: `Monitor Docker PI`.
   - Marca la casilla **"Ejecutar con los privilegios más altos"**.

2. **Desencadenador (Trigger):**
   - Haz clic en **Nuevo**.
   - Elige **Al iniciar** o **Diariamente** según prefieras.
   - Marca **Repetir cada 5 minutos** y selecciona **Indefinidamente**.

3. **Acción:**
   - Haz clic en **Nuevo**.
   - En **Programa/script**, selecciona el archivo `.bat` que generaste.

---

### ✅ Paso 3: Guardar y Ejecutar

1. Haz clic en **Aceptar** para guardar la configuración.
2. ¡Listo! El monitoreo se ejecutará automáticamente cada 5 minutos.

---

## 📣 Contribuciones

¡Las contribuciones son bienvenidas! Si tienes ideas para mejorar este proyecto, no dudes en abrir un **Pull Request** o **Issue**.

---

## 📄 Licencia

Este proyecto está bajo la licencia **MIT**.

---

💬 **¿Dudas o sugerencias?**  
¡Contáctame en [Telegram](https://t.me/MyPythonBot_bot)!
