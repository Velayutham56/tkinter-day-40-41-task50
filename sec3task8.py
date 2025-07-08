import tkinter as tk

window = tk.Tk()
window.title("Centered Window")


win_width = 400
win_height = 250

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()


x = (screen_width // 2) - (win_width // 2)
y = (screen_height // 2) - (win_height // 2)


window.geometry(f"{win_width}x{win_height}+{x}+{y}")

window.mainloop()
