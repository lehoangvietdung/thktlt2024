print("LE HOANG VIET DUNG")
print("235752021610104")
def dem_chu_hoa_thuong(cau):
  """Đếm số lượng chữ hoa và chữ thường trong một câu

  Args:
    cau: Câu cần đếm

  Returns:
    tuple: Một tuple chứa (số chữ hoa, số chữ thường)
  """

  so_chu_hoa = 0  
  so_chu_thuong = 0   

  for ky_tu in cau: 
    if ky_tu.isupper():  
      so_chu_hoa += 1 
      so_chu_thuong += 1  

  return so_chu_hoa, so_chu_thuong 


cau = input("Nhập một câu: ")


so_chu_hoa, so_chu_thuong = dem_chu_hoa_thuong(cau)
print("Số chữ hoa là:", so_chu_hoa)
print("Số chữ thường là:", so_chu_thuong)
