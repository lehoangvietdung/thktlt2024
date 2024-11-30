print("LE HOANG VIET DUNG")
print("235752021610104")
def calculate_balance(transactions):
    balance = 0

    for transaction in transactions:
        action, amount = transaction.split()
        amount = int(amount)
        
        if action == "D":
            balance += amount
        elif action == "W":
            balance -= amount

    return balance

transactions = []
print("Nhập các giao dịch (D 100 hoặc W 200), nhập 'STOP' để dừng nhập:")

while True:
    transaction = input()
    if transaction == "STOP":
        break
    transactions.append(transaction)

final_balance = calculate_balance(transactions)
print("Số tiền thực của tài khoản ngân hàng là:", final_balance)
