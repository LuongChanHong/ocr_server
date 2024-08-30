import easyocr
import cv2
import os

from os import sep
import pathlib
import warnings

# Bỏ qua cảnh báo FutureWarning về bảo mật của torch.load
warnings.filterwarnings("ignore", category=FutureWarning)

files = os.listdir(path='../OCR/img')
for item in files:
    item = "F:\DocCode\OCR"+item

print(files)
# print( os.path.dirname(os.path.abspath(__file__))+sep) 
# print => F:\DocCode\OCR\
print("\n")

class Promotion:
    def __init__(self,branch,category,pack_size,name,normal_price,promo_price,scheme_promotion):
        self.branch=branch
        self.category=category
        self.pack_size=pack_size
        self.name=name
        self.normal_price=normal_price
        self.promo_price=promo_price
        self.scheme_promotion=scheme_promotion

# Đọc ảnh
# image_axe = "F:/DocCode/OCR/axe.JPG"
# image_oliv = "F:\DocCode\OCR\oliv.JPG"

# image = cv2.imread(image_oliv)

# # Khởi tạo EasyOCR
# reader = easyocr.Reader(['vi'])  # 'en' là mã ngôn ngữ, bạn có thể thêm ngôn ngữ khác nếu cần

# # Nhận dạng văn bản từ ảnh
# result = reader.readtext(image)

# # Hiển thị kết quả
# for (bbox, text, prob) in result:
#     print(f"Detected text: {text}")