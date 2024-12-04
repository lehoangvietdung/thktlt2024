print("le hoang viet dung")
print("MSSV:235752021610104")
import tkinter as tk
from tkinter import messagebox

def show_selected():
    selected = var.get()
    messagebox.showinfo("Thông báo", f"Bạn đã chọn: {selected}")

root = tk.Tk()
root.title("Radio Button Form")

var = tk.IntVar()
var.set(1) 

radio1 = tk.Radiobutton(root, text="1", variable=var, value=1)
radio1.grid(row=0, column=0, padx=10, pady=5)

radio2 = tk.Radiobutton(root, text="2", variable=var, value=2)
radio2.grid(row=1, column=0, padx=10, pady=5)

radio3 = tk.Radiobutton(root, text="3", variable=var, value=3)
radio3.grid(row=2, column=0, padx=10, pady=5)

button = tk.Button(root, text="Click Me", command=show_selected)
button.grid(row=3, column=0, padx=10, pady=5)
h
root.mainloop()
