import tkinter as tk

splash = tk.Tk()
splash.title("Splash Screen")


splash.overrideredirect(True)


splash_width = 300
splash_height = 150
screen_width = splash.winfo_screenwidth()
screen_height = splash.winfo_screenheight()
x = (screen_width // 2) - (splash_width // 2)
y = (screen_height // 2) - (splash_height // 2)
splash.geometry(f"{splash_width}x{splash_height}+{x}+{y}")


label = tk.Label(splash, text="Welcome to My App!", font=("Arial", 14), bg="lightblue")
label.pack(expand=True, fill="both")


splash.after(3000, splash.destroy)

splash.mainloop()
