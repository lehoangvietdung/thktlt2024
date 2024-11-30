print("LE HOANG VIET DUNG")
print("235752021610104")
def tim_so_chan_toan_chu_so(bat_dau, ket_thuc):
  """Tìm tất cả các số có toàn bộ chữ số là số chẵn trong một khoảng

  Args:
    bat_dau: Số bắt đầu của khoảng
    ket_thuc: Số kết thúc của khoảng

  Returns:
    Một chuỗi chứa các số tìm được, cách nhau bởi dấu phẩy
  """

  so_chan = []
  for num in range(bat_dau, ket_thuc + 1):
 
    chuoi_so = str(num)

    if all(int(chu_so) % 2 == 0 for chu_so in chuoi_so):
      so_chan.append(str(num))

  return ', '.join(so_chan)

ket_qua = tim_so_chan_toan_chu_so(1000, 3000)
print(ket_qua)
