class Node:
    def __init__(self, key):
        # Khởi tạo một node với giá trị key và trỏ tới next, prev bằng None
        self.key = key
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        # Khởi tạo danh sách liên kết đôi với head và tail bằng None
        self.head = None
        self.tail = None

    def add_last(self, key):
        # Thêm phần tử vào cuối danh sách
        new_node = Node(key)
        current = self.head
        while current:
            # Kiểm tra nếu key đã tồn tại trong danh sách
            if current.key == key:
                return
            current = current.next

        if not self.head:
            # Nếu danh sách rỗng, đặt cả head và tail là new_node
            self.head = self.tail = new_node
        else:
            # Gắn node mới vào cuối danh sách
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def add_first(self, key):
        # Thêm phần tử vào đầu danh sách
        new_node = Node(key)
        current = self.head
        while current:
            # Kiểm tra nếu key đã tồn tại trong danh sách
            if current.key == key:
                return 
            current = current.next

        if not self.head:
            # Nếu danh sách rỗng, đặt cả head và tail là new_node
            self.head = self.tail = new_node
        else:
            # Gắn node mới vào đầu danh sách
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def add_after(self, key, target_key):
        # Thêm phần tử sau một phần tử cụ thể
        new_node = Node(key)
        current = self.head
        current_1 = self.head
        while current_1:
            # Kiểm tra nếu key đã tồn tại trong danh sách
            if current_1.key == key:
                return
            current_1 = current_1.next
        while current:
            if current.key == target_key:
                # Gắn node mới sau target_key
                new_node.next = current.next
                new_node.prev = current
                if current.next:
                    current.next.prev = new_node
                current.next = new_node
                if current == self.tail:
                    # Cập nhật tail nếu node được thêm sau node cuối
                    self.tail = new_node
                break
            current = current.next

    def add_before(self, key, target_key):
        # Thêm phần tử trước một phần tử cụ thể
        new_node = Node(key)
        current = self.head
        current_1 = self.head
        while current_1:
            # Kiểm tra nếu key đã tồn tại trong danh sách
            if current_1.key == key:
                return
            current_1 = current_1.next
        while current:
            if current.key == target_key:
                # Gắn node mới trước target_key
                new_node.prev = current.prev
                new_node.next = current
                if current.prev:
                    current.prev.next = new_node
                else:
                    # Cập nhật head nếu node được thêm trước node đầu tiên
                    self.head = new_node
                current.prev = new_node
                break
            current = current.next

    def remove(self, key):
        # Xóa một phần tử khỏi danh sách
        current = self.head
        while current:
            if current.key == key:
                if current.prev:
                    # Kết nối node trước và node sau để bỏ qua node hiện tại
                    current.prev.next = current.next
                else:
                    # Nếu là phần tử đầu tiên, cập nhật head
                    self.head = current.next
                if current.next:
                    # Nếu là phần tử cuối cùng, cập nhật tail
                    current.next.prev = current.prev
                if current == self.tail:
                    self.tail = current.prev
                break
            current = current.next

    def reverse(self):
        # Đảo ngược danh sách liên kết đôi
        current = self.head
        while current:
            # Đổi vị trí prev và next cho từng node
            current.prev, current.next = current.next, current.prev
            current = current.prev
        # Đổi vị trí head và tail
        self.head, self.tail = self.tail, self.head

def print_linked_list(linked_list):
    # Hàm để in danh sách liên kết
    result = []
    current = linked_list.head
    while current:
        result.append(current.key)
        current = current.next
    return result

# Đọc dữ liệu đầu vào
n = int(input())
data = list(map(int, input().split()))
linked_list = DoublyLinkedList()

# Thêm các phần tử ban đầu vào danh sách liên kết
for item in data:
    linked_list.add_last(item)

# Xử lý các lệnh
while True:
    command = input()
    if command == "#":  # Kết thúc khi gặp ký tự #
        break
    parts = command.split()
    if parts[0] == "addlast":
        k = int(parts[1])
        linked_list.add_last(k)
    elif parts[0] == "addfirst":
        k = int(parts[1])
        linked_list.add_first(k)
    elif parts[0] == "addafter":
        u = int(parts[1])
        v = int(parts[2])
        linked_list.add_after(u, v)
    elif parts[0] == "addbefore":
        u = int(parts[1])
        v = int(parts[2])
        linked_list.add_before(u, v)
    elif parts[0] == "remove":
        k = int(parts[1])
        linked_list.remove(k)
    elif parts[0] == "reverse":
        linked_list.reverse()

# In kết quả
result = print_linked_list(linked_list)
print(" ".join(map(str, result)))
