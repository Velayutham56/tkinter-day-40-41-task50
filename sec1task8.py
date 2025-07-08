import tkinter as tk

# Create main window
root = tk.Tk()
root.title("User Information Form")

# Full Name
tk.Label(root, text="Full Name:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
full_name_entry = tk.Entry(root)
full_name_entry.grid(row=0, column=1, padx=10, pady=5)

# Email
tk.Label(root, text="Email:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
email_entry = tk.Entry(root)
email_entry.grid(row=1, column=1, padx=10, pady=5)

# Phone Number
tk.Label(root, text="Phone:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
phone_entry = tk.Entry(root)
phone_entry.grid(row=2, column=1, padx=10, pady=5)

# Submit Button
submit_button = tk.Button(root, text="Submit")
submit_button.grid(row=3, columnspan=2, pady=10)

root.mainloop()
