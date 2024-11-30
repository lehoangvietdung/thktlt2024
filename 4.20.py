print("LE HOANG VIET DUNG")
print("235752021610104")
def print_pascals_triangle(n):
    triangle = []
    
    for i in range(n):
        row = [1] * (i + 1) 
        for j in range(1, i): 
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)
    
    for row in triangle:
        print(" ".join(map(str, row)))  

n = int(input("Nhập số nguyên n: "))

print_pascals_triangle(n)

