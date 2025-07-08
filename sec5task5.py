import tkinter as tk

def update_count(event=None):
    content = text_widget.get("1.0", tk.END).strip()
    char_count = len(content)
    word_count = len(content.split())
    count_label.config(text=f"Characters: {char_count} | Words: {word_count}")

root = tk.Tk()
root.title("Text Stats Tracker")

text_widget = tk.Text(root, width=50, height=15)
text_widget.pack(padx=10, pady=(10,0))
text_widget.bind("<KeyRelease>", update_count)

count_label = tk.Label(root, text="Characters: 0 | Words: 0")
count_label.pack(pady=(5,10))

root.mainloop()
