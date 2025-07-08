import tkinter as tk

root = tk.Tk()
root.title("Text Widget with Scrollbar")


frame = tk.Frame(root)
frame.pack(padx=10, pady=10)


text_widget = tk.Text(frame, wrap="word", width=50, height=15)
text_widget.pack(side="left", fill="both", expand=True)


scrollbar = tk.Scrollbar(frame, command=text_widget.yview)
scrollbar.pack(side="right", fill="y")


text_widget.config(yscrollcommand=scrollbar.set)

text_widget.insert("1.0", "Scroll me! 🧾\n" + ("This is a sample line.\n" * 30))

root.mainloop()
