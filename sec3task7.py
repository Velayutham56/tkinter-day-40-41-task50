import tkinter as tk

window = tk.Tk()
window.title("Simple Notepad")
window.geometry("600x400")  


window.resizable(True, True)


text_area = tk.Text(window, wrap="word")
text_area.pack(expand=True, fill="both")

window.mainloop()
