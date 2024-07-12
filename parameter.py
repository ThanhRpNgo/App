import os
import datetime
import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont


def center_screen(width, height):
    temp_window = tk.Tk()
    screen_width = temp_window.winfo_screenwidth()
    screen_height = temp_window.winfo_screenheight()
    temp_window.destroy()

    x_coordinate = (screen_width / 2) - (width / 2)
    y_coordinate = (screen_height / 2) - (height / 2 + 20)
    return f"{width}x{height}+{int(x_coordinate)}+{int(y_coordinate)}"


def calculate_chars_per_line(window_width, font):
    sample_text = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    total_width = sum(font.measure(char) for char in sample_text)
    average_char_width = total_width / len(sample_text)
    chars_per_line = int(window_width // average_char_width) - 1
    return chars_per_line


TITLE_SOFTWARE = "Ứng dụng chấm điểm thi trắc nghiệm"
TITLE_NOTE_WINDOW = "Lưu ý"

TEXT_MORNING = "Chào buổi sáng!"
TEXT_AFTERNOON = "Chào buổi chiều!"
TEXT_EVENING = "Buổi tối vui vẻ!"
TEXT_NOTE = "Lưu ý!"
TEXT_TITILE_NOTED = "Mọi Người Lưu ý khi sử dụng"
TEXT_ACCEPT = "CHẤP NHẬN"
TEXT_INPUT_TEACHER = "CHỌN SỐ LƯỢNG BÀI CỦA GIÁO VIÊN"
TEXT_INPUT_STUDENT = "CHỌN SỐ LƯỢNG BÀI CỦA SINH VIÊN"

WIDTH_FIRST_WINDOW = 1280
WIDTH_NOTE_WINDOW = 500
HEIGHT_FIRST_WINDOW = 720
HEIGHT_NOTE_WINDOW = 300
GEOMETRY_FIRST_WINDOW = center_screen(WIDTH_FIRST_WINDOW, HEIGHT_FIRST_WINDOW)
GEOMETRY_NOTE_WINDOW = center_screen(WIDTH_NOTE_WINDOW, HEIGHT_NOTE_WINDOW)
THE_WINDOW_SECOND = f"{WIDTH_FIRST_WINDOW}x{WIDTH_NOTE_WINDOW}"
COLOR_BACKGROUND = "light blue"

PATH_PROJET = os.getcwd()
PATH_FOLDER_IMG = PATH_PROJET + "\\img"
PATH_ICON = PATH_FOLDER_IMG + "\\grade.ico"
PATH_IMG_MORNING = PATH_FOLDER_IMG + "\\morning.png"
PATH_IMG_AFTERNOON = PATH_FOLDER_IMG + "\\afternoon.png"
PATH_IMG_EVENING = PATH_FOLDER_IMG + "\\evening.png"
PATH_IMG_PRINTER = PATH_FOLDER_IMG + "\\pngwing.com.png"

TIME_MORNING_START = datetime.time(5, 0)
TIME_MORNING_END = datetime.time(12, 0)
TIME_AFTERNOON_START = TIME_MORNING_END
TIME_AFTERNOON_END = datetime.time(18, 0)

FONT_TEXT_GREETING = tkFont.Font(
    family="Time New Roman",
    size=16,
    slant="italic")
FONT_NOTE = tkFont.Font(
    family="Arial",
    size=12,
    weight="bold")
FONT_DOCUMENT = tkFont.Font(
    family="Time New Roman",
    size=10)
FONT_SOFTWARE_NAME = tkFont.Font(
    family="Time New Roman",
    size=24,
    slant="italic",
    weight="bold")


# style = ttk.Style()
# style.configure(
#     'TButton',
#     background=COLOR_BACKGROUND,
#     font=FONT_NOTE,
# )
style = ttk.Style()
style.theme_use('clam') 
style.configure(
    'My.TButton',
    background='',
    relief='flat',
    font=FONT_NOTE,
)
style.map('My.TButton', background=[('active', 'lightgray')])