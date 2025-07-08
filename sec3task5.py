import tkinter as tk

def update_size(event):
    width = event.width
    height = event.height
    label.config(text=f"Width: {width}, Height: {height}")

window = tk.Tk()
window.title("Window Size Tracker")
window.geometry("300x200")

label = tk.Label(window, text="Resize the window", font=("Arial", 12))
label.pack(pady=20)

window.bind("<Configure>", update_size)

window.mainloop()
