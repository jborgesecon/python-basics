# e89
# name and 2 grades of each student (use faker)
# list of lists (3 levels of lists)
# display a table (formated like the shopping list), studend and average grade
# allow user to type a student name (validate), return both grades. 

from faker import Faker
import numpy as np
import random as rd

fake = Faker(locale="pt-br")
class_1 = []

# generate 8 students
for i in range(8):
    student = []
    grades = []
    for ii in range(2):
        value = round(rd.normalvariate(6.8, 1.4), 2)
        grades.append(value)
    
    student.append(fake.first_name())
    student.append(grades)
    class_1.append(student)

names = []
for iii in class_1:
    names.append(iii[0])
    print(f'{iii[0]} -> {np.average(iii[1]):.2f}') # --> {iii[1]}')

print('\n')
while True:
    try:
        student_name = str(input('Type the student name -> '))
        if student_name.title() in names:
            break
        else:
            print(f'Student unavailable, choose one from {names}')
    except:
        print('type a valid answer')

student_name = student_name.capitalize()

# helper function
def find_name_index(name, lst):
    for index, sublist in enumerate(lst):
        if sublist[0] == name:
            return index
    return -1

chosen_grades = class_1[find_name_index(student_name, class_1)][1]
print(f'The grades of {student_name} were: {chosen_grades}')
