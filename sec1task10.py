import tkinter as tk


root = tk.Tk()
root.title("Sidebar and Main Content Layout")
root.geometry("500x300")


sidebar = tk.Frame(root, bg="lightgray", width=120)
sidebar.pack(side="left", fill="y")


tk.Label(sidebar, text="Menu", bg="lightgray", font=("Arial", 12, "bold")).pack(pady=10)
tk.Button(sidebar, text="Home").pack(pady=5, fill="x", padx=10)
tk.Button(sidebar, text="Profile").pack(pady=5, fill="x", padx=10)
tk.Button(sidebar, text="Settings").pack(pady=5, fill="x", padx=10)


main_content = tk.Frame(root, bg="white")
main_content.pack(fill="both", expand=True)


tk.Label(main_content, text="Welcome to the main content area!", bg="white", font=("Arial", 14)).pack(pady=20)

root.mainloop()
