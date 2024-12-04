print("LE HOANG VIET DUNG")
print("235752021610104")
from sort_and_find import sort_list, find_max

def main():
    n = int(input("Nhập số lượng phần tử của danh sách: "))
    lst = []

    for i in range(n):
        value = int(input(f"Nhập giá trị thứ {i+1}: "))
        lst.append(value)

    sorted_list = sort_list(lst)
    max_value = find_max(lst)
    min_value = sorted_list[0]

    print(f"Danh sách sau khi sắp xếp: {sorted_list}")
    print(f"Phần tử lớn nhất: {max_value}")
    print(f"Phần tử nhỏ nhất: {min_value}")

if __name__ == "__main__":
    main()
