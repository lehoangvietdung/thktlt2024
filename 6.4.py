print("LE HOANG VIET DUNG")
print("235752021610104")
class RomanToInteger:
    def __init__(self):
        self.roman_numerals = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
    def roman_to_int(self, s):
        total = 0
        prev_value = 0
        for char in reversed(s):
            value = self.roman_numerals[char]
            if value < prev_value:
                total -= value
            else:
                total += value
            prev_value = value
        return total
er
converter = RomanToInteger()

roman_number = input("Nhập số La Mã: ")

integer_value = converter.roman_to_int(roman_number)
print(f"Số nguyên tương ứng với số La Mã {roman_number} là: {integer_value}")
