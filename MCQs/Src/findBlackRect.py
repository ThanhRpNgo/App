import cv2
import numpy as np




def find_black_rectangle_coordinates(image):
    width, height,_ = image.shape
    #black_threshold = 0.95  # Ngưỡng đen, tức là phần trăm của số điểm ảnh đen so với tổng số điểm ảnh
    # Tạo danh sách để lưu tọa độ của các điểm ảnh đen
    black_pixels = []
    # Đếm số điểm ảnh đen và lưu tọa độ của chúng
    for x in range(width):
        for y in range(height):
            pixel = image[x, y]  # Lưu ý rằng OpenCV sử dụng thứ tự (y, x) cho pixel
            if isinstance(pixel, np.ndarray):
                if sum(pixel[:3]) < 10:  # Giả sử màu đen nếu tổng của B, G, R nhỏ hơn 10
                    black_pixels.append((x, y))
            elif isinstance(pixel, int):  # Đối với ảnh xám
                if pixel < 10:  # Giả sử màu đen nếu giá trị pixel nhỏ hơn 10
                    black_pixels.append((x, y))
    # Nếu không có điểm ảnh đen nào, trả về None
    if not black_pixels:
        return None
    # Tìm tọa độ của hình chữ nhật bằng cách xác định tọa độ của cạnh trái, phải, trên và dưới
    left = min(point[0] for point in black_pixels)
    right = max(point[0] for point in black_pixels)
    top = min(point[1] for point in black_pixels)
    bottom = max(point[1] for point in black_pixels)
    # Trả về tọa độ của hình chữ nhật
    return (left, top, right, bottom)


def find_origin(image, coordinates):
    rectangle_coordinates = find_black_rectangle_coordinates(image[coordinates[1][1]:coordinates[3][1], coordinates[0][0]:coordinates[1][0]])
    if rectangle_coordinates is not None:
        return rectangle_coordinates
    else:
        flipped_image = cv2.flip(image, -1)  # Đảo hình ảnh theo cả hai chiều
        rectangle_coordinates = find_black_rectangle_coordinates(flipped_image[coordinates[1][1]:coordinates[3][1], coordinates[0][0]:coordinates[1][0]])
        if rectangle_coordinates is not None:
            return rectangle_coordinates
    return None