print("LE HOANG VIET DUNG")
print("235752021610104")
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def circumference(self):
        return 2 * 3.14 * self.radius

a_circle = Circle(5)

print(f"Diện tích của hình tròn là: {a_circle.area()}")
print(f"Chu vi của hình tròn là: {a_circle.circumference()}")
