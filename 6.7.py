print("LE HOANG VIET DUNG")
print("235752021610104")
class ATM:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance

    def check_balance(self):
        print(f"Số dư hiện tại của bạn là: {self.balance} VND")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Bạn đã gửi {amount} VND. Số dư mới là: {self.balance} VND")
        else:
            print("Số tiền gửi phải lớn hơn 0.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Bạn đã rút {amount} VND. Số dư còn lại là: {self.balance} VND")
        else:
            print("Số tiền rút không hợp lệ hoặc vượt quá số dư hiện tại.")

    def menu(self):
        while True:
            print("\n=== HỆ THỐNG ATM ===")
            print("1. Kiểm tra số dư")
            print("2. Gửi tiền")
            print("3. Rút tiền")
            print("4. Thoát")
            choice = int(input("Chọn chức năng (1-4): "))

            if choice == 1:
                self.check_balance()
            elif choice == 2:
                amount = int(input("Nhập số tiền gửi: "))
                self.deposit(amount)
            elif choice == 3:
                amount = int(input("Nhập số tiền rút: "))
                self.withdraw(amount)
            elif choice == 4:
                print("Cảm ơn bạn đã sử dụng dịch vụ ATM!")
                break
            else:
                print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")

atm = ATM(100000)
atm.menu()
