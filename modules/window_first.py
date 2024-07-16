from tklib import *
from parameter import *
import tkinter.font as tkFont
from modules.window_note import Window_Note
from modules.window_second import Window_Second


class Window_First():
    def __init__(self):
        self.window_first = Window(
            height=WIDTH_WINDOW_FIRST,
            width=HEIGHT_WINDOW_FIRST,
            title=TITLE_SOFTWARE
        )
        self.frame_r0_c0 = self.window_first.add_frame(row=0, column=0)
        self.frame_r0_c0.config(padx=15, pady=15)
        self.frame_r1_c0 = self.window_first.add_frame(row=1, column=0)
        self.frame_r2_c0 = self.window_first.add_frame(row=2, column=0)
        self.add_label_greeting()
        self.button_note = self.add_button_note()
        self.add_label_name()
        self.button_transfer = self.add_button_transfer()
        self.window_first.run()

    def add_label_greeting(self):
        label_greeting = My_Label(
            master=self.frame_r0_c0,
            font=font_style()[1],
            compound='left'
        )

        global morning, afternoon, evening
        morning = tk.PhotoImage(file=PATH_IMG_MORNING).subsample(10, 10)
        afternoon = tk.PhotoImage(file=PATH_IMG_AFTERNOON).subsample(10, 10)
        evening = tk.PhotoImage(file=PATH_IMG_EVENING).subsample(10, 10)

        current_time = datetime.datetime.now().time()
        if TIME_MORNING_START <= current_time < TIME_MORNING_END:
            label_greeting.config(
                 image=morning,
                 text=" " + TEXT_MORNING
            )
        elif TIME_AFTERNOON_START <= current_time < TIME_AFTERNOON_END:
            label_greeting.config(
                 image=afternoon,
                 text=" " + TEXT_AFTERNOON
            )
        else:
            label_greeting.config(
                 image=evening,
                 text=" " + TEXT_EVENING
            )

        label_greeting.grid(row=0, column=0)

    def add_button_note(self):
        button_note = My_TButton(
            master=self.frame_r0_c0,
            text=TEXT_NOTE,
            style=my_style(),
            command=lambda: self.open_window_note()
        )
        button_note.grid(row=0, column=1, padx=850)
        return button_note

    def open_window_note(self):
        Window_Note(self.button_note)
        self.button_note.config(state='disabled')

    def add_label_name(self):
        name = My_Label(
            master=self.frame_r1_c0,
            text=TITLE_SOFTWARE,
            font=font_style()[0],
            width=calculate_chars_per_line(
                WIDTH_WINDOW_FIRST,
                font_style()[0]),
            height=2)
        name.grid(row=0, column=0, sticky="w")

    def add_button_transfer(self):
        global printer
        printer = tk.PhotoImage(file=PATH_IMG_PRINTER).subsample(1, 1)

        button_transfer = My_Button(
            master=self.frame_r2_c0,
            image=printer,
            command=lambda: self.open_window_second()
        )
        button_transfer.grid(row=0, column=0, sticky="w", padx=400, pady=20)
        return button_transfer

    def open_window_second(self):
        self.window_first.root.destroy()
        Window_Second()
