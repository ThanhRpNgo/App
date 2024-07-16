from tklib import *
from parameter import *
from MCQs.system import MCQs_system


class Window_Second():
    def __init__(self):
        self.window_second = Window(
            height=WIDTH_WINDOW_FIRST,
            width=HEIGHT_WINDOW_FIRST,
            title=TITLE_SOFTWARE,
        )
        self.frame_r0_c0 = self.window_second.add_frame(row=0, column=0)
        self.frame_r0_c0.config(padx=15, pady=40)
        self.frame_r1_c0 = self.window_second.add_frame(row=1, column=0)
        self.frame_r2_c0 = self.window_second.add_frame(row=2, column=0)
        self.add_label_title()
        self.add_label_select(text=TEXT_INPUT_TEACHER, row=0)
        self.add_label_select(text=TEXT_INPUT_STUDENT, row=3)
        self.path_folder_teacher = tk.StringVar()
        self.path_folder_student = tk.StringVar()
        self.add_button_select(
            row=2, command=lambda: self.add_label_verify(
                row=1, var=self.path_folder_teacher))
        self.add_button_select(
            row=5, command=lambda: self.add_label_verify(
                row=4, var=self.path_folder_student))
        self.add_button_accept()
        self.window_second.run()

    def add_label_title(self):
        global printer
        printer = tk.PhotoImage(file=PATH_IMG_PRINTER).subsample(5, 5)

        label_title = My_Label(
            master=self.frame_r0_c0,
            image=printer,
            text=" " + TITLE_SOFTWARE,
            font=font_style()[4],
            compound='left',
            width=WIDTH_WINDOW_FIRST,
        )
        label_title.grid(row=0, column=0, sticky="w")

    def add_label_select(self, text, row):
        label_select = My_Label(
            master=self.frame_r1_c0,
            font=font_style()[5],
            text=text
        )
        label_select.grid(row=row, column=0, sticky='w', padx=100)

    def add_button_select(self, row, command):
        button_select = My_TButton(
            master=self.frame_r1_c0,
            text=TEXT_SELECT_FOLDER,
            style=style_gray(),
            command=command
        )
        button_select.grid(row=row, column=0, sticky='w', padx=100, pady=10)

    def add_label_verify(self, row, var):
        if not hasattr(self, 'label'):
            label_verify = My_Label(
                master=self.frame_r1_c0,
                text='Chưa có thư mục được chọn!',
                font=font_style()[6]
            )
            label_verify.grid(row=row, column=0, sticky='w', padx=100)
        folder_selected = filedialog.askdirectory()
        var.set(folder_selected)
        if folder_selected:
            label_verify.config(text=f"Thư Mục Đã chọn: {folder_selected}")

    def add_button_accept(self):
        button_accept = My_TButton(
            master=self.frame_r2_c0,
            style=style_gray(),
            text=TEXT_ACCEPT,
            command=lambda: MCQs_system(
                self.path_folder_teacher.get(),
                self.path_folder_student.get()))
        button_accept.grid(row=0, column=0, sticky="w", padx=250, pady=20)
