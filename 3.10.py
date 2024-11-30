print("LE HOANG VIET DUNG")
print("235752021610104")
import math

def Tinh(R):
  if R <= 0:
    return "Bán kính phải là số dương."
  else:
    chu_vi = 2 * math.pi * R
    dien_tich = math.pi * R**2
    return chu_vi, dien_tich
while True:
  try:
    R = float(input("Nhập bán kính hình tròn: "))
    break
  except ValueError:
    print("Vui lòng nhập một số thực dương.")
ket_qua = Tinh(R)
if isinstance(ket_qua, str):
  print(ket_qua)
else:
  print("Chu vi hình tròn:", ket_qua[0])
  print("Diện tích hình tròn:", ket_qua[1])
