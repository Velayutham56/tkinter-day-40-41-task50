import tkinter as tk

def is_numeric_input(P):
    return P.isdigit()

root = tk.Tk()
vcmd = (root.register(is_numeric_input), '%P')
entry = tk.Entry(root, validate='key', validatecommand=vcmd)
entry.pack()
root.mainloop()
