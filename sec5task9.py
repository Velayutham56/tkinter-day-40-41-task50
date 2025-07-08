import tkinter as tk
from tkinter import filedialog, messagebox

def load_text_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()
                text_widget.delete("1.0", tk.END)  # Clear existing content
                text_widget.insert("1.0", content)  # Load new content
        except Exception as e:
            messagebox.showerror("Error", f"Could not read file:\n{e}")

root = tk.Tk()
root.title("Load Text from File")

text_widget = tk.Text(root, wrap="word", width=50, height=15)
text_widget.pack(padx=10, pady=(10,0))

load_button = tk.Button(root, text="Load File", command=load_text_file)
load_button.pack(pady=(5,10))

root.mainloop()
