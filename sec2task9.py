import tkinter as tk

def track_mouse(event):
    label.config(text=f"Mouse Position: x={event.x}, y={event.y}")

window = tk.Tk()
window.title("Mouse Tracker")
window.geometry("400x200")

label = tk.Label(window, text="Move your mouse!", font=("Arial", 12))
label.pack(pady=20)


window.bind("<Motion>", track_mouse)

window.mainloop()
