print("LE HOANG VIET DUNG")
print("235752021610104")
def benefit(t, n, k):


    t = t / 100
    
    final_amount = n * ((1 + t) ** k)
    
    return final_amount

t = float(input("Nhập lãi suất tiết kiệm (%/tháng): "))
n = float(input("Nhập số vốn ban đầu: "))
k = int(input("Nhập số tháng gửi: "))

result = benefit(t, n, k)
print("Số tiền nhận được sau", k, "tháng là:", round(result, 2))
