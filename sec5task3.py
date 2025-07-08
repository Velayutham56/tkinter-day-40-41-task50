import tkinter as tk

def print_content():
    content = text_widget.get("1.0", tk.END).strip()
    print(content)

root = tk.Tk()
root.title("Print Text Content")

text_widget = tk.Text(root, width=50, height=15)
text_widget.pack(padx=10, pady=10)


text_widget.insert("1.0", "Write something here or keep this sample text.")


print_button = tk.Button(root, text="Print Content", command=print_content)
print_button.pack(pady=(0,10))

root.mainloop()
