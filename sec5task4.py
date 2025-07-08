import tkinter as tk

def clear_text():
    text_widget.delete("1.0", tk.END)

root = tk.Tk()
root.title("Clear Text Content")

text_widget = tk.Text(root, width=50, height=15)
text_widget.pack(padx=10, pady=10)


text_widget.insert("1.0", "This is some sample text that will be cleared.")

clear_button = tk.Button(root, text="Clear Text", command=clear_text)
clear_button.pack(pady=(0,10))

root.mainloop()
