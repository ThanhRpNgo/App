import cv2
import numpy as np
from MCQs.Src.inforFunc import increase_sharpness, gaussian_blur_a4
#import inforFunc as infor
#import os
#from PIL import Image
import matplotlib.pyplot as plt

## TO STACK ALL THE IMAGES IN ONE WINDOW (với Hàm StackImage hổ trợ cho người dụng việc kết hợp tất cả bộ lọc vào 1 khung hình)
def stackImages(imgArray,scale,lables=[]):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
            hor_con[x] = np.concatenate(imgArray[x])
        ver = np.vstack(hor)
        ver_con = np.concatenate(hor)
    else:
        for x in range(0, rows):
            imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        hor_con= np.concatenate(imgArray)
        ver = hor
    if len(lables) != 0:
        eachImgWidth= int(ver.shape[1] / cols)
        eachImgHeight = int(ver.shape[0] / rows)
        #print(eachImgHeight)
        for d in range(0, rows):
            for c in range (0,cols):
                cv2.rectangle(ver,(c*eachImgWidth,eachImgHeight*d),(c*eachImgWidth+len(lables[d][c])*13+27,30+eachImgHeight*d),(255,255,255),cv2.FILLED)
                cv2.putText(ver,lables[d][c],(eachImgWidth*c+10,eachImgHeight*d+20),cv2.FONT_HERSHEY_COMPLEX,0.7,(255,0,255),2)
    return ver

def reorder(myPoints):

    myPoints = myPoints.reshape((4, 2)) # REMOVE EXTRA BRACKET 
    #print(myPoints)
    myPointsNew = np.zeros((4, 1, 2), np.int32) # NEW MATRIX WITH ARRANGED POINTS (tạo ra 1 ma trận có các điểm đã được sắp xếp)
    add = myPoints.sum(1) #tính tổng từng giá trị 
    #print(add)
    #print(np.argmax(add))
    myPointsNew[0] = myPoints[np.argmin(add)]  #[0,0]
    myPointsNew[3] =myPoints[np.argmax(add)]   #[w,h]
    diff = np.diff(myPoints, axis=1)
    myPointsNew[1] =myPoints[np.argmin(diff)]  #[w,0]
    myPointsNew[2] = myPoints[np.argmax(diff)] #[h,0]

    return myPointsNew

################################################################
# HÀM BIỂU THỊ CÁC VIỀN DÀNH CHO HÌNH CHỮ NHẬT
def rectContour(contours):
    rectCon = []
    max_area = 0
    for i in contours:
        area = cv2.contourArea(i)
        if area > 50:
            peri = cv2.arcLength(i, True)
            approx = cv2.approxPolyDP(i, 0.02 * peri, True)
            if len(approx) == 4:
                rectCon.append(i)
    rectCon = sorted(rectCon, key=cv2.contourArea,reverse=True)
    #print(len(rectCon))
    return rectCon

def getCornerPoints(cont):
    peri = cv2.arcLength(cont, True) # LENGTH OF CONTOUR
    approx = cv2.approxPolyDP(cont, 0.02 * peri, True) # APPROXIMATE THE POLY TO GET CORNER POINTS
    return approx

def resizeImage(img, new_height, new_width):
    return cv2.resize(img, (new_width, new_height))

def splitBoxes_ID(img):
    resized_img = resizeImage(img, new_height=(img.shape[0] // 11) * 11, new_width=(img.shape[1] // 7) * 7)
    rows = np.vsplit(resized_img, 11)
    boxes = []
    for r in rows:
        cols = np.hsplit(r, 7)
        for box in cols:
            boxes.append(box)
            #cv2.imshow('',cols[1])
    return boxes

def splitBoxes_code(img):
    resized_img = resizeImage(img, new_height=(img.shape[0] // 11) * 11, new_width=(img.shape[1] // 4) * 4)
    rows_Code = np.vsplit(resized_img, 11)
    boxes = []
    for r in rows_Code:
        cols_Code = np.hsplit(r, 4)
        for box in cols_Code:
            boxes.append(box)
            #cv2.imshow('',rows_Code[1])
    return boxes

def split_5_boxes_each_Sheet(image):
    # Dịch lên 10 pixel mỗi hình chữ nhật
    shifted_boxes = [box[:-30, :] for box in np.vsplit(image, 5)]
    box_dict = {}
    for i, box in enumerate(shifted_boxes):
        box_dict[f'Box_{i+1}'] = box
    return box_dict


def process_image(image_path):
    imgShaped = increase_sharpness(image_path, amount=0.5, radius=2)
    imgGray = cv2.cvtColor(imgShaped, cv2.COLOR_BGR2GRAY) 
    imgBlur = gaussian_blur_a4(imgGray) 
    imgCanny  = cv2.Canny(imgBlur, 10, 50)
    #cv2.imshow('',imgCanny)
    return imgCanny  
def process_image_answersheet(image):
        image_sheet = image.copy()
        imgShaped = increase_sharpness(image, amount=0.5, radius=2)
        imgGray = cv2.cvtColor(imgShaped, cv2.COLOR_BGR2GRAY) 
        imgBlur = gaussian_blur_a4(imgGray) 
        imgCanny  = cv2.Canny(imgBlur,10,50)
        
        contour, _  = cv2.findContours(imgCanny,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
        cv2.drawContours(image,contour,-1,(0,255,0),2)

        rect_answerSheet = rectContour(contour)
        answersheetFrame = getCornerPoints(rect_answerSheet[0])
        if answersheetFrame.size !=0:
            cv2.drawContours(image,answersheetFrame,-1,(255,0,0),10)
            answersheetFrame = reorder(answersheetFrame)

            pt1_answerSheet = np.float32(answersheetFrame)
            pt2_answerSheet = np.float32([[0,0],[300,0],[0,2500],[300,2500]])
            matrix_Sheet = cv2.getPerspectiveTransform(pt1_answerSheet,pt2_answerSheet)
            imgWarpColorSheet = cv2.warpPerspective(image_sheet,matrix_Sheet,(300,2600))
            imgWarpColorSheet=imgWarpColorSheet[20:imgWarpColorSheet.shape[0] - 100 , 10:imgWarpColorSheet.shape[1] - 10]

            imgWarpGray_Sheet = cv2.cvtColor(imgWarpColorSheet,cv2.COLOR_BGR2GRAY)
            imgThresh_Sheet  = cv2.threshold(imgWarpGray_Sheet,150,255,cv2.THRESH_BINARY_INV)[1]
            return imgThresh_Sheet
        
def find_ConerPoint(frame):
    imgShaped = increase_sharpness(frame, amount=0.5, radius=2)
    imgGray = cv2.cvtColor(imgShaped, cv2.COLOR_BGR2GRAY) 
    imgBlur = gaussian_blur_a4(imgGray) 
    imgCanny  = cv2.Canny(imgBlur,10,50)
    
    contour, _ = cv2.findContours(imgCanny,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    cv2.drawContours(frame,contour,-1,(0,255,0),2)
    rect_answerSheet = rectContour(contour)
    answersheetFrame = getCornerPoints(rect_answerSheet[0])
    return answersheetFrame

    
def splitBox_Sheet(img):
    boxes = []
    resized_img = resizeImage(img, new_height=(img.shape[0] // 5) * 5, new_width=(img.shape[1] // 6) * 6)
    rows = np.vsplit(resized_img, 5)
    for row in rows:
        cols = np.hsplit(row, 6)
        for box in cols:
            boxes.append(box)   
        #    cv2.imshow('',box)
        #cv2.waitKey(0)
        #cv2.destroyAllWindows            
    return boxes

def getArray(rows, columns, boxes):
    countR = 0
    countC = 0
    choices = columns 
    myPixelVal = np.zeros((rows, columns))
    data = []
    answers = []  # Initialize the answers list
    for image in boxes:
        totalPixels = cv2.countNonZero(image)
        if countR < rows and countC < columns:  
            myPixelVal[countR][countC] = totalPixels
            countC += 1
            if countC == choices:
                countC = 0
                countR += 1
    myPixelVal[:, 0] = '0'
    # Duyệt qua từng hàng trong mảng
    for row in myPixelVal:
        sorted_row = sorted(row, reverse=True)  # Sắp xếp hàng theo thứ tự giảm dần
        if len(sorted_row) >= 2:
            max_value = sorted_row[0]  # Giá trị lớn nhất
            second_max_value = sorted_row[1]  # Giá trị lớn nhì
            #average = (max_value - second_max_value) /2
            # Kiểm tra nếu chênh lệch giữa hai giá trị lớn nhất và lớn nhì nằm trong khoảng max_value - 200
            if second_max_value >= max_value - 200:
                answers.append('0')  # Trả về 0 nếu có
                continue  # Chuyển sang hàng tiếp theo

            # Xử lý bình thường nếu không thoả điều kiện
            
        max_indices = np.where(row == np.amax(row))[0]  # Lấy các chỉ mục của giá trị lớn nhất trong hàng
        answer = ""
        for index in max_indices:
            choices = ['0','A', 'B', 'C', 'D', 'E']
            if index < len(choices):
                answer += choices[index] + ","
        answers.append(answer[:-1])  # Loại bỏ dấu phẩy cuối cùng
    #print(myPixelVal)
    return answers




    

    
    
    
    

    




