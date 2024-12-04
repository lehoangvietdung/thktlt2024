print("LE HOANG VIET DUNG")
print("235752021610104")
class Hinhchunhat(object):
    def __init__(self, dai, rong):
        self.chieu_dai = dai
        self.chieu_rong = rong

    def dien_tich(self):
        return self.chieu_dai * self.chieu_rong

hinh_chunhat = Hinhchunhat(4, 3)
print(f"Diện tích hình chữ nhật là: {hinh_chunhat.dien_tich()}")
