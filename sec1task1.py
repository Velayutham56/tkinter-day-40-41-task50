import tkinter as tk


root = tk.Tk()
root.title("Stacked Labels")


label1 = tk.Label(root, text="Label One", bg="lightblue", font=("Arial", 12))
label1.pack(pady=5)


label2 = tk.Label(root, text="Label Two", bg="lightgreen", font=("Arial", 12))
label2.pack(pady=5)


label3 = tk.Label(root, text="Label Three", bg="lightyellow", font=("Arial", 12))
label3.pack(pady=5)

root.mainloop()
