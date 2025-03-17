## Requirements

To run the Python script on **Windows**, ensure you have the following:

### 1. **Python Installed**
   - Download and install Python from the official website: [python.org](https://www.python.org/downloads/).
   - During installation, make sure to check the box that says **"Add Python to PATH"**.
   - Verify the installation by opening a command prompt and running:
     ```bash
     python --version
     ```
     This should display the installed Python version (e.g., `Python 3.x.x`).

### 2. **Required Libraries**
   The script uses the following libraries:
   - `os` (included in Python's standard library)
   - `requests` (needs to be installed)
   - `sys` (included in Python's standard library)
   - `json` (included in Python's standard library)
   - `datetime` (included in Python's standard library)

   To install the `requests` library, open a command prompt and run:
   ```bash
   pip install requests

## 3: Create a Bot in BotFather

1. Open Telegram and search for `@BotFather` in the search bar.
2. Start a conversation with BotFather.
3. Use the `/newbot` command to create a new bot.
4. Follow BotFather's instructions:
   - Provide a name for your bot (e.g., `MyPythonBot`).
   - Provide a unique username for your bot (it must end with `bot`, e.g., `MyPythonBot_bot`).
5. Once the bot is created, BotFather will provide you with an **access token**. This token is required to interact with the Telegram API. Save it in a secure place.

## 4: Get the `TELEGRAM_CHAT_ID`

1. Open Telegram and search for the bot you just created (e.g., `@MyPythonBot_bot`).
2. Start a conversation with the bot by sending any message (e.g., `/start`).
3. Open your browser and visit the following URL, replacing `YOUR_TOKEN` with the token you obtained from BotFather: https://api.telegram.org/bot<YOUR_TOKEN>/getUpdates

4. In the JSON response, look for the `id` field inside the `chat` object. This is your `TELEGRAM_CHAT_ID`. Save it in a secure place.

## 5: Create a JSON Configuration File

1. Create a file named `config.json` in the same directory as your Python script.
2. Add the following content to the file, replacing `YOUR_TOKEN` and `YOUR_CHAT_ID` with the values you obtained earlier:

```json
{
    "TELEGRAM_TOKEN": "YOUR_TOKEN",
    "TELEGRAM_CHAT_ID": "YOUR_CHAT_ID"
}

Example:

{
    "TELEGRAM_TOKEN": "123456789:ABCdefGhIJKlmNoPQRstuVWXyz",
    "TELEGRAM_CHAT_ID": "987654321"
}