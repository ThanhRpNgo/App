import tkinter as tk
from tkinter import messagebox

def show_warning():
    messagebox.showwarning("Cảnh báo", "Đây là thông báo cảnh báo!")

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Cửa sổ chính")

# Tạo nút để hiển thị cảnh báo
button = tk.Button(root, text="Hiển thị cảnh báo", command=show_warning)
button.pack(pady=20)

# Chạy vòng lặp chính
root.mainloop()
