# 🚀 Pi Network Node Monitoring Script

Automate the monitoring of your **Pi Network** node and receive real-time notifications on **Telegram**.

---

## 📋 Requirements

To run the script on **Windows**, make sure you have the following:

### 🐍 1. Python Installed

1. Download and install Python from [python.org](https://www.python.org/downloads/).
2. During installation, **check the box** `"Add Python to PATH"`.
3. Verify the installation by running in the terminal:

   ```bash
   python --version
   ```

✅ It should display something like: `Python 3.x.x`.

---

### 📦 2. Required Libraries

The script uses the following libraries:

- ✅ `os`, `sys`, `json`, `datetime` (Included by default in Python).
- ✅ `requests` (Must be installed manually).

To install `requests`, run:

```bash
pip install requests
```

---

## 🚀 Getting Started

### 📂 1. Clone the Repository

Copy this repository to your local machine:

```bash
git clone https://github.com/AvispaCoder/monitoring_pi_network_node.git
```

---

## 🤖 2. Create a Telegram Bot (BotFather)

1. Open **Telegram** and search for `@BotFather`.
2. Start a conversation and use the command:

   ```bash
   /newbot
   ```

3. Follow the instructions:
   - Assign a name to your bot (e.g., `MyPythonBot`).
   - Choose a **username** that ends with `bot` (e.g., `MyPythonBot_bot`).

4. Save the **access token** provided by BotFather. 🚨

---

## 📌 3. Get the `TELEGRAM_CHAT_ID`

1. Send any message to your bot (`/start` is enoug).
2. Open your browser and enter:

   ```
   https://api.telegram.org/bot<YOUR_TOKEN>/getUpdates
   ```

   Replace `<YOUR_TOKEN>` with the token provided by BotFather.

3. In the JSON response, look for the `id` field inside the `chat` object.

✅ That is your **`TELEGRAM_CHAT_ID`**.

---

## 🛠️ 4. Create the Configuration File

1. Create a file named **`config.json`** in the same directory as the script.
2. Add the following content (replace with your values):

```json
{
    "TELEGRAM_TOKEN": "YOUR_TOKEN",
    "TELEGRAM_CHAT_ID": "YOUR_CHAT_ID"
}
```

🔍 **Example:**

```json
{
    "TELEGRAM_TOKEN": "123456789:ABCdefGhIJKlmNoPQRstuVWXyz",
    "TELEGRAM_CHAT_ID": "987654321"
}
```

---

## 📜 5. Generate the `.bat` File

From the cloned repository directory, run:

```bash
python create_monitor_docker.py
```

### ✅ What does this command do?

- Creates a **`.bat`**  file that automates the execution of the script.
- The `.bat` file will contain:

```bash
@echo off
[Python Path] [Script Path]
```

Donde:

- **[Python Path]:** Path to the Python interpreter (automatically detected).
- **[Script Path]:** Path to the `monitor_docker_pi.py` script.

---

## 📅 6. Configure in Windows Task Scheduler

### 📌 Step 1: Open Task Scheduler

1. Press  `Win + S` and search for **"Task Scheduler"**.
2. Click on **Create Task**.

---

### ⚙️ Step 2: Configure the Task

1. **General:**
   - Name: `Monitor Docker PI`.
   - Check the box  **"Run with highest privilege"**.

2. **Trigger:**
   - Click on **New**.
   - Choose **At startup**.
   - Check **Repeat every 5 minutes** and select **Indefinitely**.

3. **Acción:**
   - Click on **New**.
   - In  **Program/script**, select the `.bat` file you generated.

---

### ✅ Step 3: Save and Run

1. Click **OK** to save the configuration.
2. Done! The monitoring will run automatically every 5 minutes.

---

## 📣 Contributions

Contributions are welcome! If you have ideas to improve this project, feel free to open a **Pull Request** or **Issue**.

---

## 📄 Licencia

This project is licensed under the **MIT**.

