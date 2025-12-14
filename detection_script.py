import psutil
import os

# This function detects the keyloggers process
def detect_script(keylogger_file):
    # The loop retreves the processes and the parameters i'm after
    for proc in psutil.process_iter(["pid", "name", "username", "cmdline"]):
        # This tries to get the cmdline command to compare it to the file to see if the command matchs to the file
        try:
            # The process info for cmdline
            cmdline = proc.info.get("cmdline")
            # checks if the path of cmdline and the keylogger appear in each other
            if cmdline and os.path.basename(keylogger_file) in cmdline[-1]:
                # this returns if the script was found and the process
                print("[+] Script was found.")
                # Returns true and the process
                return True, proc
        except Exception as e:
            # Outputs error message
            print(f"error encountered: {e}")
    # Outputs the result if the script is not found
    print("[-] Script not found.")
    # Returns false and none
    return False, None

# This detects if there is a text log by checking if the text file is at the path
def detect_text_log(text_log):
    # Checks if the text log exists
    file_exists = os.path.exists(text_log)

    # Checks the log exists
    if file_exists:
        # Outputs the log was found
        print("[+] Log was found")
        # Returns true
        return True
    else:
        # Outputs it does not found
        print("[-] Log was not found")
        # Returns fault
        return False

# This terminates the scripts
def terminate_script(proc):
    # Terminates the process
    proc.terminate()
    # Outputs that it is terminated
    print("[+] Process Terminated")

# This deletes the script
def delete_log(text_log):
    # Removes the files
    os.remove(text_log)
    # Outputs that the log was deleted
    print("[+] Log was deleted.")

# This is the main logic of the program that triggers the forementioned functions
def main():
    # Stores the keylogger file and log paths
    keylogger_file = "./Keylogger-and-Detection-Script/keylogger.py"
    text_log = "./key_presses.txt"

    # Outputs the header of the script
    print("=" * 60)
    print("Keylogger Detection Script")
    print("=" * 60)

    # Gets the result and keylogger process from the detect script function
    script_detection_result, keylogger_process = detect_script(keylogger_file)
    # Gets the log detection result from the function
    log_detection_result = detect_text_log(text_log)

    # checks if both the script and log are detected
    if script_detection_result == True and log_detection_result == True:
        # Terminates the script and deletes the logs
        terminate_script(keylogger_process)
        delete_log(text_log)
    # deletes the log if the script isnt detected
    elif log_detection_result == True and script_detection_result == False:
        delete_log(text_log)

# Starts the program
if __name__ == "__main__":
    main()