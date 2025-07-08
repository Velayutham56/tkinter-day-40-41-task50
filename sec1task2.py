import tkinter as tk


root = tk.Tk()
root.title("Horizontal Button Layout")


btn1 = tk.Button(root, text="Button 1")
btn1.pack(side="left", padx=10, pady=10)


btn2 = tk.Button(root, text="Button 2")
btn2.pack(side="left", padx=10, pady=10)


btn3 = tk.Button(root, text="Button 3")
btn3.pack(side="left", padx=10, pady=10)

root.mainloop()
