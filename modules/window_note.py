from tklib import *
from parameter import *


class Window_Note():
    def __init__(self, button_note):
        self.button_note = button_note
        self.window_note = My_Toplevel()
        self.window_note.title(TITLE_WINDOW_NOTE)
        self.window_note.geometry(GEOMETRY_WINDOW_NOTE)
        self.add_label_note()
        self.close_window()

    def add_label_note(self):
        note = My_Label(
            master=self.window_note,
            font=FONT_DOCUMENT,
            text=TEXT_TITILE_NOTED
        )
        note.grid(row=0, column=0)

    def close_window(self):
        self.window_note.protocol(
            'WM_DELETE_WINDOW',
            func=lambda: (
                self.button_note.config(state='normal'),
                self.window_note.destroy()
            )
        )
