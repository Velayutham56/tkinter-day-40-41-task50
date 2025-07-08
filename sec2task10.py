import tkinter as tk

def on_hover(event):
    button.config(text="Hovered!")

def on_leave(event):
    button.config(text="Hover Me")

window = tk.Tk()
window.title("Button Hover")
window.geometry("300x150")

button = tk.Button(window, text="Hover Me")
button.pack(pady=40)


button.bind("<Enter>", on_hover)
button.bind("<Leave>", on_leave)

window.mainloop()
