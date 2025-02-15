import tkinter as tk
import pyautogui
import time
import threading
import subprocess
import sys

REQUIRED_PACKAGE = ["pyautogui"]

def install_missing_packages():
    for package in REQUIRED_PACKAGE:
        try:
            __import__(package)
        except ImportError:
            print(f"installation de {package}...")

    subprocess.run([sys.executable, "-m", "pip", "install", package], check=True)

    install_missing_packages()

running = False

def start_typing():
    global running
    running = True
    message = message_entry.get()

    def send_message():
        time.sleep(3)

        while running:
            pyautogui.write(message, interval=0.1)
            pyautogui.press("enter")
            time.sleep(2)

    threading.Thread(target=send_message, daemon=True).start()

def stop_typing():
    global running
    running = False

root = tk.Tk()
root.title("auto typer")
root.geometry("300x150")

tk.Label(root, text="Message a envoyer: ").pack()
message_entry = tk.Entry(root, width=30)
message_entry.pack()
message_entry.insert(0, "message test")

start_button = tk.Button(root, text="Démarrer", command=start_typing)
start_button.pack(pady=5)

stop_button = tk.Button(root, text="Arreter", command=stop_typing)
stop_button.pack()

root.mainloop()
