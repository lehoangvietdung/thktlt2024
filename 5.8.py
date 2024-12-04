print("LE HOANG VIET DUNG")
print("235752021610104")
def Sequential_Search(dlist, item):
    for i in range(len(dlist)):
        if dlist[i] == item:
            return (True, i)
    return (False, -1)

def input_list(n):
    dlist = []
    for _ in range(n):
        element = int(input("Nhập phần tử: "))
        dlist.append(element)
    return dlist

n = int(input("Nhập số lượng phần tử trong danh sách: "))
dlist = input_list(n)

item = int(input("Nhập phần tử cần tìm kiếm: "))

found, index = Sequential_Search(dlist, item)

if found:
    print(f"Phần tử {item} được tìm thấy tại chỉ mục {index}.")
else:
    print(f"Phần tử {item} không được tìm thấy.")
