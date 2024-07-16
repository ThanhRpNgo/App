import numpy as np
import string
def remove_special_characters(input_data):
    if isinstance(input_data, np.ndarray):  # Kiểm tra xem đầu vào có phải là mảng NumPy không
        input_string = ' '.join(str(item) for item in input_data)  # Chuyển đổi mảng NumPy thành chuỗi
    elif isinstance(input_data, str):  # Kiểm tra xem đầu vào có phải là chuỗi không
        input_string = input_data
    else:
        raise ValueError("Input data must be either a NumPy array or a string")
    
    # Tạo một chuỗi chứa tất cả các ký tự đặc biệt và dấu cách
    special_characters = string.punctuation + ' '
    # Loại bỏ các ký tự đặc biệt và dấu cách từ chuỗi đầu vào
    cleaned_string = ''.join(char for char in input_string if char not in special_characters)
    return cleaned_string


def check_answers(total_questions, correct_answers):
    num_correct = correct_answers
    total_questions = total_questions
    percentage_correct = (num_correct / total_questions) * 100
    return percentage_correct

def count_correct_answers(teacher_answers, student_answers):
    num_correct_answers = 0
    
    for teacher_answer, student_answer in zip(teacher_answers, student_answers):
        if teacher_answer == student_answer:
            num_correct_answers += 1
    
    return num_correct_answers


def flatten_list(nested_list):
    flattened_list = []
    for sublist in nested_list:
        if isinstance(sublist, list):
            flattened_list.extend(flatten_list(sublist))
        else:
            flattened_list.append(sublist)
    return flattened_list

def compare_list_enrollment_answer(answer_student, answer_teacher):
    correct_answers = 0
    for student_ans, teacher_ans in zip(answer_student, answer_teacher):
        if student_ans == teacher_ans:
            correct_answers += 1
    return correct_answers