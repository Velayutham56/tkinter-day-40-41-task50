import tkinter as tk

# Create main window
root = tk.Tk()
root.title("Label Alignment Example")

# Right-aligned label using sticky='E'
label = tk.Label(root, text="Right-Aligned Label:")
label.grid(row=0, column=0, padx=10, pady=10, sticky='E')

# Entry field beside the label
entry = tk.Entry(root)
entry.grid(row=0, column=1, padx=10, pady=10)

root.mainloop()
