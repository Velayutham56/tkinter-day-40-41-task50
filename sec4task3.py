import tkinter as tk

window = tk.Tk()
window.title("Pre-filled Entry")
window.geometry("300x100")

entry = tk.Entry(window, width=30)
entry.pack(pady=20)


entry.insert(0, "Enter Name")

window.mainloop()
