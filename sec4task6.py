import tkinter as tk
from tkinter import messagebox
import re

def submit_form():
    name = name_entry.get().strip()
    email = email_entry.get().strip()

   
    if not name:
        messagebox.showwarning("Validation Error", "Please enter your name.")
        return

    email_pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    if not re.match(email_pattern, email):
        messagebox.showerror("Validation Error", "Please enter a valid email address.")
        return

    print(f"Name: {name}")
    print(f"Email: {email}")

window = tk.Tk()
window.title("Form with Regex Validation")
window.geometry("350x200")


tk.Label(window, text="Name:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
name_entry = tk.Entry(window, width=30)
name_entry.grid(row=0, column=1, padx=10, pady=5)


tk.Label(window, text="Email:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
email_entry = tk.Entry(window, width=30)
email_entry.grid(row=1, column=1, padx=10, pady=5)

submit_btn = tk.Button(window, text="Submit", command=submit_form)
submit_btn.grid(row=2, column=0, columnspan=2, pady=10)

window.mainloop()
