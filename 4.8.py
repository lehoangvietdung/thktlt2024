print("LE HOANG VIET DUNG")
print("235752021610104")
def tim_tu_dai_nhat(danh_sach_tu):
    """Tìm và in ra các từ dài nhất trong một danh sách các từ."""
    
    if not danh_sach_tu:
        print("Danh sách trống! Không có từ nào để tìm.")
        return

    do_dai_lon_nhat = max(len(tu) for tu in danh_sach_tu)
    
    print("Các từ dài nhất:")
    for tu in danh_sach_tu:
        if len(tu) == do_dai_lon_nhat:
            print(tu)

danh_sach_tu = input("Nhập danh sách các từ: ").split()

tim_tu_dai_nhat(danh_sach_tu)
