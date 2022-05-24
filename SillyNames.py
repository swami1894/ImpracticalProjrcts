import tkinter as tk
import random

WIDTH = 500
HEIGHT = 300

root = tk.Tk()
root.title("Silly Name Generator")

SCREEN_WIDTH = root.winfo_screenwidth()
SCREEN_HEIGHT = root.winfo_screenheight()

center_x = int(SCREEN_WIDTH/2 - WIDTH/2)
center_y = int(SCREEN_HEIGHT/2 - HEIGHT/2)

root.geometry(f'{WIDTH}x{HEIGHT}+{center_x}+{center_y}')

message = tk.Label(root, text="Find your Silly Persona")
message.pack()

root.mainloop()
