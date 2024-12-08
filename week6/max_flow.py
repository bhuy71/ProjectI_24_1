# Khởi tạo đồ thị với n đỉnh, sử dụng defaultdict để lưu trữ các cạnh
from collections import defaultdict, deque

class Graph:
    def __init__(self, n):
        self.graph = defaultdict(lambda: defaultdict(int))  # Khởi tạo đồ thị là defaultdict để dễ dàng thêm các cạnh
        self.ROW = n  # Lưu số đỉnh trong đồ thị

    # Hàm thêm cạnh vào đồ thị
    def add_edge(self, u, v, c):
        self.graph[u][v] += c  # Cộng dồn trọng số của cạnh (u, v)

    # Hàm BFS để tìm đường đi từ nguồn s đến đích t
    def bfs(self, s, t, parent):
        visited = [False] * self.ROW  # Mảng lưu trạng thái thăm của các đỉnh
        queue = deque([s])  # Sử dụng deque để thực hiện BFS
        visited[s] = True  # Đánh dấu nguồn s là đã thăm

        # Duyệt các đỉnh theo BFS
        while queue:
            u = queue.popleft()
            for ind, val in self.graph[u].items():  # Duyệt qua các đỉnh kề của u
                if not visited[ind] and val > 0:  # Chưa thăm và có khả năng dòng chảy
                    queue.append(ind)
                    visited[ind] = True  # Đánh dấu đỉnh kề đã thăm
                    parent[ind] = u  # Ghi lại đỉnh cha của đỉnh kề
                    if ind == t:  # Nếu đích t đã được thăm, trả về True
                        return True
        return False  # Nếu không tìm thấy đường đi từ s đến t

    # Hàm Ford-Fulkerson để tính toán lưu lượng lớn nhất
    def ford_fulkerson(self, source, sink):
        parent = [-1] * self.ROW  # Mảng lưu trữ đường đi (cha của mỗi đỉnh)
        max_flow = 0  # Lưu trữ lưu lượng lớn nhất

        # Lặp lại quá trình tìm đường đi từ s đến t cho đến khi không còn đường đi
        while self.bfs(source, sink, parent):
            path_flow = float("Inf")  # Dòng chảy tối thiểu trên đường đi
            s = sink

            # Duyệt ngược từ đích đến nguồn để tìm dòng chảy tối thiểu
            while s != source:
                path_flow = min(path_flow, self.graph[parent[s]][s])  # Dòng chảy tối thiểu trên đoạn đường
                s = parent[s]

            max_flow += path_flow  # Cộng dòng chảy tối thiểu vào tổng lưu lượng

            # Cập nhật đồ thị: giảm dòng chảy trên các cạnh trong đường đi, tăng dòng chảy ngược lại
            v = sink
            while v != source:
                u = parent[v]
                self.graph[u][v] -= path_flow  # Giảm dòng chảy trên cạnh u-v
                self.graph[v][u] += path_flow  # Tăng dòng chảy trên cạnh v-u (dòng ngược)
                v = parent[v]

        return max_flow  # Trả về lưu lượng lớn nhất

def main():
    n, m = map(int, input().split())  # Đọc số đỉnh và số cạnh
    s, t = map(int, input().split())  # Đọc nguồn s và đích t
    g = Graph(n)  # Khởi tạo đồ thị

    # Đọc các cạnh và thêm vào đồ thị
    for _ in range(m):
        u, v, c = map(int, input().split())
        g.add_edge(u - 1, v - 1, c)  # Chuyển từ chỉ số bắt đầu từ 1 sang 0
    
    # Tính lưu lượng lớn nhất từ nguồn s đến đích t
    max_flow = g.ford_fulkerson(s - 1, t - 1)  # Gọi thuật toán Ford-Fulkerson
    print(max_flow)  # In kết quả

main()  # Gọi hàm main để thực thi chương trình
