print("LE HOANG VIET DUNG")
print("235752021610104")
def sieve_of_eratosthenes(limit):
    is_prime = [True] * limit
    is_prime[0] = is_prime[1] = False  
    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, limit, i):
                is_prime[j] = False
    return tuple(i for i in range(limit) if is_prime[i])

P = sieve_of_eratosthenes(1_000_000)

print(f"Số lượng số nguyên tố nhỏ hơn 1 triệu: {len(P)}")
print(f"Các số nguyên tố nhỏ hơn 1 triệu (100 số đầu tiên): {P[:100]}")
