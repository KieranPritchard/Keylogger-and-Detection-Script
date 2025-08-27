import psutil
import os

# This function detects the keyloggers process
def detect_script(keylogger_file):
    # The loop retreves the processes and the parameters i'm after
    for proc in psutil.process_iter(["pid", "name", "username", "cmdline"]):
        # This tries to get the cmdline command to compare it to the file to see if the command matchs to the file
        try:
            cmdline = proc.info.get("cmdline")
            if cmdline and os.path.basename(keylogger_file) in cmdline[-1]:
                # this returns if the script was found and the process
                print("[+] Script was found.")
                return True, proc
        except Exception as e:
            print(f"error encountered: {e}")
    # Outputs the result if the script is not found
    print("[-] Script not found.")
    return False, None

# This detects if there is a text log by checking if the text file is at the path
def detect_text_log(text_log):
    file_exists = os.path.exists(text_log)

    if file_exists:
        print("[+] Log was found")
        return True
    else:
        print("[-] Log was not found")
        return False

# This terminates the scripts
def terminate_script(proc):
    proc.terminate()
    print("[+] Process Terminated")

# This deletes the script
def delete_log(text_log):
    os.remove(text_log)
    print("[+] Log was deleted.")

# This is the main logic of the program that triggers the forementioned functions
def main():
    keylogger_file = "Python/Projects/Keylogger-and-Detection-Script/keylogger.py"
    text_log = "Python/Projects/Keylogger-and-Detection-Script/key_presses.txt"

    print("=" * 60)
    print("Keylogger Detection Script")
    print("=" * 60)

    script_detection_result, keylogger_process = detect_script(keylogger_file)
    log_detection_result = detect_text_log(text_log)

    if script_detection_result == True and log_detection_result == True:
        terminate_script(keylogger_process)
        delete_log(text_log)
    elif log_detection_result == True and script_detection_result == False:
        delete_log(text_log)

if __name__ == "__main__":
    main()