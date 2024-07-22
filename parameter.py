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
TITLE_WINDOW_NOTE = "Lưu ý"
TITLE_WINDOW_WAITING = "Hệ thống đang xử lý..."
TITLE_MESSAGEBOX_WARNING = "Cảnh báo!"

TEXT_MORNING = "Chào buổi sáng!"
TEXT_AFTERNOON = "Chào buổi chiều!"
TEXT_EVENING = "Buổi tối vui vẻ!"
TEXT_NOTE = "Lưu ý!"
TEXT_TITILE_NOTED = "Mọi Người Lưu ý khi sử dụng"
TEXT_ACCEPT = "CHẤP NHẬN"
TEXT_INPUT_TEACHER = "CHỌN FOLDER ANSWER-SHEET CỦA GIÁO VIÊN"
TEXT_INPUT_STUDENT = "CHỌN FOLDER ANSWER-SHEET CỦA SINH VIÊN"
TEXT_SELECT_FOLDER = "CHỌN THƯ MỤC"
TEXT_WARNING_CASE_1 = "Chưa chọn folder giáo viên và sinh viên!"
TEXT_WARNING_CASE_2 = "Chưa chọn folder giáo viên!"
TEXT_WARNING_CASE_3 = "Chưa chọn folder sinh viên!"
TEXT_WAITING_1 = "Đang xử lý bài giáo viên..."
TEXT_WAITING_2 = "Đang xử lý bài học sinh..."
TEXT_WAITING_3 = "Đang lưu..."
TEXT_WAITING_4 = "Đã xong!"

WIDTH_WINDOW_FIRST = 1280
WIDTH_WINDOW_NOTE = 500
HEIGHT_WINDOW_FIRST = 720
HEIGHT_WINDOW_NOTE = 300
GEOMETRY_WINDOW_FIRST = (WIDTH_WINDOW_FIRST, HEIGHT_WINDOW_FIRST)
GEOMETRY_WINDOW_NOTE = (WIDTH_WINDOW_NOTE, HEIGHT_WINDOW_NOTE)
THE_WINDOW_SECOND = f"{WIDTH_WINDOW_FIRST}x{WIDTH_WINDOW_NOTE}"
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


def my_style():
    style = ttk.Style()
    style.configure(
        'TButton',
        background='white',
        font=font_style()[2],
    )


def style_gray():
    style = ttk.Style()
    style.theme_use('clam')
    style.configure(
        'My.TButton',
        background='',
        relief='flat',
        font=font_style()[2],
    )
    style.map('My.TButton', background=[('active', 'lightgray')])


def font_style():
    FONT_SOFTWARE_NAME = tkFont.Font(
        family="Time New Roman",
        size=24,
        slant="italic",
        weight="bold")
    FONT_TEXT_GREETING = tkFont.Font(
        family="Time New Roman",
        size=16,
        slant="italic"
    )
    FONT_NOTE = tkFont.Font(
        family="Arial",
        size=14,
        slant="roman"
    )
    FONT_DOCUMENT = tkFont.Font(
        family="Time New Roman",
        size=30
    )
    FONT_SOFTWARE_NAME_SECOND = tkFont.Font(
        family="Arial",
        size=26,
        weight="bold"
    )
    FONT_INFO_FOLDER = tkFont.Font(
        family="Arial",
        size=12,
        slant='italic',
        weight="bold"
    )
    FONT_SELECT_FOLDER = tkFont.Font(
        family="Arial",
        size=12,
        slant='italic'
    )
    font = [
        FONT_SOFTWARE_NAME,
        FONT_TEXT_GREETING,
        FONT_NOTE,
        FONT_DOCUMENT,
        FONT_SOFTWARE_NAME_SECOND,
        FONT_INFO_FOLDER,
        FONT_SELECT_FOLDER]
    return font
