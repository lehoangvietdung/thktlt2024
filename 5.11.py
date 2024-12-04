print("le hoang viet dung")
print("MSSV:235752021610104")
import numpy as np

data_type = [('name', 'S15'), ('class', int), ('height', float)]

students_details = [
    ('James', 5, 48.5),
    ('Nail', 6, 52.5),
    ('Paul', 5, 42.1),
    ('Pit', 5, 40.11)
]


students = np.array(students_details, dtype=data_type)


print("Original array:")
print(students)


sorted_students = np.sort(students, order=['class', 'height'])

print("Sorted array by class and height:")
print(sorted_students)
