import tkinter as tk
from tkinter import messagebox

valid_username = "admin"
valid_password = "1234"

def check_login():
    username = username_entry.get().strip()
    password = password_entry.get().strip()

    if username == valid_username and password == valid_password:
        print("Login Success")
        messagebox.showinfo("Login Status", "Login Success")
    else:
        messagebox.showerror("Login Failed", "Invalid credentials")

window = tk.Tk()
window.title("Login Form")
window.geometry("300x180")


tk.Label(window, text="Username:").pack(pady=5)
username_entry = tk.Entry(window, width=30)
username_entry.pack()


tk.Label(window, text="Password:").pack(pady=5)
password_entry = tk.Entry(window, show="*", width=30)
password_entry.pack()


tk.Button(window, text="Login", command=check_login).pack(pady=10)

window.mainloop()
