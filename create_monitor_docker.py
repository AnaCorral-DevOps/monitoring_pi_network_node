import os
import sys

def create_bat_file():
    """Creates a .bat file to run monitor_docker_pi.py automatically."""
    directory = os.path.dirname(os.path.abspath(__file__))
    bat_file_path = os.path.join(directory, "monitor_docker_pi.bat")
    python_path = sys.executable
    script_path = os.path.join(directory, "monitor_docker_pi.py")

    with open(bat_file_path, "w") as bat_file:
        bat_file.write(f"@echo off\n{python_path} {script_path}\n")

    print("Batch file created successfully at:", bat_file_path)

if __name__ == "__main__":
    create_bat_file()