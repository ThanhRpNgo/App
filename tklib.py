import tkinter as tk
from tkinter import ttk
from parameter import *
from tkinter import filedialog


class Window():
    def __init__(self, title, geometry):
        self.root = tk.Tk()
        self.root.title(title)
        self.root.geometry(geometry)
        self.root.configure(bg=COLOR_BACKGROUND)
        self.root.iconbitmap(PATH_ICON)
        my_style()

    def run(self):
        self.root.mainloop()

    def add_frame(self, row, column):
        frame = My_Frame(
            master=self.root
        )
        frame.grid(row=row, column=column, sticky="w")
        return frame


class My_Frame(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self['bg'] = COLOR_BACKGROUND


class My_Label(tk.Label):
    def __init__(self, *args, **kwargs):
        tk.Label.__init__(self, *args, **kwargs)
        self['bg'] = COLOR_BACKGROUND
        self['relief'] = tk.FLAT


class My_Text(tk.Text):
    def __init__(self, *args, **kwargs):
        tk.Text.__init__(self, *args, **kwargs)
        self['bg'] = COLOR_BACKGROUND
        self['relief'] = tk.FLAT


class My_Toplevel(tk.Toplevel):
    def __init__(self, *args, **kwargs):
        tk.Toplevel.__init__(self, *args, **kwargs)
        self['bg'] = COLOR_BACKGROUND


class My_Button(tk.Button):
    def __init__(self, *args, **kwargs):
        tk.Button.__init__(self, *args, **kwargs)
        self['bg'] = COLOR_BACKGROUND
        self['relief'] = tk.FLAT
        self['cursor'] = "mouse"


class My_TButton(ttk.Button):
    def __init__(self, *args, **kwargs):
        ttk.Button.__init__(self, *args, **kwargs)
        self['style'] = "TButton"


# class My_Invar(tk.IntVar):
#     def __init__(self, *arg, **kwargs):
#         super().__init__(self, *arg, **kwargs)


# class My_OptionMenu(ttk.OptionMenu):
#     def __init__(self, master, default, values, command=None, **kwargs):
#         self.var = tk.StringVar(master, default)
#         super().__init__(master, self.var, *values, command=command, **kwargs)


# class My_Combobox(ttk.Combobox):
#     def __init__(self, master=None, values=[], **kw):
#         self.var = tk.StringVar(master)
#         super().__init__(master, values=values, **kw)
#         self.width = 8
#         self.values = values
#         self.configure(values=self.values)
#         self.bind("<KeyRelease>", self.check_value)

#     def check_value(self, event):
#         current_value = self.get()
#         if current_value not in self.values:
#             self.set(self.values[0])
