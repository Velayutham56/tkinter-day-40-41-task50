import tkinter as tk


root = tk.Tk()
root.title("Keyboard Event Demo")


def key_pressed(event):
    print(f"you `{event.char}`  clicked")


root.bind("<Key>", key_pressed)


root.geometry("300x150")


root.mainloop()
