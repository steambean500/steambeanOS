import tkinter as tk
from PIL import Image, ImageTk
import subprocess
import os
import RPi.GPIO as GPIO
import time

FAN_PIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(FAN_PIN, GPIO.OUT)
GPIO.output(FAN_PIN, True)

def launch_app(command):
    subprocess.Popen(command, shell=True)

root = tk.Tk()
root.attributes('-fullscreen', True)
root.config(bg='black')

def make_button(image_path, command, row, col):
    img = Image.open(image_path)
    img = img.resize((150, 150))
    img = ImageTk.PhotoImage(img)
    btn = tk.Button(root, image=img, bg='black', command=command, border=0)
    btn.image = img
    btn.grid(row=row, column=col, padx=20, pady=20)

make_button("images/steamlink.png", lambda: launch_app("steamlink"), 0, 0)
make_button("images/retropie.png", lambda: launch_app("emulationstation"), 0, 1)
make_button("images/chrome.png", lambda: launch_app("chromium-browser"), 1, 0)
make_button("images/spotify.png", lambda: launch_app("chromium-browser https://open.spotify.com"), 1, 1)

exit_btn = tk.Button(root, text="Exit", command=root.destroy, bg="red", fg="white")
exit_btn.grid(row=2, column=1, pady=10)

root.mainloop()