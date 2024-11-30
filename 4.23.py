print("LE HOANG VIET DUNG")
print("235752021610104")
def dem_chu_cai_va_chu_so(cau):
  """Đếm số chữ cái và chữ số trong một câu

  Args:
    cau: Câu cần đếm

  Returns:
    tuple: Một tuple chứa (số chữ cái, số chữ số)
  """

  so_chu_cai = 0  
  so_chu_so = 0   

  for ky_tu in cau: 
    if ky_tu.isalpha(): 
      so_chu_cai += 1 
    elif ky_tu.isdigit():  
      so_chu_so += 1 

  return so_chu_cai, so_chu_so  

cau = input("Nhập một câu: ")

so_chu_cai, so_chu_so = dem_chu_cai_va_chu_so(cau)
print("Số chữ cái là:", so_chu_cai)
print("Số chữ số là:", so_chu_so)
