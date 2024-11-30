print("LE HOANG VIET DUNG")
print("235752021610104")
danh_sach = input("Nhập danh sách các từ: ").split()

danh_sach.reverse()

print("Danh sách các từ sau khi đảo ngược: ", end="")
for sach in danh_sach:
    print(sach, end=" ")
