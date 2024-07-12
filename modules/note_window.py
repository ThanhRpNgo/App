from tklib import *
from parameter import *


class Note_Window():
    def __init__(self, note_button):
        self.note_button = note_button
        self.note_window = My_Toplevel()
        self.note_window.title(TITLE_NOTE_WINDOW)
        self.note_window.geometry(GEOMETRY_NOTE_WINDOW)
        self.create_note()
        self.turn_off_window()

    def create_note(self):
        my_note = My_Label(
            master=self.note_window,
            font=FONT_DOCUMENT,
            text=TEXT_TITILE_NOTED
        )
        my_note.grid(row=0, column=0)

    def turn_off_window(self):
        self.note_window.protocol(
            'WM_DELETE_WINDOW',
            func=lambda: (
                self.note_button.config(state='normal'),
                self.note_window.destroy()
            )
        )
