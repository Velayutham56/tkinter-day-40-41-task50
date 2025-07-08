import tkinter as tk

window = tk.Tk()
window.title("Password Entry")
window.geometry("300x150")


tk.Label(window, text="Enter Password:").pack(pady=10)


password_entry = tk.Entry(window, show="*", width=30)
password_entry.pack(pady=5)

window.mainloop()
