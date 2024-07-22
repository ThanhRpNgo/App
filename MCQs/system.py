import MCQs.OMR_checker as student
import MCQs.OMR_CheckTest as teacher
from MCQs.Src.check_code_and_answer import check_answers, compare_list_enrollment_answer
import numpy as np
from MCQs.Src.template_excel import save_to_excel_student, save_to_excel_teacher
import os
import pandas as pd
import time
import threading
from parameter import TEXT_WAITING_1, TEXT_WAITING_2, TEXT_WAITING_3, TEXT_WAITING_4


class MCQs_system():
    def __init__(
            self,
            path_folder_teacher,
            path_folder_student,
            window_waiting):
        self.window_waiting = window_waiting
        s = time.time()
        self.path_folder_teacher = path_folder_teacher
        self.path_folder_student = path_folder_student
        self.dfs_teacher = []
        self.dfs_student = []
        self.all_result_teacher = []
        self.run()
        self.save_to_excel()
        self.window_waiting.create_label(row=3, message=TEXT_WAITING_4)
        e = time.time()
        print("time : ", e - s)

    def run(self):
        files_teacher = os.listdir(self.path_folder_teacher)
        files_student = os.listdir(self.path_folder_student)

        self.window_waiting.create_label(row=0, message=TEXT_WAITING_1)
        threads_teacher = []
        for file_teacher in files_teacher:
            thread_teacher = threading.Thread(
                target=self.handle_file_teacher, args=(
                    file_teacher,))
            threads_teacher.append(thread_teacher)
            thread_teacher.start()

        for thread in threads_teacher:
            thread.join()

        self.window_waiting.create_label(row=1, message=TEXT_WAITING_2)
        threads_student = []
        for file_student in files_student:
            thread_student = threading.Thread(
                target=self.handle_file_student, args=(
                    file_student,))
            threads_student.append(thread_student)
            thread_student.start()

        for thread in threads_student:
            thread.join()

        self.window_waiting.create_label(row=2, message=TEXT_WAITING_3)
        if self.dfs_teacher:
            self.df_teacher = pd.concat(self.dfs_teacher, ignore_index=True)
            print(self.df_teacher)
        if self.dfs_student:
            self.df_student = pd.concat(self.dfs_student, ignore_index=True)
            print(self.df_student)

    def handle_file_teacher(self, file_teacher):
        file_path_teacher = os.path.join(
            self.path_folder_teacher, file_teacher)
        result_teacher = teacher.image_process_teacher(file_path_teacher)

        self.all_result_teacher.append(result_teacher)

        if result_teacher is not None:
            enrollment_teacher, answer_sheet_teacher, total_answer_teacher = result_teacher
            df_teacher_temp = save_to_excel_teacher(
                enrollment_teacher,
                answer_sheet_teacher,
                total_answer_teacher)
            self.dfs_teacher.append(df_teacher_temp)
        else:
            print(
                f"xử lý ảnh của giáo vien **{file_teacher}** vì có lỗi xảy ra trong quá trình xử lý ảnh")

    def handle_file_student(self, file_student):
        file_path_student = os.path.join(
            self.path_folder_student, file_student)
        result_student = student.img_process_student(file_path_student)

        if result_student is not None:
            ID_student, enrollment_student, answer_sheet_student = result_student

            for result_teacher in self.all_result_teacher:
                if result_teacher is not None:
                    enrollment_teacher, answer_sheet_teacher, total_answer_teacher = result_teacher

                    if np.array_equal(enrollment_student, enrollment_teacher):
                        correct_ans = compare_list_enrollment_answer(
                            answer_sheet_student, answer_sheet_teacher)
                        break
                    else:
                        correct_ans = '0'
            grading = check_answers(total_answer_teacher, correct_ans)
            df_student_temp = save_to_excel_student(
                ID_student, enrollment_student, answer_sheet_student, correct_ans, grading)
            self.dfs_student.append(df_student_temp)
        else:
            print(
                f"Xử lý ảnh của **{file_student}** gặp lỗi, cần được xử lý và chỉnh lại")

    def save_to_excel(self):
        with pd.ExcelWriter('output.xlsx') as writer:
            self.df_teacher.to_excel(
                writer,
                sheet_name='Data_Of_Teacher',
                index=False)
            # Write student data starting from the row after the last row of
            # teacher data
            self.df_student.to_excel(
                writer,
                sheet_name='Data_Of_Student',
                index=False)
            