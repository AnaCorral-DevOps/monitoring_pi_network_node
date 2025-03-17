import os
import requests
import sys
import json
from datetime import datetime, timedelta

# Get the absolute path of the current script
directory = os.path.dirname(os.path.abspath(__file__))

# Load credentials from config.json
CONFIG_FILE = os.path.join(directory, "config.json")


def load_config():
    if not os.path.exists(CONFIG_FILE):
        print(f"Error: The file {CONFIG_FILE} was not found")
        sys.exit(1)

    with open(CONFIG_FILE, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError as e:
            print(f"Error reading the configuration file: {e}")
            sys.exit(1)


config = load_config()

TOKEN = config.get("TELEGRAM_TOKEN")
CHAT_ID = config.get("TELEGRAM_CHAT_ID")

if not TOKEN or not CHAT_ID:
    print("Error: TOKEN or CHAT_ID are not defined in the config.json file")
    sys.exit(1)

# Log file and retention
LOG_FILE = os.path.join(directory, "script_log.txt")
LOG_RETENTION_DAYS = 7  # Delete logs older than 7 days


def clean_old_logs():
    """Deletes log records older than LOG_RETENTION_DAYS."""
    if not os.path.exists(LOG_FILE):
        return

    with open(LOG_FILE, "r", encoding="utf-8") as log:
        lines = log.readlines()

    cutoff_date = datetime.now() - timedelta(days=LOG_RETENTION_DAYS)
    filtered_lines = [line for line in lines if is_recent_log(line, cutoff_date)]

    with open(LOG_FILE, "w", encoding="utf-8") as log:
        log.writelines(filtered_lines)


def is_recent_log(log_line, cutoff_date):
    """Checks if a log is recent based on its timestamp."""
    try:
        log_timestamp = datetime.strptime(log_line[1:20], "%Y-%m-%d %H:%M:%S")
        return log_timestamp >= cutoff_date
    except ValueError:
        return True  # If the line has no date, do not delete it


def write_log(message):
    """Saves a message to the log file and cleans old records."""
    clean_old_logs()  # Delete old logs before writing
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a", encoding="utf-8") as log:
        log.write(f"[{timestamp}] {message}\n")


def send_telegram_message(message):
    """Sends an alert to Telegram and logs the attempt."""
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    params = {'chat_id': CHAT_ID, 'text': message}

    try:
        response = requests.get(url, params=params)
        write_log(f"Message sent: {message}")
        return response.json()
    except requests.exceptions.RequestException as e:
        write_log(f"Error sending message: {e}")
        return None


def check_pi_network_node():
    """Checks if the Pi Network node is running."""
    try:
        result = os.popen("docker ps --filter name=testnet2 --format '{{.ID}}'").read().strip()

        if not result:
            send_telegram_message("Alert! The Pi Network node is not running.")
            write_log("Pi Network node stopped, notification sent.")
        else:
            write_log("The Pi Network node is running correctly.")

    except Exception as e:
        send_telegram_message(f"Error checking the Pi Network node: {e}")
        write_log(f"Error checking the Pi Network node: {e}")


def main():
    write_log("Verification started")
    check_pi_network_node()
    write_log("Verification completed")


if __name__ == "__main__":
    main()
