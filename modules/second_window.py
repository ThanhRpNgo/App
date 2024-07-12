from tklib import *
from parameter import *
from tkinter import filedialog


class Second_Window():
    def __init__(self):
        self.second_window = Window(
            root=tk.Tk(),
            title=TITLE_SOFTWARE,
            geometry=GEOMETRY_FIRST_WINDOW
        )
        self.frame_r0_c0 = self.second_window.create_frame(row=0, column=0)
        self.frame_r0_c0.config(padx=15, pady=15)
        self.frame_r1_c0 = self.second_window.create_frame(row=1, column=0)
        self.frame_r2_c0 = self.second_window.create_frame(row=2, column=0)
        self.frame_r3_c0 = self.second_window.create_frame(row=3, column=0)
        self.create_info_frame()
        self.create_option_menu_1()
        self.create_option_menu_2()
        self.accept_button()
        self.button_select_student_ans()
        self.button_select_teacher_ans()

    def create_info_frame(self):
        global printer
        printer = tk.PhotoImage(file=PATH_IMG_PRINTER).subsample(3, 3)
        FONT_SOFTWARE_NAME_SECOND = tkFont.Font(
            family="Arial",
            size=26,
            weight="bold"
        )
        frame_title = My_Label(
            master=self.frame_r0_c0,
            text=TITLE_SOFTWARE,
            font=FONT_SOFTWARE_NAME_SECOND,
        )
        frame_title.config(text=TITLE_SOFTWARE, image=printer, compound='left')
        frame_title.grid(row=0, column=0, sticky="ew")

    def button_select_teacher_ans(self):
        style = ttk.Style()
        style.theme_use('clam')
        style.configure(
            'My.TButton',
            background='',
            relief='flat',
            font=FONT_NOTE,
        )
        style.map('My.TButton', background=[('active', 'lightgray')])
        button_select = My_TButton(
            master=self.frame_r1_c0,
            text='Chọn Thư Mục',
            style='My.TButton',
            command=self.create_label_and_select_folder_teacher
        )
        button_select.grid(row=1, column=0, sticky='w', padx=100)

    def button_select_student_ans(self):
        style = ttk.Style()
        style.theme_use('clam')
        style.configure(
            'My.TButton',
            background='',
            relief='flat',
            font=FONT_NOTE,
        )
        button_select = My_TButton(
            master=self.frame_r1_c0,
            text='Chọn Thư Mục',
            style='My.TButton',
            command=self.create_label_and_select_folder_student
        )
        button_select.grid(row=1, column=1, sticky='w', padx=450)

    def create_option_menu_1(self):
        label = My_Label(
            master=self.frame_r2_c0,
            text=TEXT_INPUT_TEACHER
        )
        values = list(map(str, range(1, 51)))
        default_value = "1"
        optionMenu = My_Combobox(
            self.frame_r2_c0,
            values=values,
        )
        optionMenu.set(default_value)
        label.grid(row=0, column=0, sticky='w', padx=100)
        optionMenu.grid(row=1, column=0, sticky='w', padx=100)

    def create_option_menu_2(self):
        label = My_Label(
            master=self.frame_r2_c0,
            text=TEXT_INPUT_STUDENT
        )
        values = list(map(str, range(1, 51)))
        default_value = "1"
        optionMenu = My_Combobox(
            self.frame_r2_c0,
            values=values,
        )
        optionMenu.set(default_value)
        label.grid(row=0, column=1, sticky='w', padx=300)
        optionMenu.grid(row=1, column=1, sticky='w', padx=300)

    def accept_button(self):
        style = ttk.Style()
        style.theme_use('clam')
        style.configure(
            'My.TButton',
            background='',
            relief='flat',
            font=FONT_NOTE,
        )
        style.map('My.TButton', background=[('active', 'lightgray')])
        accept_button = My_TButton(
            master=self.frame_r3_c0,
            style='My.TButton',
            text=TEXT_ACCEPT
        )
        accept_button.grid(row=0, column=0, sticky="w", padx=400, pady=20)

    def create_label_and_select_folder_student(self):
        if not hasattr(self, 'label'):
            label = My_Label(
                master=self.frame_r1_c0,
                text='Chưa có thư mục được chọn!'
            )
            label.grid(row=0, column=1, sticky='w', padx=450)
        folder_selected = filedialog.askdirectory()
        if folder_selected:
            label.config(text=f"Thư Mục Đã chọn: {folder_selected}")

    def create_label_and_select_folder_teacher(self):
        if not hasattr(self, 'label'):
            label = My_Label(
                master=self.frame_r1_c0,
                text='Chưa có thư mục được chọn!'
            )
            label.grid(row=0, column=0, sticky='w',padx=100)
        folder_selected = filedialog.askdirectory()
        if folder_selected:
            label.config(text=f"Thư Mục Đã chọn: {folder_selected}")
