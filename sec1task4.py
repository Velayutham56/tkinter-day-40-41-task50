import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("3x3 Button Matrix")

# Define button labels (like a calculator)
buttons = [
    "1", "2", "3",
    "4", "5", "6",
    "7", "8", "9"
]

# Create and place buttons in a 3x3 grid
for i in range(3):         # row index
    for j in range(3):     # column index
        btn_text = buttons[i * 3 + j]
        button = tk.Button(root, text=btn_text, width=10, height=3)
        button.grid(row=i, column=j, padx=5, pady=5)

root.mainloop()
