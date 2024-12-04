print("LE HOANG VIET DUNG")
print("235752021610104")
from search_module import Sequential_Search

def main():
 
    n = int(input("Nhập số lượng phần tử của danh sách: "))
    dlist = []

    for i in range(n):
        value = int(input(f"Nhập giá trị thứ {i+1}: "))
        dlist.append(value)

    item = int(input("Nhập phần tử cần tìm kiếm: "))

    position = Sequential_Search(dlist, item)

    if position != -1:
        print(f"Phần tử {item} được tìm thấy tại vị trí {position + 1}")
    else:
        print(f"Phần tử {item} không có trong danh sách")

if __name__ == "__main__":
    main()
