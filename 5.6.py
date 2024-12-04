print("LE HOANG VIET DUNG")
print("235752021610104")
def main():

    n = int(input("Nhập số lượng phần tử của danh sách: "))
    lst = []

    for i in range(n):
        value = int(input(f"Nhập giá trị thứ {i+1}: "))
        lst.append(value)

    max_value = lst[0]
    min_value = lst[0]
    max_index = 0
    min_index = 0

    for i in range(1, n):
        if lst[i] > max_value:
            max_value = lst[i]
            max_index = i
        if lst[i] < min_value:
            min_value = lst[i]
            min_index = i

    print(f"Danh sách: {lst}")
    print(f"Phần tử lớn nhất: {max_value} tại vị trí {max_index + 1}")
    print(f"Phần tử nhỏ nhất: {min_value} tại vị trí {min_index + 1}")

if __name__ == "__main__":
    main()
