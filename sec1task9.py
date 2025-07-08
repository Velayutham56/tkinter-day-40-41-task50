import tkinter as tk

# Main window setup
root = tk.Tk()
root.title("Login Form with place()")
root.geometry("300x200")  # Set a defined window size

# Username Label and Entry
username_label = tk.Label(root, text="Username:")
username_label.place(x=30, y=30)

username_entry = tk.Entry(root)
username_entry.place(x=120, y=30)

# Password Label and Entry
password_label = tk.Label(root, text="Password:")
password_label.place(x=30, y=70)

password_entry = tk.Entry(root, show="*")
password_entry.place(x=120, y=70)

# Login Button
login_button = tk.Button(root, text="Login")
login_button.place(x=120, y=110)

root.mainloop()
