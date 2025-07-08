import tkinter as tk

def on_enter(event):
    entered_text = entry.get()
    label.config(text=f"You typed: {entered_text}")

window = tk.Tk()
window.title("Enter Key Event")
window.geometry("300x150")

entry = tk.Entry(window, width=25)
entry.pack(pady=10)


entry.bind("<Return>", on_enter)

label = tk.Label(window, text="")
label.pack(pady=10)

window.mainloop()
