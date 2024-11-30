print("LE HOANG VIET DUNG")
print("235752021610104")
ho_ten = input("Họ tên đầy đủ :")

vi_tri_khoang_trang = ho_ten.find(" ")


ho = ho_ten[:vi_tri_khoang_trang]
ten = ho_ten[vi_tri_khoang_trang+1:]

print("Họ:", ho)
print("Tên:", ten)
