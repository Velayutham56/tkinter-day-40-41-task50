import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import os

def save_entry():
    content = text_widget.get("1.0", tk.END).strip()
    if not content:
        messagebox.showwarning("Empty", "Diary entry is empty!")
        return

    date_str = datetime.now().strftime("%Y-%m-%d")
    filename = f"diary_{date_str}.txt"
    try:
        os.makedirs("diary_entries", exist_ok=True)
        filepath = os.path.join("diary_entries", filename)
        with open(filepath, "w", encoding="utf-8") as file:
            file.write(content)
        messagebox.showinfo("Saved", f"Diary saved as {filename}")
    except Exception as e:
        messagebox.showerror("Error", f"Could not save diary entry:\n{e}")

root = tk.Tk()
root.title("Mini Diary App")

text_widget = tk.Text(root, wrap="word", width=60, height=20)
text_widget.pack(padx=10, pady=(10, 0))

save_button = tk.Button(root, text="Save Entry", command=save_entry)
save_button.pack(pady=(5, 10))

root.mainloop()
