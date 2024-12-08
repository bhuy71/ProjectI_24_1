# Kiểm tra xem việc đưa đỉnh v vào vị trí p trong chu trình Hamilton có hợp lệ hay không
def is_valid(v, graph, rs, p):
    # Nếu không có cạnh từ đỉnh rs[p-1] đến đỉnh v, trả về False
    if graph[rs[p - 1]][v] == 0:
        return False
    # Nếu đỉnh v đã có trong chu trình, không thể chọn lại đỉnh này
    if v in rs:
        return False
    return True

# Hàm quay lui để tìm chu trình Hamilton
def back_track(graph, rs, p, n):
    # Nếu đã đi qua tất cả các đỉnh (p == n), kiểm tra xem có cạnh từ đỉnh cuối cùng rs[p-1] đến đỉnh đầu tiên rs[0]
    # Nếu có, trả về True, tức là tìm thấy chu trình Hamilton
    if p == n:
        return graph[rs[p - 1]][rs[0]] == 1

    # Duyệt qua các đỉnh còn lại để tìm chu trình Hamilton
    for v in range(1, n):
        # Kiểm tra tính hợp lệ của đỉnh v
        if is_valid(v, graph, rs, p):
            # Nếu hợp lệ, thêm đỉnh v vào vị trí p trong chu trình
            rs[p] = v
            # Tiến hành quay lui với vị trí p+1
            if back_track(graph, rs, p + 1, n):
                return True
            # Nếu không tìm được chu trình, quay lại và thử đỉnh khác
            rs[p] = -1
    return False

# Hàm kiểm tra chu trình Hamilton trong đồ thị
def is_hamilton_cycle(graph, n):
    # Mảng rs lưu trữ chu trình Hamilton, bắt đầu từ đỉnh 0
    rs = [-1] * n
    rs[0] = 0
    # Gọi hàm back_track để kiểm tra chu trình Hamilton
    return back_track(graph, rs, 1, n)

def main():
    # Đọc số bộ test
    T = int(input())
    results = []
    for _ in range(T):
        # Đọc số đỉnh n và số cạnh m
        n, m = map(int, input().split())
        # Khởi tạo ma trận kề đồ thị
        graph = [[0] * n for _ in range(n)]
        # Đọc các cạnh và cập nhật ma trận kề
        for __ in range(m):
            u, v = map(int, input().split())
            graph[u - 1][v - 1] = 1
            graph[v - 1][u - 1] = 1
        # Kiểm tra chu trình Hamilton và lưu kết quả
        results.append(1 if is_hamilton_cycle(graph, n) else 0)

    # In kết quả cho mỗi bộ test
    for result in results:
        print(result)

# Gọi hàm main để thực thi chương trình
main()
