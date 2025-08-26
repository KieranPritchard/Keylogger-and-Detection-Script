import psutil
import os

keylogger_file = "Python/Projects/Keylogger-and-Detection-Script/keylogger.py"

def detect_script():
    for proc in psutil.process_iter(["pid", "name", "username"]):
        process =  psutil.Process(proc[0])

        if process.name() == keylogger_file:
            process.terminate()
            print("Script was successfully removed.")
        else:
            print("Script not found yet.")