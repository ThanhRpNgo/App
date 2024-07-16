import cv2
import numpy as np

#HÀM BẮT ĐIỂM CÓ HÌNH CHỮ NHẬT THUỘC DIỆN TÍCH TỪ  40 -> 50

class ImageProcessingParams:
    def __init__(self, threshold_low, threshold_high, width_img, height_img,
                 x_offset, y_offset, x1_offset, y1_offset,
                 rows_id, cols_id, rows_code, cols_code,
                 sheet_rows, sheet_cols, alpha, beta):
        self.threshold_low = threshold_low
        self.threshold_high = threshold_high
        self.width_img = width_img
        self.height_img = height_img
        self.x_offset = x_offset
        self.y_offset = y_offset
        self.x1_offset = x1_offset
        self.y1_offset = y1_offset
        self.rows_id = rows_id
        self.cols_id = cols_id
        self.rows_code = rows_code
        self.cols_code = cols_code
        self.sheet_rows = sheet_rows
        self.sheet_cols = sheet_cols
        self.alpha = alpha
        self.beta = beta

# Tạo một instance của class và truyền các giá trị vào
image_params = ImageProcessingParams(
    threshold_low=0,
    threshold_high=2000,
    width_img=2408,
    height_img=3508,
    x_offset=600,
    y_offset=650,
    x1_offset=0,
    y1_offset=0,
    rows_id=11,
    cols_id=7,
    rows_code=11,
    cols_code=4,
    sheet_rows=5,
    sheet_cols=6,
    alpha=1.1,
    beta=0.4
)   # Đối với việc tăng cường tương phản, beta thường được đặt là 0
def gaussian_blur_a4(image):
    # Kích thước ảnh A4 thường là khoảng 210mm x 297mm
    # Trong pixel, điều này có thể thay đổi tùy thuộc vào độ phân giải của ảnh
    # Dưới đây là một ước lượng về kích thước ảnh A4 ở đơn vị pixel


    # Tính toán kích thước kernel Gaussian dựa trên kích thước ảnh A4
    kernel_width = int(image_params.width_img / 700) // 2 * 2 + 1  # Kernel width là một số lẻ
    kernel_height = int(image_params.height_img / 800) // 2 * 2 + 1  # Kernel height là một số lẻ

    # Áp dụng Gaussian blur với kích thước kernel được tính toán
    imgBlur = cv2.GaussianBlur(image, (kernel_width, kernel_height), 0)

    return imgBlur

def increase_sharpness(image, amount=1.0, radius=1.0):
    # Tạo bản sao của ảnh để tránh thay đổi ảnh gốc
    imgShaped = np.copy(image)
    # Áp dụng bộ lọc unsharp mask để tăng độ rõ nét
    imgShaped = cv2.GaussianBlur(imgShaped, (1, 1), radius)
    imgShaped = cv2.addWeighted(image, 1.0 + amount, imgShaped, -amount, 0)

    return imgShaped


originalPaper1 = np.array([[2408,3508],[2108,2408],[2108,3308],[3508,3308]])
originalPaper =  np.array([[0,0],[300,0],[300,200],[0,200]])
#originalPaper1 = np.array([[700,0],[600,0],[600,50],[700,50]])
#originalPaper =  np.array([[0,700],[100,700],[100,650],[0,650]])

  

