from tklib import *
from parameter import *


class Window_Second():
    def __init__(self):
        self.window_second = Window(
            title=TITLE_SOFTWARE,
            geometry=GEOMETRY_WINDOW_FIRST
        )
        self.frame_r0_c0 = self.window_second.add_frame(row=0, column=0)
        self.frame_r0_c0.config(padx=15, pady=15)
        self.frame_r1_c0 = self.window_second.add_frame(row=1, column=0)
        self.frame_r2_c0 = self.window_second.add_frame(row=2, column=0)
        self.add_label_title()
        # self.accept_button()
        # self.button_select_student_ans()
        # self.button_select_teacher_ans()
        self.window_second.run()

    def add_label_title(self):
        global printer
        printer = tk.PhotoImage(file=PATH_IMG_PRINTER).subsample(5, 5)

        label_title = My_Label(
            master=self.frame_r0_c0,
            image=printer,
            text=" " + TITLE_SOFTWARE,
            font=FONT_SOFTWARE_NAME_SECOND,
            compound='left',
            width=WIDTH_WINDOW_FIRST,
        )
        label_title.grid(row=0, column=0, sticky="w")

    # def button_select_teacher_ans(self):
    #     style = ttk.Style()
    #     style.theme_use('clam')
    #     style.configure(
    #         'My.TButton',
    #         background='',
    #         relief='flat',
    #         font=FONT_NOTE,
    #     )
    #     style.map('My.TButton', background=[('active', 'lightgray')])
    #     button_select = My_TButton(
    #         master=self.frame_r1_c0,
    #         text='Chọn Thư Mục',
    #         style='My.TButton',
    #         command=self.create_label_and_select_folder_teacher
    #     )
    #     button_select.grid(row=1, column=0, sticky='w', padx=100)

    # def button_select_student_ans(self):
    #     style = ttk.Style()
    #     style.theme_use('clam')
    #     style.configure(
    #         'My.TButton',
    #         background='',
    #         relief='flat',
    #         font=FONT_NOTE,
    #     )
    #     button_select = My_TButton(
    #         master=self.frame_r1_c0,
    #         text='Chọn Thư Mục',
    #         style='My.TButton',
    #         command=self.create_label_and_select_folder_student
    #     )
    #     button_select.grid(row=1, column=1, sticky='w', padx=450)


    # def accept_button(self):
    #     style = ttk.Style()
    #     style.theme_use('clam')
    #     style.configure(
    #         'My.TButton',
    #         background='',
    #         relief='flat',
    #         font=FONT_NOTE,
    #     )
    #     style.map('My.TButton', background=[('active', 'lightgray')])
    #     accept_button = My_TButton(
    #         master=self.frame_r3_c0,
    #         style='My.TButton',
    #         text=TEXT_ACCEPT
    #     )
    #     accept_button.grid(row=0, column=0, sticky="w", padx=400, pady=20)

    # def create_label_and_select_folder_student(self):
    #     if not hasattr(self, 'label'):
    #         label = My_Label(
    #             master=self.frame_r1_c0,
    #             text='Chưa có thư mục được chọn!'
    #         )
    #         label.grid(row=0, column=1, sticky='w', padx=450)
    #     folder_selected = filedialog.askdirectory()
    #     if folder_selected:
    #         label.config(text=f"Thư Mục Đã chọn: {folder_selected}")

    # def create_label_and_select_folder_teacher(self):
    #     if not hasattr(self, 'label'):
    #         label = My_Label(
    #             master=self.frame_r1_c0,
    #             text='Chưa có thư mục được chọn!'
    #         )
    #         label.grid(row=0, column=0, sticky='w',padx=100)
    #     folder_selected = filedialog.askdirectory()
    #     if folder_selected:
    #         label.config(text=f"Thư Mục Đã chọn: {folder_selected}")
