# Khởi tạo một từ điển (database) để lưu trữ các phần tử
database = {}

# Vòng lặp để nhập vào các khóa (key) vào cơ sở dữ liệu cho đến khi gặp dấu "*"
while True:
    key = input().strip()  # Đọc vào khóa (key)
    if key == "*":  # Nếu nhập "*" thì kết thúc việc nhập khóa
        break
    database[key] = True  # Thêm khóa vào từ điển và gán giá trị True

# Vòng lặp tiếp theo để xử lý các lệnh tìm kiếm hoặc thêm vào cơ sở dữ liệu
while True:
    temp = input().strip().split()  # Đọc lệnh và tách nó thành các phần
    if temp[0] == "find":
        # Kiểm tra nếu khóa cần tìm có trong cơ sở dữ liệu, in 1 nếu có, 0 nếu không
        print(1 if temp[1] in database else 0)
    elif temp[0] == "insert":
        # Nếu khóa đã có trong cơ sở dữ liệu, in 0 (không thể thêm lại)
        # Nếu chưa có, thêm khóa vào và in 1 (đã thêm thành công)
        if temp[1] in database:
            print(0)
        else:
            database[temp[1]] = True
            print(1)
    elif temp[0] == "***":
        # Dừng chương trình khi gặp lệnh "***"
        break
