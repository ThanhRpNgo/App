from tklib import *
from parameter import *


class Window_Waiting():
    def __init__(
            self,
            button_accept,
            width=WIDTH_WINDOW_NOTE,
            height=HEIGHT_WINDOW_NOTE):
        self.button_accept = button_accept
        self.window_watiting = My_Toplevel(height=height,width=width)
        self.window_watiting.title(TITLE_WINDOW_WAITING)
        self.close_window()

    def create_label(self, row, message: str):
        label = My_Label(
            self.window_watiting,
            text=message,
            font=("Arial", 16)
        )

        label.grid(row=row, column=0, sticky='w', padx=10, pady=10)
        self.window_watiting.update()
    
    def close_window(self):
        self.window_watiting.protocol(
            'WM_DELETE_WINDOW',
            func=lambda: (
                self.button_accept.config(state='normal'),
                self.window_watiting.destroy()
            )
        )
