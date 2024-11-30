print("LE HOANG VIET DUNG")
print("235752021610104")
def fibonacci_less_than(n):
    fib_list = []
    a, b = 0, 1
    while a < n:
        fib_list.append(a)
        a, b = b, a + b
    return fib_list

n = int(input("Nhập số nguyên n: "))

fibonacci_numbers = fibonacci_less_than(n)

print(f"Các số Fibonacci nhỏ hơn {n}:")
print(fibonacci_numbers)
