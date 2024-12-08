import sys
import bisect
from collections import defaultdict

# Thiết lập giới hạn đệ quy để tránh lỗi khi xử lý dữ liệu lớn
sys.setrecursionlimit(1 << 25)

# Lớp Person đại diện cho thông tin của mỗi người dân
class Person:
    def __init__(self, code, date_of_birth, father_code, mother_code, is_alive, region_code):
        self.code = code  # Mã của người
        self.date_of_birth = date_of_birth  # Ngày sinh của người
        self.father_code = father_code  # Mã của cha
        self.mother_code = mother_code  # Mã của mẹ
        self.is_alive = is_alive  # Trạng thái sống (sống hay chết)
        self.region_code = region_code  # Mã vùng
        self.children = []  # Danh sách con cái
        self.generation_distance = None  # Khoảng cách thế hệ từ cha mẹ

# Lớp CitizenDatabase dùng để quản lý cơ sở dữ liệu dân số
class CitizenDatabase:
    def __init__(self):
        self.code_to_person = {}  # Mã người -> đối tượng Person
        self.date_counts = defaultdict(int)  # Đếm số lượng người sinh vào mỗi ngày
        self.cumulative_date_counts = []  # Danh sách cộng dồn số người theo ngày sinh
        self.persons = []  # Danh sách các đối tượng Person
        self.total_people = 0  # Tổng số người

    # Thêm một người vào cơ sở dữ liệu
    def add_person(self, line):
        tokens = line.strip().split()  # Tách các phần từ trong dòng
        code, date_of_birth, father_code, mother_code, is_alive_char, region_code = tokens
        is_alive = is_alive_char == 'Y'  # Kiểm tra trạng thái sống
        person = Person(code, date_of_birth, father_code, mother_code, is_alive, region_code)
        self.code_to_person[code] = person  # Lưu người vào cơ sở dữ liệu
        self.persons.append(person)  # Thêm người vào danh sách
        self.date_counts[date_of_birth] += 1  # Cập nhật số lượng người sinh vào ngày này
        self.total_people += 1  # Tăng tổng số người

    # Xây dựng mối quan hệ cha mẹ-con cái giữa các người
    def build_relationships(self):
        for person in self.persons:
            if person.father_code != '0000000' and person.father_code in self.code_to_person:
                self.code_to_person[person.father_code].children.append(person)
            if person.mother_code != '0000000' and person.mother_code in self.code_to_person:
                self.code_to_person[person.mother_code].children.append(person)

    # Xây dựng danh sách ngày sinh đã sắp xếp và cộng dồn số lượng người
    def build_date_list(self):
        dates = sorted(self.date_counts.keys())  # Sắp xếp các ngày sinh
        cumulative = 0  # Biến dùng để tính cộng dồn
        self.cumulative_date_counts.clear()  # Xóa dữ liệu cũ
        for date in dates:
            cumulative += self.date_counts[date]  # Cộng dồn số lượng người sinh vào mỗi ngày
            self.cumulative_date_counts.append((date, cumulative))  # Lưu kết quả

    # Trả về tổng số người trong cơ sở dữ liệu
    def get_number_of_people(self):
        return self.total_people

    # Trả về số lượng người sinh vào một ngày cụ thể
    def get_number_of_people_born_at(self, date):
        return self.date_counts.get(date, 0)

    # Trả về số lượng người sinh trong khoảng thời gian từ ngày "from_date" đến "to_date"
    def get_number_of_people_born_between(self, from_date, to_date):
        if not self.cumulative_date_counts:
            self.build_date_list()  # Xây dựng danh sách ngày nếu chưa có
        start_idx = bisect.bisect_left(self.cumulative_date_counts, (from_date, 0))  # Tìm chỉ số ngày bắt đầu
        end_idx = bisect.bisect_right(self.cumulative_date_counts, (to_date, float('inf'))) - 1  # Tìm chỉ số ngày kết thúc
        if start_idx > end_idx:
            return 0
        end_count = self.cumulative_date_counts[end_idx][1]  # Lấy số lượng người ở ngày kết thúc
        start_count = self.cumulative_date_counts[start_idx - 1][1] if start_idx > 0 else 0  # Số lượng người ở ngày bắt đầu
        return end_count - start_count  # Trả về số lượng người trong khoảng thời gian

    # Trả về khoảng cách thế hệ của tổ tiên sống nhất của một người
    def get_most_alive_ancestor(self, code):
        if code not in self.code_to_person:
            return 0
        person = self.code_to_person[code]
        return self.compute_generation_distance(person)

    # Tính khoảng cách thế hệ của một người
    def compute_generation_distance(self, person):
        if person.generation_distance is not None:
            return person.generation_distance
        father_distance = (self.compute_generation_distance(self.code_to_person[person.father_code]) + 1
                           if person.father_code in self.code_to_person else 0)
        mother_distance = (self.compute_generation_distance(self.code_to_person[person.mother_code]) + 1
                           if person.mother_code in self.code_to_person else 0)
        person.generation_distance = max(father_distance, mother_distance)  # Khoảng cách thế hệ là khoảng cách tối đa giữa cha và mẹ
        return person.generation_distance

    # Trả về số người không có quan hệ huyết thống (tối đa số lượng không liên quan)
    def get_max_unrelated_people(self):
        # Xây dựng đồ thị đại diện cho các mối quan hệ cha mẹ - con cái
        graph = defaultdict(list)
        
        for person in self.persons:
            if person.father_code != '0000000' and person.father_code in self.code_to_person:
                father = self.code_to_person[person.father_code]
                graph[person.code].append(father.code)
                graph[father.code].append(person.code)
            if person.mother_code != '0000000' and person.mother_code in self.code_to_person:
                mother = self.code_to_person[person.mother_code]
                graph[person.code].append(mother.code)
                graph[mother.code].append(person.code)

        # Thuật toán tham lam để tìm tập độc lập lớn nhất
        visited = set()  # Tập các người đã được thăm
        independent_set = set()  # Tập các người không có quan hệ huyết thống
        
        for person_code in self.code_to_person:
            if person_code not in visited:
                # Thêm người hiện tại vào tập độc lập
                independent_set.add(person_code)
                visited.add(person_code)
                # Đánh dấu tất cả các láng giềng là đã thăm
                for neighbor in graph[person_code]:
                    visited.add(neighbor)

        return len(independent_set)  # Trả về kích thước của tập độc lập

# Hàm main để đọc dữ liệu và xử lý các truy vấn
def main():
    db = CitizenDatabase()
    lines = sys.stdin.read().split('\n')  # Đọc dữ liệu từ đầu vào
    i = 0
    n = len(lines)

    while i < n:
        line = lines[i]
        i += 1
        if line.strip() == '*':
            break
        if not line.strip():
            continue
        db.add_person(line)  # Thêm người vào cơ sở dữ liệu
    db.build_relationships()  # Xây dựng các mối quan hệ cha mẹ - con cái

    queries = []
    while i < n:
        line = lines[i]
        i += 1
        if line.strip() == '***':
            break
        if not line.strip():
            continue
        queries.append(line)

    # Xử lý các truy vấn
    for query_line in queries:
        tokens = query_line.strip().split()
        if not tokens:
            continue
        command = tokens[0]
        if command == 'NUMBER_PEOPLE':
            print(db.get_number_of_people())
        elif command == 'NUMBER_PEOPLE_BORN_AT':
            date = tokens[1]
            print(db.get_number_of_people_born_at(date))
        elif command == 'NUMBER_PEOPLE_BORN_BETWEEN':
            from_date = tokens[1]
            to_date = tokens[2]
            print(db.get_number_of_people_born_between(from_date, to_date))
        elif command == 'MOST_ALIVE_ANCESTOR':
            code = tokens[1]
            print(db.get_most_alive_ancestor(code))
        elif command == 'MAX_UNRELATED_PEOPLE':
            print(db.get_max_unrelated_people())

if __name__ == '__main__':
    main()
