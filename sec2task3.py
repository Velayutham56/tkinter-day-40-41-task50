import tkinter as tk


root = tk.Tk()
root.title("Mouse Click Label")

def change_text(event):
    label.config(text="you are cliked!")


label = tk.Label(root, text="clik me", font=("Arial", 16), fg="blue")
label.pack(pady=40)


label.bind("<Button-1>", change_text)

# Run the GUI loop
root.mainloop()
