import cv2
import numpy as np


coordinate_IDandCode = [((30,900,580,900))]

def adjust_rectangle_coordinates(rectangles, coordinate_IDandCode):
    adjusted_rectangles = []
    for rect, new_coord in zip(rectangles, coordinate_IDandCode):
        left, top, right, bottom = rect
        new_left, new_right, new_top, new_bottom = new_coord
        # Tính toán kích thước mới của hình ảnh cắt
        new_right = right + new_right
        new_bottom = bottom + new_bottom
        new_left =  left + new_left
        new_top = top - bottom + new_top
        adjusted_rectangles.append((new_left,new_top,new_right,new_bottom))
    return adjusted_rectangles


coordinate_SheetAnswer = [((30,900,580,3000))]

def adjust_answerSheet_coordinates(coordinate_SheetAnswer):
    max_bottom = float("-inf")
    max_bottom_index = None
    for i, rect in enumerate(coordinate_SheetAnswer):
        left, top, right, bottom = rect
        bottom_pos = top + bottom
        if bottom_pos > max_bottom:
            max_bottom = bottom_pos
            max_bottom_index = i
    
    if max_bottom_index is not None:
        rect = coordinate_SheetAnswer[max_bottom_index]
        left, top, right, bottom = rect
        new_rect = (left + 100, top + 100, right + 100, bottom + 100)
        return new_rect
    else:
        return None




