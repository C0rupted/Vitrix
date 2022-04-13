import os
import tkinter as tk
from pathlib import Path

def on_closing():
    os._exit(0)

def notify(title: str, msg: str,):
    popup = tk.Tk()
    popup.title(title)
    path = Path(os.path.dirname(os.path.realpath(__file__))).parent
    popup.iconbitmap(os.path.join(path, "assets", "logo.ico"))
    label = tk.Label(popup, text=msg)
    label.pack(side="top", fill="x", pady=10)
    B1 = tk.Button(popup, text="Okay", command=popup.destroy)
    B1.pack(pady=10)
    popup.protocol("WM_DELETE_WINDOW", on_closing)
    popup.mainloop()

if __name__ == '__main__':
    notify("hello", "this is a test.")