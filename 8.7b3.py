print("le hoang viet dung")
print("MSSV:235752021610104")
import tkinter as tk
import random

colours = ['Red', 'Blue', 'Green', 'Pink', 'Black', 'Yellow', 'Orange', 'White', 'Purple', 'Brown']
score = 0
y
timeleft = 120

def startGame(event):
    if timeleft == 120:

        countdown()

    nextColour()

def nextColour():
    global score
    global timeleft

    if timeleft > 0:

        e.focus_set()

        if e.get().lower() == colours[1].lower():
            score += 2
        else:
            score -= 1

        e.delete(0, tk.END)

        random.shuffle(colours)

        label.config(fg=str(colours[1]), text=str(colours[0]))

        scoreLabel.config(text="Score: " + str(score))

def countdown():
    global timeleft

    if timeleft > 0:

        timeleft -= 1

        timeLabel.config(text="Time left: " + str(timeleft))

        timeLabel.after(1000, countdown)

root = tk.Tk()

root.title("COLORGAME")

root.geometry("375x200")

instructions = tk.Label(root, text="Type in the colour of the words, and not the word text!", font=('Helvetica', 12))
instructions.pack()

scoreLabel = tk.Label(root, text="Press Enter to start", font=('Helvetica', 12))
scoreLabel.pack()

timeLabel = tk.Label(root, text="Time left: " + str(timeleft), font=('Helvetica', 12))
timeLabel.pack()

label = tk.Label(root, font=('Helvetica', 60))
label.pack()

e = tk.Entry(root)

root.bind('<Return>', startGame)
e.pack()

e.focus_set()

root.mainloop()
