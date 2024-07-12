from tklib import *
from parameter import *
from modules.note_window import Note_Window
from modules.second_window import Second_Window


class First_Window():
    def __init__(self, root):
        self.first_window = Window(
            root=root,
            title=TITLE_SOFTWARE,
            geometry=GEOMETRY_FIRST_WINDOW
        )
        self.images = self.load_images()
        self.greeting_info = self.get_current_time()
        self.frame_r0_c0 = self.first_window.create_frame(row=0, column=0)
        self.frame_r0_c0.config(padx=15, pady=15)
        self.frame_r1_c0 = self.first_window.create_frame(row=1, column=0)
        self.frame_r2_c0 = self.first_window.create_frame(row=2, column=0)
        self.create_sun_moon()
        self.create_greeting()
        self.note_button = self.create_note_button()
        self.transfer_second_window = self.create_transfer_button()
        self.create_software_name()
        self.first_window.run()

    def load_images(self):
        morning = tk.PhotoImage(file=PATH_IMG_MORNING).subsample(10, 10)
        afternoon = tk.PhotoImage(file=PATH_IMG_AFTERNOON).subsample(10, 10)
        evening = tk.PhotoImage(file=PATH_IMG_EVENING).subsample(10, 10)

        global images
        images = [morning, afternoon, evening]
        return images

    def get_current_time(self):
        current_time = datetime.datetime.now().time()

        if TIME_MORNING_START <= current_time < TIME_MORNING_END:
            greeting_text = " " + TEXT_MORNING
            greeting_image = self.images[0]
        elif TIME_AFTERNOON_START <= current_time < TIME_AFTERNOON_END:
            greeting_text = " " + TEXT_AFTERNOON
            greeting_image = self.images[1]
        else:
            greeting_text = " " + TEXT_EVENING
            greeting_image = self.images[2]

        greeting_info = [greeting_text, greeting_image]
        return greeting_info

    def create_sun_moon(self):
        sun_moon = My_Label(
            master=self.frame_r0_c0,
            image=self.greeting_info[1])
        sun_moon.grid(row=0, column=0, sticky="w")

    def create_greeting(self):
        greeting = My_Text(
            master=self.frame_r0_c0,
            width=35,
            height=1,
            font=FONT_TEXT_GREETING
        )
        greeting.insert('1.0', self.greeting_info[0])
        greeting.config(state=tk.DISABLED)
        greeting.grid(row=0, column=1, sticky="w")

    def create_note_button(self):
        note_button = My_TButton(
            master=self.frame_r0_c0,
            text=TEXT_NOTE,
            command=lambda: self.open_note_window()
        )
        note_button.grid(row=0, column=2, padx=500)
        return note_button

    def open_note_window(self):
        Note_Window(self.note_button)
        self.note_button.config(state='disabled')

    def create_software_name(self):
        greeting = My_Label(
            master=self.frame_r1_c0,
            text=TITLE_SOFTWARE,
            font=FONT_SOFTWARE_NAME,
            width=calculate_chars_per_line(
                WIDTH_FIRST_WINDOW,
                FONT_SOFTWARE_NAME),
            height=2)
        greeting.grid(row=0, column=0, sticky="w")

    def create_transfer_button(self):
        global printer
        printer = tk.PhotoImage(file=PATH_IMG_PRINTER).subsample(1, 1)
        trans_button = My_Button(
            master=self.frame_r2_c0,
            image=printer,
            command=lambda: self.open_second_window()
        )
        trans_button.grid(row=0, column=0, sticky="w", padx=400, pady=20)
        return trans_button

    def open_second_window(self):
        self.first_window.root.destroy()
        Second_Window()
