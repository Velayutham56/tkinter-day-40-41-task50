import tkinter as tk

root = tk.Tk()
root.title("Geometry Manager Conflict")

# Title label using pack()
title_label = tk.Label(root, text="Login Form", font=("Arial", 16))
title_label.pack(pady=10)

# Attempting to use grid() below in the same root window
username_label = tk.Label(root, text="Username:")
username_label.grid(row=0, column=0, padx=5, pady=5)

username_entry = tk.Entry(root)
username_entry.grid(row=0, column=1, padx=5, pady=5)

password_label = tk.Label(root, text="Password:")
password_label.grid(row=1, column=0, padx=5, pady=5)

password_entry = tk.Entry(root, show="*")
password_entry.grid(row=1, column=1, padx=5, pady=5)

root.mainloop()
