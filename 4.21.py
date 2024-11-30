print("LE HOANG VIET DUNG")
print("235752021610104")
def kiem_tra_chia_het_cho_5(chuoi_nhi_phan):
  """Kiểm tra và in các số nhị phân chia hết cho 5 trong một chuỗi

  Args:
    chuoi_nhi_phan: Chuỗi các số nhị phân cách nhau bởi dấu phẩy
  """
  
  danh_sach_so_nhi_phan = chuoi_nhi_phan.split(',')

  ket_qua = []
  for so_nhi_phan in danh_sach_so_nhi_phan:

    so_thap_phan = int(so_nhi_phan, 2)

    if so_thap_phan % 5 == 0:
      ket_qua.append(so_nhi_phan)

  print(','.join(ket_qua))

chuoi_nhap = input("Nhập chuỗi các số nhị phân: ")

kiem_tra_chia_het_cho_5(chuoi_nhap)
