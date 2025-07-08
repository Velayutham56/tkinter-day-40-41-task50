import tkinter as tk
from tkinter import messagebox

def save_notes():
    content = text_widget.get("1.0", tk.END).strip()
    if content:
        with open("notes.txt", "w", encoding="utf-8") as file:
            file.write(content)
        messagebox.showinfo("Success", "Notes saved to notes.txt")
    else:
        messagebox.showwarning("Empty", "No content to save!")

root = tk.Tk()
root.title("Notes App")

text_widget = tk.Text(root, width=50, height=15)
text_widget.pack(padx=10, pady=10)

save_button = tk.Button(root, text="Save Notes", command=save_notes)
save_button.pack(pady=(0,10))

root.mainloop()
