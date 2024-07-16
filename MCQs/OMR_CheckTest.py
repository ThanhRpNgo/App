import cv2
import numpy as np
from MCQs.Src.inforFunc import increase_sharpness, image_params, gaussian_blur_a4
from MCQs.Src.utlis import process_image, rectContour, getCornerPoints,reorder, splitBoxes_code, split_5_boxes_each_Sheet, process_image_answersheet, getArray, splitBox_Sheet
#from Src.luufile_giaovien import save_data_teacher
from MCQs.Src.findFrame import adjust_rectangle_coordinates, adjust_answerSheet_coordinates, coordinate_IDandCode
from MCQs.Src.findBlackRect import find_origin
from MCQs.Src.check_code_and_answer import flatten_list,remove_special_characters



def image_process_teacher(pathImage):
    image = cv2.imread(pathImage)
    #### KHU VỰC XỬ LÝ ẢNH GỐC ####
    image = cv2.resize(image, (image_params.width_img, image_params.height_img))
    process_image(image)



    originalPaper1 = np.array([[2408,3508],[2108,2408],[2108,3308],[3508,3308]])
    originalPaper =  np.array([[0,0],[300,0],[300,200],[0,200]])
    #### LẤY GIÁ TRỊ 2 GỐC CỦA BỨC ẢNH CÓ CHỨA HÌNH CHỮ NHẬT ĐỂ LÀM GỐC ####
    #cropped_image1 = imgCoordinate[IF.originalPaper1[0][1]:IF.originalPaper1[2][1], IF.originalPaper1[1][0]:IF.originalPaper1[0][0]]
    #cropped_image2 = imgCoordinate[IF.originalPaper[2][1]:IF.originalPaper[0][1], IF.originalPaper[0][0]:IF.originalPaper[1][0]]
    #cropped_image2 = imgCoordinate[image_params.originalPaper1[2][1]:image_params.originalPaper1[0][1], image_params.originalPaper1[1][0]:image_params.originalPaper1[0][0]]
    #cropped_image1 = imgCoordinate[image_params.originalPaper[0][1]:image_params.originalPaper[2][1], image_params.originalPaper[0][0]:image_params.originalPaper[1][0]]
    #cropped1 = cropped_image1.copy()
    #cropped2 =cropped_image2.copy()

    #########################################################################################################################
    ################# HÀM TÌM TỌA ĐỘ  GỐC CHỨA CÁC PHẦN TỬ HÌNH CHỮ NHẬT ĐEN TRÊN GÓC TRÁI PHIẾU ĐỎ ##################################

    rectangles = []
    for coordinates in [originalPaper, originalPaper1]:
        rectangle_coordinates = find_origin(image, coordinates)
        if rectangle_coordinates is not None:
            rectangles.append(rectangle_coordinates)
    #########################################################################################################################
    if rectangles:
        for i, rect in enumerate(rectangles):
            adjust_coordinates = adjust_rectangle_coordinates([rect],coordinate_IDandCode)
            #Cắt và xuất hình ảnh từ vị trí bottom mới
            for i, rect in enumerate(adjust_coordinates):
                left, top, right, bottom = rect
                cropped_Code_image = image[top:bottom, left:right]
                #idandgradeCase = cropped_Code_image.copy()
    else:
        print("Không tìm thấy hình chữ nhật đen trong các tọa độ đã cho!")
    ######################## HÀM TÁCH KHUNG ##########################################################
    answer_Sheet = adjust_answerSheet_coordinates([(10, 1000, 2300, 3600)])
    # Kiểm tra nếu có tọa độ mới
    if answer_Sheet:
        left, top, right, bottom = answer_Sheet
        # Cắt hình ảnh từ tọa độ của ansher_sheet
        cropped_AnswerSheet_image = image[top:bottom, left:right]
    answerSheet_image = cropped_AnswerSheet_image.copy()
    #cv2.imshow('',answerSheet_image)
    ####################################################################################################    
    cropped_Code_image_copy = cropped_Code_image.copy()
    codeImage = cropped_Code_image.copy()
    codeimageFrame = cropped_Code_image.copy()
    #cv2.imshow('',cropped_Code_image_copy)

    contour_Code, hierachy = cv2.findContours(process_image(codeImage),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    cv2.drawContours(cropped_Code_image_copy,contour_Code,-1,(0,255,0),5)
    rectCode = rectContour(contour_Code)
    codeFrame = getCornerPoints(rectCode[1])
    if codeFrame.size !=0:
        cv2.drawContours(codeImage,codeFrame,-1,(255,0,0),10)
        codeFrame = reorder(codeFrame)

        ptcode1 = np.float32(codeFrame)
        ptcode2 = np.float32([[0,0],[300,0],[0,650],[300,650]])
        matrixcode = cv2.getPerspectiveTransform(ptcode1,ptcode2)
        imgWarpColoedcode = cv2.warpPerspective(codeimageFrame,matrixcode,(300,650))
        #cv2.imshow('',imgWarpColoedcode)

        imgWarpGrayCode = cv2.cvtColor(imgWarpColoedcode,cv2.COLOR_BGR2GRAY)
        imgThreshCode = cv2.threshold(imgWarpGrayCode,150,255,cv2.THRESH_BINARY_INV)[1]
        boxesCode = splitBoxes_code(imgThreshCode)


        myPixelVal_Code = np.zeros((image_params.rows_code,image_params.cols_code))
        countR_Code = 0
        countC_Code = 0
        for codeimageFrame in boxesCode:
            totalPixelCode = cv2.countNonZero(codeimageFrame)
            if countR_Code < myPixelVal_Code.shape[0] and countC_Code < myPixelVal_Code.shape[1]:
                myPixelVal_Code[countR_Code, countC_Code] = totalPixelCode
                countC_Code += 1
                if countC_Code == image_params.cols_code: 
                    countR_Code += 1
                    countC_Code = 0

        #print(myPixelVal_Code)

        myIndex_Code = []
        for x  in range(image_params.cols_code):
            arr_Code = myPixelVal_Code[:, x] 
            index_Code = np.argmax(arr_Code)
            myIndex_Code.append(index_Code)

        myIndex_Code = np.array(myIndex_Code)
        Index_code = myIndex_Code - 1
        #print(Index_code)


    ###############################################################################################################



    #answerSheet_image_copy = answerSheet_image.copy()

    imgShaped_AnswerSheet = increase_sharpness(cropped_AnswerSheet_image, amount=0.5, radius=2)
    imgGray_AnswerSheet = cv2.cvtColor(imgShaped_AnswerSheet, cv2.COLOR_BGR2GRAY) 
    imgBlur_AnswerSheet = gaussian_blur_a4(imgGray_AnswerSheet) 
    imgCanny_AnswerSheet  = cv2.Canny(imgBlur_AnswerSheet,50,100) # APPLY CANNY BLUR
    kernel = np.ones((5, 5))
    imgDial = cv2.dilate(imgCanny_AnswerSheet, kernel, iterations=2) # APPLY DILATION
    imgThreshold = cv2.erode(imgDial, kernel, iterations=1) 


    imgContours_AnswerSheet = answerSheet_image.copy() # COPY IMAGE FOR DISPLAY PURPOSES
    contour_AnsherSheet, hierachy = cv2.findContours(imgThreshold,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    cv2.drawContours(imgContours_AnswerSheet,contour_AnsherSheet,-1,(0,255,0),5)
 
    #cv2.imshow('', imgContours_AnswerSheet)

    rect_AnswerSheet = rectContour(contour_AnsherSheet)
    point_AnswerSheet = getCornerPoints(rect_AnswerSheet[0])
    if point_AnswerSheet.size !=0:
        cv2.drawContours(answerSheet_image,point_AnswerSheet,-1,(255,0,0),10)
        #answerSheet_image = cv2.resize(answerSheet_image,(700,700))
        #cv2.imshow('',answerSheet_image)
        point_AnswerSheet = reorder(point_AnswerSheet)

        pt1_answerSheet = np.float32(point_AnswerSheet)
        pt2_answerSheet = np.float32([[0,0],[1100,0],[0,3600],[1100,3600]])
        matrix_answerSheet = cv2.getPerspectiveTransform(pt1_answerSheet,pt2_answerSheet)
        imgWarpColoed_answerSheet = cv2.warpPerspective(answerSheet_image,matrix_answerSheet,(1100,3600))
        imgWarpColoed_answerSheet = cv2.resize(imgWarpColoed_answerSheet,(700,700))

        imgSheet = imgWarpColoed_answerSheet.copy()
        imgShaped_Sheet = increase_sharpness(imgSheet, amount=0.5, radius=2)
        imgGray_Sheet = cv2.cvtColor(imgShaped_Sheet, cv2.COLOR_BGR2GRAY) 
        imgBlur_Sheet = gaussian_blur_a4(imgGray_Sheet) 
        imgCanny_Sheet  = cv2.Canny(imgBlur_Sheet,50,200)
        contour_Sheet,hierachy=cv2.findContours(imgCanny_Sheet,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
        rectangles = [cv2.boundingRect(contour) for contour in contour_Sheet]
        # Sắp xếp các hình chữ nhật theo chiều từ trái sang phải
        sorted_rectangles = sorted(rectangles, key=lambda rect: rect[0])

        # Chọn hình chữ nhật lớn nhất
        largest_rectangle = max(sorted_rectangles, key=lambda rect: rect[2] * rect[3])

        # Xác định các hình chữ nhật có sự tương đồng với hình chữ nhật lớn nhất
        similar_rectangles = [rect for rect in sorted_rectangles if rect[2] * rect[3] >= largest_rectangle[2] * largest_rectangle[3] * 0.8]


        x, y, w, h = largest_rectangle
        cv2.rectangle(imgSheet, (x, y), (x+w, y+h), (0, 0, 255), 2)

        # Hiển thị các hình chữ nhật tương đồng (màu xanh)
        for rect in similar_rectangles:
            x, y, w, h = rect
            cv2.rectangle(imgSheet, (x, y), (x+w, y+h), (255, 0, 0), 2)
        # Hiển thị ảnh gốc với các hình chữ nhật đã vẽ lên
        cropped_rectangle_images = {}  # Tạo một từ điển để lưu trữ các hình cắt
        for i, rect in enumerate(similar_rectangles):
            x, y, w, h = rect
            x -= 5
            y -= 5
            w += 10
            h += 10
            cropped_rectangle = imgSheet[y:y+h, x:x+w]
            cropped_rectangle_images[f'Cropped Rectangle {i}'] = cropped_rectangle  # Gán mỗi hình cắt cho một biến trong từ điển

        answer_sheets = [cropped_rectangle_images[f'Cropped Rectangle {i}'].copy() for i in range(4)]

        data_Sheet = []
        data_Code = np.array(Index_code) 
        total_questions = 0  # Tổng số câu trong tất cả các box
        for sheet_index in range(4):
            Sheet = split_5_boxes_each_Sheet(process_image_answersheet(answer_sheets[sheet_index]))
            box_r = []
            for box_index in range(1, 6):
                box_dict = Sheet[f'Box_{box_index}']
                box_data = getArray(5, 6, splitBox_Sheet(box_dict)) 
    
                # Loại bỏ các giá trị không chứa A, B, C, D, E và đếm số lượng câu
                num_questions = 0
                box_data_filtered = []  # Khởi tạo danh sách để lưu trữ các hàng đã lọc
                for row in box_data:
                    filtered_row = [value for value in row if value in ['A', 'B', 'C', 'D', 'E','-1']]
                    if filtered_row:  # Kiểm tra nếu hàng vẫn còn phần tử sau khi lọc
                        box_data_filtered.append(filtered_row)
                        num_questions += len(filtered_row)
    
    
                total_questions += num_questions
                box_r.append(box_data_filtered)
            data_Sheet.append(box_r)
        clean_data_Sheet = flatten_list(data_Sheet)
        clean_data_code = remove_special_characters(data_Code)
        if -1 in data_Code: 
            print("Xảy ra lỗi: Sai giá trị Code")
            return clean_data_code,clean_data_Sheet , total_questions
        else:
            return clean_data_code,clean_data_Sheet , total_questions

    #return clean_data_Sheet


if __name__ == '__main__':
    image_process_teacher()