import tkinter as tk
from tkinter import filedialog
from tkinter import ttk  # Assuming you're using ttk for themed widgets

class MyApplication:
    def __init__(self, master):
        self.master = master
        self.master.title("Chọn Thư Mục Lưu Ảnh")

        # Create a frame to place widgets
        self.frame_r2_c0 = tk.Frame(self.master)
        self.frame_r2_c0.pack(padx=20, pady=20)

        # Create button to select folder
        self.button_select = ttk.Button(
            self.frame_r2_c0,
            text='Chọn Thư Mục',
            command=self.select_folder
        )
        self.button_select.grid(row=0, column=0, sticky='w')

        # Create label to display the selected folder path
        self.folder_label = ttk.Label(self.frame_r2_c0, text="No folder selected")
        self.folder_label.grid(row=1, column=0, sticky='w')

    def select_folder(self):
        folder_selected = filedialog.askdirectory()
        if folder_selected:
            print(f"Folder selected: {folder_selected}")
            self.folder_label.config(text=f"Folder selected: {folder_selected}")

# Main application
if __name__ == "__main__":
    root = tk.Tk()
    app = MyApplication(root)
    root.mainloop()
