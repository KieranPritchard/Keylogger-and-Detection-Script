import psutil
import os

keylogger_file = "Python/Projects/Keylogger-and-Detection-Script/keylogger.py"
text_log = "Python/Projects/Keylogger-and-Detection-Script/key_presses.txt"

def detect_script():
    for proc in psutil.process_iter(["pid", "name", "username"]):
        process =  psutil.Process(proc[0])

        if process.name() == keylogger_file:
            print("[+] Script was Found.")
        else:
            print("[+] Script not found yet.")

def detect_text_log():
    file_exists = os.path.exists(text_log)

    if file_exists:
        print("[+] Log was found")
        return True
    else:
        print("[+] Log was not found")
        return False