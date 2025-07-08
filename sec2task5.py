import tkinter as tk

def display_text():
    entered_text = entry.get()
    label.config(text=f"You entered: {entered_text}")

window = tk.Tk()
window.title("Text Display")
window.geometry("300x150")

entry = tk.Entry(window, width=25)
entry.pack(pady=10)

btn = tk.Button(window, text="Display", command=display_text)
btn.pack(pady=5)

label = tk.Label(window, text="")
label.pack(pady=10)

window.mainloop()
