print("LE HOANG VIET DUNG")
print("235752021610104")
def sort_words(input_string):

    words = input_string.split()
    
    words.sort()
    
    return words

input_string = input("Nhập các từ tiếng Anh tách nhau bởi dấu cách: ")

sorted_words = sort_words(input_string)
print("Các từ theo thứ tự từ điển:", sorted_words)
