import tkinter as tk

root = tk.Tk()

root.title("Cửa sổ đồ họa Tkinter")

root.geometry("400x300")

label = tk.Label(root, text="Chào mừng đến với Tkinter!")
label.pack(pady=20)

def on_button_click():
    print("Bạn đã nhấn vào nút!")

button = tk.Button(root, text="Nhấn vào đây", command=on_button_click)
button.pack(pady=10)

root.mainloop()
