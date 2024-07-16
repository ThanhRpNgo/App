
import pandas as pd
import re
## Load the workbook#
#

#def excel_student(data_ID, data_enrollment, Data_answerSheet,total_answer,correct_answer):
#    workbook = Workbook()
#    workbook['Sheet'].title = 'Data_Of_Student'
#    
#    # Select the active worksheet
#    sheet2 = workbook.active
#    
#    # Merge cells and assign values
#    for i in range(1, 100):
#        sheet2.merge_cells(start_row=i, start_column=1, end_row=i, end_column=2)
#        sheet2.merge_cells(start_row=i, start_column=3, end_row=i, end_column=4)
#        sheet2.merge_cells(start_row=i, start_column=5, end_row=i, end_column=10)
#        sheet2.merge_cells(start_row=i, start_column=11, end_row=i, end_column = 12)
#        sheet2.merge_cells(start_row=i, start_column=13, end_row=i, end_column = 14)#

#    concatenated_value_ID = ''.join(map(str, data_ID))
#    concatenated_value_enrollment = ''.join(map(str, data_enrollment))#

#    # Set the concatenated value to cell A2
#    sheet2['A2'].value = concatenated_value_ID
#    sheet2['C2'].value = concatenated_value_enrollment
#    sheet2['K2'].value = total_answer
#    sheet2['M2'].value = correct_answer
#    
#    for i, value in enumerate(Data_answerSheet, start=2):
#        sheet2[f'E{i}'].value = value
#    
#    # Apply font
#    for row in sheet2.iter_rows():
#        for cell in row:
#            cell.font = Font(name='Times New Roman')
#    
#    # Assigning values and applying formatting to header cells
#    sheet2['A1'].value = 'Ma So Sinh vien'
#    sheet2['A1'].fill = PatternFill("solid", fgColor="33FFC4")
#    sheet2['C1'].value = 'Ma De'
#    sheet2['C1'].fill = PatternFill("solid", fgColor="33FFE0")
#    sheet2['E1'].value = 'Dap An cua sinh vien'
#    sheet2['E1'].fill = PatternFill("solid", fgColor="33ECFF")
#    sheet2['K1'].value = 'Tong so cau'
#    sheet2['K1'].fill = PatternFill("solid", fgColor="2FAFD8")
#    sheet2['M1'].value = 'Tong so cau dung'
#    sheet2['M1'].fill = PatternFill("solid", fgColor="2FAFD8")
#    
#    
#    # Save the workbook#



#def excel_teacher(data_enrollment, Data_answerSheet,total_answer):
#    workbook = Workbook()
#    workbook['Sheet'].title = 'Data_Of_Teacher'
#    
#    # Select the active worksheet
#    sheet2 = workbook.active
#    
#    # Merge cells and assign values
#    for i in range(1, 100):
#        sheet2.merge_cells(start_row=i, start_column=1, end_row=i, end_column=2)
#        sheet2.merge_cells(start_row=i, start_column=3, end_row=i, end_column=8)
#        sheet2.merge_cells(start_row=i, start_column=9, end_row=i, end_column=10)#

#    concatenated_value_enrollment = ''.join(map(str, data_enrollment))#
#

#    # Set the concatenated value to cell A2#

#    sheet2['A2'].value = concatenated_value_enrollment
#    sheet2['I2'].value = total_answer
#    
#    for i, value in enumerate(Data_answerSheet, start=2):
#        sheet2[f'C{i}'].value = value
#    
#    # Apply font
#    for row in sheet2.iter_rows():
#        for cell in row:
#            cell.font = Font(name='Times New Roman')
#    
#    # Assigning values and applying formatting to header cells
#    sheet2['A1'].value = 'Ma De'
#    sheet2['A1'].fill = PatternFill("solid", fgColor="33FFE0")
#    sheet2['C1'].value = 'Dap An cua giao vien'
#    sheet2['C1'].fill = PatternFill("solid", fgColor="33ECFF")
#    sheet2['I1'].value = 'Tong so cau'
#    sheet2['I1'].fill = PatternFill("solid", fgColor="2FAFD8")
#    
#    


def save_to_excel_student(data_ID, data_enrollment, Data_answerSheet, correct_answer,grading):
   
    # Khai báo dữ liệu từ hàm excel_student
    columns = {f"cau {i+1}": [ans] for i, ans in enumerate(Data_answerSheet)}  # Use formatted answers
    data_student = {
            "Ma So Sinh vien": [data_ID],
            "Ma De": [data_enrollment],
            **columns,  # Sử dụng unpacking để thêm các cột từ danh sách vào từ điển dữ liệu sinh viên
            "Tong so cau dung": [correct_answer],
            "Diem (%)": [f"{grading}%"]
        }   

        # Tạo DataFrame từ dữ liệu
    df_student = pd.DataFrame(data_student)

    # Thêm màu xanh cho hàng đầu tiên

    return df_student

def save_to_excel_teacher(data_enrollment, Data_answerSheet, total_answer):
    # Khai báo dữ liệu từ hàm excel_teacher
    columns = {f"cau {i+1}": [ans] for i, ans in enumerate(Data_answerSheet)}
    data_teacher = {
        "Ma De": [data_enrollment],
        **columns,
        "Tong so cau": [total_answer]
    }

    # Tạo DataFrame từ dữ liệu
    df_teacher = pd.DataFrame(data_teacher)
    # Thêm màu xanh cho hàng đầu tiên

    return df_teacher


# Sử dụng hàm để lưu dữ liệu vào file Excel
if __name__ == '__main__':
    # Gọi hàm lưu dữ liệu sinh viên
    save_to_excel_student()
    # Gọi hàm lưu dữ liệu giáo viên
    save_to_excel_teacher()