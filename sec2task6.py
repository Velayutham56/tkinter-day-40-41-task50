import tkinter as tk
from tkinter import messagebox

def show_message():
    messagebox.showinfo("Greetings", "Hello! This is your message box.")

window = tk.Tk()
window.title("Message Box Example")
window.geometry("300x150")

btn = tk.Button(window, text="Show Message", command=show_message)
btn.pack(pady=40)

window.mainloop()
