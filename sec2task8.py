import tkinter as tk

def on_key_press(event):
    if event.keysym == "Up":
        label.config(text="Direction: Up ⬆️")
    elif event.keysym == "Down":
        label.config(text="Direction: Down ⬇️")

window = tk.Tk()
window.title("Arrow Key Direction")
window.geometry("300x150")

label = tk.Label(window, text="Press ↑ or ↓", font=("Arial", 14))
label.pack(pady=40)

# Bind arrow keys to the window
window.bind("<Up>", on_key_press)
window.bind("<Down>", on_key_press)

window.mainloop()
