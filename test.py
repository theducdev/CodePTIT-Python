# from datetime import datetime
# ns = "1/1/2001"
# x = datetime.strptime(ns, "%d/%m/%Y")
# print(datetime.strftime(x, "%d/%m/%y"))

from datetime import datetime

def chuan_hoa_ngay_sinh(ngay_sinh_nguon):
    # Chuyển đổi ngày sinh từ định dạng nguồn sang định dạng đích
    ngay_sinh_datetime = datetime.strptime(ngay_sinh_nguon, "%d/%m/%Y")
    ngay_sinh_chuan_hoa = ngay_sinh_datetime.strftime("%d/%m/%Y")
    return ngay_sinh_chuan_hoa

# Nhập ngày sinh từ người dùng
ngay_sinh_nguon = input("Nhập ngày sinh (MM/DD/YYYY): ")

# Chuẩn hóa ngày sinh
ngay_sinh_chuan_hoa = chuan_hoa_ngay_sinh(ngay_sinh_nguon)

# In kết quả
print("Ngày sinh chuẩn hóa:", ngay_sinh_chuan_hoa)
