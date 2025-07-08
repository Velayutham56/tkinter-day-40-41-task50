import tkinter as tk

def highlight_keywords():
    text_widget.tag_remove("highlight", "1.0", tk.END)  # Clear previous highlights
    keywords = ["Python", "Tkinter", "widget"]
    content = text_widget.get("1.0", tk.END)

    for keyword in keywords:
        start_index = "1.0"
        while True:
            start_index = text_widget.search(keyword, start_index, stopindex=tk.END)
            if not start_index:
                break
            end_index = f"{start_index}+{len(keyword)}c"
            text_widget.tag_add("highlight", start_index, end_index)
            start_index = end_index

    text_widget.tag_config("highlight", background="yellow", foreground="black")

root = tk.Tk()
root.title("Keyword Highlighter")

text_widget = tk.Text(root, wrap="word", width=50, height=15)
text_widget.pack(padx=10, pady=(10,0))

text_widget.insert("1.0", "Python is great for GUI development with Tkinter. This widget is a Text widget.")

highlight_button = tk.Button(root, text="Highlight Keywords", command=highlight_keywords)
highlight_button.pack(pady=(5,10))

root.mainloop()
