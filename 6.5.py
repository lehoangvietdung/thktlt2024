print("LE HOANG VIET DUNG")
print("235752021610104")
class ReversedString:
    def __init__(self, text):
        self.text = text

    def reverse_words(self):
        words = self.text.split()
        reversed_words = ' '.join(reversed(words))
        return reversed_words

input_string = 'hello .py'
reverser = ReversedString(input_string)

output_string = reverser.reverse_words()
print(f"Đầu ra: '{output_string}'")

