print("LE HOANG VIET DUNG")
print("235752021610104")
def loc_so_le(danh_sach):
  """Hàm lọc các số lẻ từ một danh sách

  Args:
    danh_sach: Danh sách các số nguyên

  Returns:
    list: Danh sách các số lẻ
  """

  so_le = [] 
  for so in danh_sach: 
    if so % 2 != 0:  
      so_le.append(so)  
  return so_le 


danh_sach_nhap = input("Nhập danh sách các số (cách nhau bằng dấu phẩy): ")


danh_sach = [int(so) for so in danh_sach_nhap.split(',')]  

ket_qua = loc_so_le(danh_sach) 
print("Danh sách các số lẻ:", ket_qua)
