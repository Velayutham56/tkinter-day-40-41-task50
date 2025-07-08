import tkinter as tk

# Create main window
root = tk.Tk()
root.title("Label Placement Example")
root.geometry("300x200")  # Set window size

# Label at fixed coordinates (50, 50)
label_fixed = tk.Label(root, text="Fixed at (50, 50)", bg="lightblue")
label_fixed.place(x=50, y=50)

# Label at center using relx and rely
label_centered = tk.Label(root, text="Centered", bg="lightgreen")
label_centered.place(relx=0.5, rely=0.5, anchor="center")

root.mainloop()
