print("le hoang viet dung")
print("MSSV:235752021610104")
import tkinter as tk

root = tk.Tk()
root.title("Programming Language Selector")

v = tk.IntVar()
v.set(1)
languages = [
    ("Python", 1),
    ("Perl", 2),
    ("Java", 3),
    ("C++", 4),
    ("C", 5)
]

def ShowChoice():
    print(f"Selected language: {languages[v.get() - 1][0]}")

tk.Label(root, 
         text="Choose your favourite programming language:", 
         justify=tk.LEFT, 
         padx=20).pack()

for language, val in languages:
    tk.Radiobutton(root, 
                   text=language, 
                   padx=20, 
                   variable=v, 
                   command=ShowChoice, 
                   value=val).pack(anchor=tk.W)

root.mainloop()
