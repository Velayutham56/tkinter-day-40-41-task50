import tkinter as tk
from tkinter import messagebox
import re

def validate_email(email):
    email_pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(email_pattern, email)

def submit_form():
    email = email_entry.get().strip()

    if not email:
        messagebox.showwarning("Validation Error", "Email field cannot be empty.")
    elif not validate_email(email):
        messagebox.showwarning("Validation Error", "Invalid email format.")
    else:
        print(f"Email entered: {email}")
        messagebox.showinfo("Success", "Email is valid!")

window = tk.Tk()
window.title("Email Validation")
window.geometry("350x150")

tk.Label(window, text="Email:").pack(pady=5)
email_entry = tk.Entry(window, width=35)
email_entry.pack(pady=5)

tk.Button(window, text="Submit", command=submit_form).pack(pady=10)

window.mainloop()
