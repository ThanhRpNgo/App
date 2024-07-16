import cv2
import numpy as np
from MCQs.Src.inforFunc import increase_sharpness, image_params, gaussian_blur_a4
from MCQs.Src.utlis import process_image, rectContour, getCornerPoints,reorder, splitBoxes_ID, splitBoxes_code, split_5_boxes_each_Sheet, process_image_answersheet, getArray, splitBox_Sheet

#from PIL import Image
from MCQs.Src.findFrame import adjust_rectangle_coordinates, adjust_answerSheet_coordinates, coordinate_IDandCode
from MCQs.Src.findBlackRect import find_origin
from MCQs.Src.check_code_and_answer import flatten_list, remove_special_characters



def img_process_student(path_image):
    image = cv2.imread(path_image)
    #### KHU VỰC XỬ LÝ ẢNH GỐC ####
    image = cv2.resize(image, (image_params.width_img, image_params.height_img))
    process_image(image)
    
    originalPaper1 = np.array([[2408,3508],[2108,2408],[2108,3308],[3508,3308]])
    originalPaper =  np.array([[0,0],[300,0],[300,200],[0,200]])
    #### LẤY GIÁ TRỊ 2 GỐC CỦA BỨC ẢNH CÓ CHỨA HÌNH CHỮ NHẬT ĐỂ LÀM GỐC ####
    #cropped_image1 = imgCoordinate[IF.originalPaper1[0][1]:IF.originalPaper1[2][1], IF.originalPaper1[1][0]:IF.originalPaper1[0][0]]
    #cropped_image2 = imgCoordinate[IF.originalPaper[2][1]:IF.originalPaper[0][1], IF.originalPaper[0][0]:IF.originalPaper[1][0]]
    #cropped_image2 = imgCoordinate[IF.originalPaper1[2][1]:IF.originalPaper1[0][1], IF.originalPaper1[1][0]:IF.originalPaper1[0][0]]
    #cropped_image1 = imgCoordinate[IF.originalPaper[0][1]:IF.originalPaper[2][1], IF.originalPaper[0][0]:IF.originalPaper[1][0]]
    #cropped1 = cropped_image1.copy()
    #cropped2 =cropped_image2.copy()

    #########################################################################################################################
    ################# HÀM TÌM TỌA ĐỘ 2 GỐC CHỨA CÁC PHẦN TỬ HÌNH CHỮ NHẬT ĐEN CỦA PHIẾU ĐỔ ##################################

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
                cropped_IDandCode_image = image[top:bottom, left:right]
                #idandgradeCase = cropped_IDandCode_image.copy()
    #######################################################################################################################


    ######################## HÀM TÁCH KHUNG ##########################################################
    answer_Sheet = adjust_answerSheet_coordinates([(10, 1000, 2300, 3600)])
    # Kiểm tra nếu có tọa độ mới
    if answer_Sheet:
        left, top, right, bottom = answer_Sheet
        # Cắt hình ảnh từ tọa độ của answer_Sheet
        cropped_answer_Sheet = image[top:bottom, left:right]
    answer_Sheet = cropped_answer_Sheet.copy()
    ##############################################################################################################

    cropped_IDandCode_image_copy_1 = cropped_IDandCode_image.copy()
    IDandCode_image = cropped_IDandCode_image.copy()
    IDimageFrame = cropped_IDandCode_image.copy()
    codeimageFrame = cropped_IDandCode_image.copy()
    #cv2.imshow('ID_Frame',IDimageFrame)
 

    ##############################################################################################################
    contour_IDandCode, _ = cv2.findContours(process_image(IDandCode_image),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    cv2.drawContours(cropped_IDandCode_image_copy_1,contour_IDandCode,-1,(0,255,0),5)

    rectIDandCodeFrame = rectContour(contour_IDandCode)
    if rectIDandCodeFrame:
        IDFrame = getCornerPoints(rectIDandCodeFrame[0])
    
        #print(IDFrame.shape)
        codeFrame = getCornerPoints(rectIDandCodeFrame[1])
        #print(codeFrame.shape)
        if IDFrame.size and codeFrame.size != 0:
            cv2.drawContours(IDandCode_image,IDFrame,-1,(0,255,0),10)
            cv2.drawContours(IDandCode_image,codeFrame,-1,(255,0,0),10)

            IDFrame = reorder(IDFrame)
            codeFrame = reorder(codeFrame)

            ptID1 = np.float32(IDFrame)
            ptID2 = np.float32([[0,0],[300,0],[0,650],[300,650]])
            matrixID = cv2.getPerspectiveTransform(ptID1,ptID2)
            imgWarpColoedID = cv2.warpPerspective(IDimageFrame,matrixID,(300,650))
            #imgWarp1 = cv2.resize(imgWarpColoedID,(700,700))
            #cv2.imshow('MaDe_Frame',cropped_IDandCode_image_copy_1)

            ptcode1 = np.float32(codeFrame)
            ptcode2 = np.float32([[0,0],[300,0],[0,650],[300,650]])
            matrixcode = cv2.getPerspectiveTransform(ptcode1,ptcode2)
            imgWarpColoedcode = cv2.warpPerspective(codeimageFrame,matrixcode,(300,650))
            #imgWarp = cv2.resize(imgWarpColoedcode,(700,700))
            #cv2.imshow('MaDep',imgWarp)

            ######################################################################################################
            #################### LỌC FILTER THÊM 1 LẦN NỮA CHO IDFRAME VÀ CODEFRAME ##############################
            imgWarpGrayID = cv2.cvtColor(imgWarpColoedID,cv2.COLOR_BGR2GRAY)
            imgThreshID = cv2.threshold(imgWarpGrayID,150,255,cv2.THRESH_BINARY_INV)[1]
            imgWarpGrayCode = cv2.cvtColor(imgWarpColoedcode,cv2.COLOR_BGR2GRAY)
            imgThreshCode = cv2.threshold(imgWarpGrayCode,150,255,cv2.THRESH_BINARY_INV)[1]
            #resize_image = cv2.resize(imgWarpGrayCode,(700,700))
            #cv2.imshow('MaDe_Frame',resize_image)
            #resize_image_1 = cv2.resize(imgThreshID,(700,700))
            #cv2.imshow('ID_Frame',imgWarpGrayID)
            

            boxesID = splitBoxes_ID(imgThreshID)
            boxesCode = splitBoxes_code(imgThreshCode)

            myPixelVal_ID = np.zeros((image_params.rows_id,image_params.cols_id))
            countR_ID = 0
            countC_ID = 0

            for IDimageFrame in boxesID:
                totalPixelID = cv2.countNonZero(IDimageFrame)
                myPixelVal_ID[countR_ID, countC_ID] = totalPixelID
                countC_ID += 1
                if countC_ID == image_params.cols_id:  # Nếu đã đủ cột, chuyển sang hàng tiếp theo
                    countR_ID += 1
                    countC_ID = 0

            #print(myPixelVal_ID)

            myIndex_ID = []
            for x  in range(image_params.cols_id):
                arr_ID = myPixelVal_ID[:, x] 
                index_ID = np.argmax(arr_ID)
                myIndex_ID.append(index_ID)
            myIndex_ID = np.array(myIndex_ID)
            Index_ID = myIndex_ID -1



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



        #answer_Sheet_copy = answer_Sheet.copy()

        imgShaped_AnswerSheet = increase_sharpness(cropped_answer_Sheet, amount=0.5, radius=2)
        imgGray_AnswerSheet = cv2.cvtColor(imgShaped_AnswerSheet, cv2.COLOR_BGR2GRAY) 
        imgBlur_AnswerSheet = gaussian_blur_a4(imgGray_AnswerSheet) 
        imgCanny_AnswerSheet  = cv2.Canny(imgBlur_AnswerSheet,50,100) # APPLY CANNY BLUR
        kernel = np.ones((5, 5))
        imgDial = cv2.dilate(imgCanny_AnswerSheet, kernel, iterations=2) # APPLY DILATION
        imgThreshold = cv2.erode(imgDial, kernel, iterations=1) 


        imgContours_AnswerSheet = answer_Sheet.copy() # COPY IMAGE FOR DISPLAY PURPOSES
        contour_AnsherSheet, _ = cv2.findContours(imgThreshold,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
        cv2.drawContours(imgContours_AnswerSheet,contour_AnsherSheet,-1,(0,255,0),5)
        #resize_image1 = cv2.resize(imgContours_AnswerSheet,(700,700))
        #cv2.imshow('', resize_image1)

        rect_AnswerSheet = rectContour(contour_AnsherSheet)
        point_AnswerSheet = getCornerPoints(rect_AnswerSheet[0])
        if point_AnswerSheet.size !=0:
            cv2.drawContours(answer_Sheet,point_AnswerSheet,-1,(255,0,0),10)
            #resize_image = cv2.resize(answer_Sheet,(700,700))
            #cv2.imshow('',resize_image)
            point_AnswerSheet = reorder(point_AnswerSheet)

            pt1_answerSheet = np.float32(point_AnswerSheet)
            pt2_answerSheet = np.float32([[0,0],[1100,0],[0,3600],[1100,3600]])
            matrix_answerSheet = cv2.getPerspectiveTransform(pt1_answerSheet,pt2_answerSheet)
            imgWarpColoed_answerSheet = cv2.warpPerspective(answer_Sheet,matrix_answerSheet,(1100,3600))
            imgWarpColoed_answerSheet = cv2.resize(imgWarpColoed_answerSheet,(700,700))

            imgSheet = imgWarpColoed_answerSheet.copy()
            imgShaped_Sheet = increase_sharpness(imgSheet, amount=0.5, radius=2)
            imgGray_Sheet = cv2.cvtColor(imgShaped_Sheet, cv2.COLOR_BGR2GRAY) 
            imgBlur_Sheet = gaussian_blur_a4(imgGray_Sheet) 
            imgCanny_Sheet  = cv2.Canny(imgBlur_Sheet,50,200)
            contour_Sheet,_=cv2.findContours(imgCanny_Sheet,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
            #resize_image = cv2.resize(imgCanny_Sheet,(700,700))
            #cv2.imshow('DapAn_Frame',resize_image)
            


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
            #for i, image in enumerate(answer_sheets):
            #    cv2.imshow(f'Cropped Rectangle {i}', image)
            data_Sheet = []
            data_ID = np.array(Index_ID) 
            data_Code = np.array(Index_code) 
            #total_questions = 0  # Tổng số câu trong tất cả các box 
            for sheet_index in range(4):
                Sheet = split_5_boxes_each_Sheet(process_image_answersheet(answer_sheets[sheet_index]))
                box_r = []
                for box_index in range(1, 6):
                    box_dict = Sheet[f'Box_{box_index}']
                    box_data = getArray(5, 6, splitBox_Sheet(box_dict)) 
        
                    # Loại bỏ các giá trị không chứa A, B, C, D, E và đếm số lượng câu
                    box_data_filtered = []  # Khởi tạo danh sách để lưu trữ các hàng đã lọc
                    for row in box_data:
                        filtered_row = [value for value in row if value in ['0','A', 'B', 'C', 'D', 'E']]
                        if filtered_row:  # Kiểm tra nếu hàng vẫn còn phần tử sau khi lọc
                            box_data_filtered.append(filtered_row)
                            #num_questions += len(filtered_row)  
                        else:
                            break
                    #total_questions += num_questions
                    box_r.append(box_data_filtered)
                data_Sheet.append(box_r)
            clean_data_Sheet = flatten_list(data_Sheet)
            clean_data_ID = remove_special_characters(data_ID)
            clean_data_Code = remove_special_characters(data_Code)
            
            if -1 in data_ID or -1 in data_Code:
                print("Có lỗi xảy ra cần kiểm tra lại")
                return None
            else:
                return clean_data_ID,clean_data_Code,clean_data_Sheet#, total_questions
        else:
            print("thieu dữ liệu vui lòng kiểm tra lại độ sáng và các giá trị ID, Mã Đề, answer_sheet đã được chỉnh chưa",path_image)
    
    #return clean_data_Sheet

if __name__ == '__main__':
    #img_process_student()
    result = img_process_student('2.jpg')
    if result:
        clean_data_ID, clean_data_Code, clean_data_Sheet = result
        print("ID:", clean_data_ID)
        print("Code:", clean_data_Code)
        print("Answer Sheet:", clean_data_Sheet)
   #
    # Add key event handling to close OpenCV windows
    while True:
        if cv2.waitKey(1) & 0xFF == ord('s'):
            break
    cv2.destroyAllWindows()
    #################################################################################################################
    ############################################# LƯU VÀO TẬP TIN TXT ###############################################










