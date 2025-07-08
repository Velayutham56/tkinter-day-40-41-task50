import tkinter as tk

def clear_entry():
    entry.delete(0, tk.END)  

window = tk.Tk()
window.title("Clear Entry Field")
window.geometry("300x120")

entry = tk.Entry(window, width=30)
entry.pack(pady=10)

clear_btn = tk.Button(window, text="Clear", command=clear_entry)
clear_btn.pack(pady=5)

window.mainloop()
