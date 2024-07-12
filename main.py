import tkinter as tk
from ctypes import windll


windll.shcore.SetProcessDpiAwareness(1)
root = tk.Tk()


from modules.first_window import First_Window
First_Window(root)
from modules.second_window import Second_Window
Second_Window()
