print("LE HOANG VIET DUNG")
print("235752021610104")
def remove_digits(input_string):

    result = ''.join([char for char in input_string if not char.isdigit()])
    return result

input_string = input("Nhập một chuỗi: ")


new_string = remove_digits(input_string)
print("Chuỗi mới không chứa chữ số:", new_string)
