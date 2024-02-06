def count_digits_frequency(a, b):
    # Khởi tạo mảng tần số cho các chữ số từ 0 đến 9
    frequency = [0] * 10

    # Tính tần số xuất hiện của các chữ số từ 1 đến b
    for digit in range(1, 10):
        count = (b // 10) * digit  # Số lần xuất hiện đầy đủ của digit trong mọi hàng đơn vị
        count += min(max(0, b % 10 - digit + 1), digit)  # Xuất hiện thêm ở hàng đơn vị nếu cần

        count -= (a // 10) * digit  # Loại bỏ số lần xuất hiện của digit trong mọi hàng đơn vị
        count -= min(max(0, a % 10 - digit + 1), digit)  # Loại bỏ thêm ở hàng đơn vị nếu cần

        frequency[digit] = count

    return frequency

# Đọc số lượng bộ test
T = int(input("Nhập số lượng bộ test T: "))

# Duyệt qua từng bộ test
for _ in range(T):
    # Nhập giá trị a và b cho mỗi bộ test
    a, b = map(int, input().split())

    # Gọi hàm count_digits_frequency để tính tần số xuất hiện của các chữ số
    result = count_digits_frequency(a, b)

    # In kết quả
    print(*result)
