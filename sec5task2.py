import tkinter as tk

root = tk.Tk()
root.title("Sample Paragraph Inserter")

text_widget = tk.Text(root, width=50, height=15)
text_widget.pack(padx=10, pady=10)

# Insert a sample paragraph at the start of the widget
sample_paragraph = (
    "Tkinter is Python’s standard GUI toolkit and is great for building simple desktop applications. "
    "It comes bundled with Python, making it easy to get started. With widgets like buttons, labels, "
    "and text boxes, you can build interactive interfaces in no time!"
)
text_widget.insert("1.0", sample_paragraph)

root.mainloop()
