import psutil
import os

keylogger_file = "Python/Projects/Keylogger-and-Detection-Script/keylogger.py"
text_log = "Python/Projects/Keylogger-and-Detection-Script/key_presses.txt"

def detect_script():
    for proc in psutil.process_iter(["pid", "name", "username"]):
        try:
            if proc.info["name"] == keylogger_file:
                print("[+] Script was found.")
                return True, proc
        except Exception as e:
            print(f"error encountered: {e}")
        
    print("[+] Script not found.")
    return False, None

def detect_text_log():
    file_exists = os.path.exists(text_log)

    if file_exists:
        print("[+] Log was found")
        return True
    else:
        print("[+] Log was not found")
        return False

def terminate_script(proc):
    proc.terminate()
    print("[+] Process Terminated")

def delete_log(text_log):
    os.remove(text_log)

def main():
    print("=" * 60)
    print("Keylogger Detection Script")
    print("=" * 60)

    script_detection_result, keylogger_process = detect_script()
    log_detection_result = detect_text_log()

    if script_detection_result == True and log_detection_result == True:
        terminate_script(keylogger_process)
        delete_log(text_log)

if __name__ == "__main__":
    main()