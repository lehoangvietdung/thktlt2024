print("LE HOANG VIET DUNG")
print("235752021610104")
import math

def calculate_distance(movements):
    x, y = 0, 0 
    
    for movement in movements:
        direction, steps = movement.split()
        steps = int(steps)
        
        if direction == "UP":
            y += steps
        elif direction == "DOWN":
            y -= steps
        elif direction == "LEFT":
            x -= steps
        elif direction == "RIGHT":
            x += steps
    
    distance = round(math.sqrt(x**2 + y**2))
    return distance

movements = ["UP 5", "DOWN 3", "LEFT 3", "RIGHT 3"]

distance = calculate_distance(movements)
print("Khoảng cách từ vị trí hiện tại đến vị trí đầu tiên:", distance)
