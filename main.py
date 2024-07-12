from ctypes import windll
from modules.window_first import Window_First


windll.shcore.SetProcessDpiAwareness(1)
Window_First()
