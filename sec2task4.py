import tkinter as tk
import random

window = tk.Tk()
colors = ["red","green","blue","white","orange"]
def change_color():
    choicecolor =random.choice(colors)
    window.config(bg=choicecolor)

button = tk.Button(window,text="change window color",command=change_color)
button.pack(side="bottom")
window.mainloop()