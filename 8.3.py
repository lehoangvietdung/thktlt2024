print("le hoang viet dung")
print("MSSV:235752021610104")
import turtle

t = turtle.Turtle()

t.speed(2)

colors = ["blue", "cyan", "red"]

for i in range(12):
    t.color(colors[i % 3]) 
    t.circle(50)        
    t.right(30)            

turtle.done()

