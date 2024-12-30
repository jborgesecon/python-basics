# e89
# name and 2 grades of each student (use faker)
# list of lists (3 levels of lists)
# display a table (formated like the shopping list), studend and average grade
# allow user to type a student name (validate), return both grades. 

from faker import Faker
import numpy as np
import random as rd

fake = Faker()
class_1 = []

# generate 8 students
for i in range(8):
    student = []
    grades = []
    for ii in range(2):
        value = rd.uniform(2.00, 10.00)
        grades.append(value)
    
    student.append(fake.first_name())
    student.append(grades)
    class_1.append(student)

names = []
for iii in class_1:
    names.append(iii[0])
    print(f'{iii[0]} -> {np.average(iii[1]):.2f}')

print('\n')
while True:
    try:
        student_name = str(input('Type the student name -> '))
        if student_name in names:
            break
        else:
            print(f'Student unavailable, choose one from {names}')
    except:
        print('type a valid answer')

