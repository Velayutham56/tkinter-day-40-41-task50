import tkinter as tk


root = tk.Tk()
root.title("Click Button Example")


def say_hello():
    print("the button was clicked")


button = tk.Button(root, text="Click Me!", command=say_hello, width=15, height=2)
button.pack(pady=20)


root.mainloop()
