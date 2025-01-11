import gguanabara.dataValid as dv
import pandas as pd
import numpy as np
import random as rd
from faker import Faker
import time



def generic_print():
    print('ok')

# # ep 16

# e72
def number_names():
    nnames = (
        'Zero', 'One', 'Two', 'Three',
        'Four', 'Five', 'Six', 'Seven', 
        'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve',
        'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen',
        'Seventeen', 'Eighteen', 'Nineteen', 'Twenty'
    )
    while True:
        chosen_num = dv.intValid(input('Enter a number between 0 and 20: '))
        if 0 <= chosen_num <= 20:
            break
        else:
            print('Please enter a number between 0 and 20.')
    print(f'You chose number {nnames[chosen_num]}!')

# e73
def standings():
    csv = 'gguanabara/datasets/Standings.csv'
    df = pd.read_csv(csv)
    
    dv.sepper('Top 5:', ' ')
    print('\n')
    top_5 = df['TEAM'].head(5).tolist()
    o = 1
    for i in top_5:
        print(f'{o}° - {i}')
        o += 1
    
    print('\n')
    dv.sepper('Last 4:', ' ')
    print('\n')
    last_4 = top_5 = df['TEAM'].tail(5).tolist()
    last_4 = reversed(last_4)
    o = len(df['TEAM']) + 4
    for i in last_4:
        print(f'{o - 4}° - {i}')
        o -= 1
    
    print('\n')
    dv.sepper('Alphabetically: ', ' ')
    print('\n')
    s_standings = sorted(df['TEAM'].tolist())
    print(s_standings)

    print('\n')
    dv.sepper('Choose your Team!', ' ')
    print('\n')
    standings2 = df['TEAM'].tolist()
    while True:
        usr_team = input('Desired Team: ').upper().strip()
        if usr_team in standings2:
            break
        else:
            print('Type an available team!')
    position = standings2.index(usr_team)
    print(f'The {usr_team} are in position {position + 1}°')

    
# e74
def fv_randNums():
    m_tp = (
        rd.randint(0,9),
        rd.randint(0,9),
        rd.randint(0,9),
        rd.randint(0,9),
        rd.randint(0,9)
    )
    # m_tp.pop()
    print(m_tp)
    print(f'The highest number is {max(m_tp)}')
    print(f'The lowest number is {min(m_tp)}')


# e75
def tuple_values():
    m_tp = (
        dv.intValid(input('Enter a number: ')),
        dv.intValid(input('Enter a number: ')),
        dv.intValid(input('Enter a number: ')),
        dv.intValid(input('Enter a number: ')),
        dv.intValid(input('Enter a number: '))
    )
    print(f'The number 9 appeared {m_tp.count(9)} times.')
    if 3 in m_tp:
        print(f'The number 3 appeared in position {m_tp.index(3) + 1}')
    else:
        print('The number 3 did not appear.')
    print('The even numbers are: ', end='')
    for i in m_tp:
        if i % 2 == 0:
            print(i, end=' ')
    print('\n')

# e76
def shopping_list():
    m_list = (
        'Pencil', 1.75,
        'Eraser', 2.00,
        'Notebook', 15.90,
        'Pencilcase', 25.00,
        'Ruler', 4.20,
        'Compass', 9.99,
        'Backpack', 120.32,
        'Pen', 22.30,
        'Book', 34.90
    )
    print(38* '-')
    msg = 'SHOPPING LIST'
    print(f'{msg:^38}')
    print(38* '-')
    print('\n')
    for i in range(0, len(m_list), 2):
        print(f'{m_list[i]:.<30}$ {m_list[i + 1]:>7.2f}')
    print(38* '-')
    print('\n')

# e77
def tuple_vowels():
    m_tp = (
        "application", 
        "revolutionary", 
        "consideration", 
        "misunderstanding", 
        "organization", 
        "preoccupation", 
        "interpretation", 
        "exaggeration", 
        "circumstances", 
        "representation", 
        "collaboration", 
        "multiplication"
    )
    vowels = ('a', 'e', 'i', 'o', 'u')
    print('\n')

    for i in range(len(m_tp)):
        print(f'In the word {m_tp[i].upper()} the vowels are: ', end='')
        for o in m_tp[i]:
            if o in vowels:
                print(f'{o} ', end='')
        print('')

# # Episode 17

# e78
def list_num_order():
    m_list = list()
    for i in range(5):
        value = dv.intValid(input(f'Enter a number for position {i + 1}°: '))
        m_list.append(value)
    
    print('-=' * 30)
    print('\n')

    mx = max(m_list)
    mn = min(m_list)
    
    print(f'You type the values {m_list}')
    print(f'The highest value was {mx}')
    print(f'The lowest value was {mn}')
    
    mx_positions = [i + 1 for i, x in enumerate(m_list) if x == mx]
    mn_positions = [i + 1 for i, x in enumerate(m_list) if x == mn]

    print(f'The value {mx} appeared in positions: ', end='')
    print(', '.join(f'{pos}°' for pos in mx_positions))
    print(f'The value {mn} appeared in positions: ', end='')
    print(', '.join(f'{pos}°' for pos in mn_positions))
    print('')
    return

# e79
def unique_ordered_list():
    m_list = list()
    while True:
        num = dv.intValid(input('Enter a number:'))
        if num in m_list:
            print(f"{num} is already on the list, won't be added")
        else:
            inserted = False
            for i in range(len(m_list)):
                if num < m_list[i]:
                    m_list.insert(i, num)
                    inserted = True
                    break
            if not inserted:
                m_list.append(num)
        ans2 = dv.yn_valid(input('Would you like to try again? [y/n]: '))
        if ans2 == 'n':
            break
    print('\n')
    print(m_list)
    print('\n')
    return

# e80
# same as 79

def unlimited_list():
    m_list = list()
    length = dv.intValid(input('How many number do you want in the list: '))
    while True:
        if len(m_list) == length:
            # print(m_list)
            break
        num = rd.randint(1, length)
        if not m_list:
            m_list.append(num)
        elif num in m_list:
            print(f'{num} is already on the list!')
        else:
            for i in range(len(m_list)):
                if num < m_list[i]:
                    m_list.insert(i, num)
                    print(m_list)
                    break
                elif num > m_list[-1]:
                    m_list.append(num)
                    break
                else:
                    print(m_list)
                    dv.sepper(str(num), '*')
        print(m_list)
    print(len(m_list))
    return

# e81
def ordered_list_i():
    # how many number do you want to type?:
    # print resverse sort (both methods, both prints)
    # if 5 in list, print position, else print 'not in the list'
    m_list = list()
    length = dv.intValid(input('How many number do you want in the list: '))
    for i in range(length):
        m_list.append(rd.randint(0, 100))
    sorted(m_list, reverse=True)
    print(m_list )
    return

# e82
def even_odd_list():
    m_list = list()
    length = dv.intValid(input('How long do you want your list to be: '))
    odd_list = list()
    even_list = list()
    for i in range(length):
        usr = dv.intValid(input(f'type the {i + 1}° value: '))
        m_list.append(usr)
        if usr % 2 == 0:
            even_list.append(usr)
        else:
            odd_list.append(usr)

    m_list = sorted(m_list)
    even_list = sorted(even_list)
    odd_list = sorted(odd_list)

    print(f'The values you types were: {m_list}')
    print(f'The even numbers were => {even_list}')
    print(f'The odds numbers were => {odd_list}')
    return


# e83
def checkBalanced():
    obj = input('Type an expression with parenthese: ')
    par = ('(', ')')

    stack = list()
    balanced = True

    for i in obj:
        if i == par[0]:
            stack.append(i)
        elif i == par[1]:
            if not stack:
                balanced = False
                break
            else:
                stack.pop()
    
    if not stack and balanced:
        print('Balanced!')
    else:
        print('Unbalanced!')
    
    return

# # Episode 18 (list of lists)

# e84
def weigthCheck():
    people = []
    length = dv.intValid(input('Type the amount of people to be added: '))

    for i in range(length):
        while True:
            u_name = str(input(f'Input the name of the {i + 1}° person: '))
            if len(u_name) >= 2:
                break
            else:
                print('Type a name with at least 2 characters')
        u_weigth = dv.floatValid(input(f'Type the weigth of the {i + 1}° person: '))

        to_add = [u_name, u_weigth]
        people.append(to_add)

    people.sort(key=lambda x: x[1])
    quant = len(people)
    heaviest = [people[-1], people[-2]]
    lightest =[people[0], people[1]]

    print('\n', 30 * '-')
    print(f'There are {quant} people in the list', '\n')
    print('The heaviest people are: \n')
    for ii in heaviest:
        print(f'-> {ii[0]}: {ii[1]}kg')
    print('\n')
    print('The lightest people are: \n')
    for iii in lightest:
        print(f'-> {iii[0]}: {iii[1]}kg')

    return

# e85
def even_odd_2():
    list_1 = [[],[]]
    for i in range(7):
        value = dv.intValid(input(f'Type the {i + 1}° value: '))
        if value % 2 == 0: # Even, list_1[0]
            call = 0
        else: # Odd, list_1[1]
            call = 1
        
        if not list_1[call]:
            list_1[call].append(value)
        else:
            for index, v in enumerate(list_1[call]):
                if value < v:
                    list_1[call].insert(index, value)
                    break
            else:
                list_1[call].append(value)
    
    print('\n')
    print('The Even numbers are: ', list_1[0])
    print('The Odds number are: ', list_1[1])

    return

# e86/ e87
def tbt_matrix():
    rows = 3
    cols = 3

    matrix = list()
    sep = [
        [], # evens
        []  # odds
    ]

    for row in range(rows):
        n_row = []
        matrix.append(n_row)
        for col in range(cols):
            value1 = dv.intValid(input(f'Type a number for position [{row}, {col}] -> '))
            matrix[row].append(value1)

    print('\n')
    # print(15 * '=-',)
    msg = 'MATRIX'
    print(f'{msg:-^30}', '\n')
    # print(15 * '=-', '\n')
    for row in range(rows):
        for col in range(cols):
            print(f'[ {matrix[row][col]} ] ', end='')
        print('')
    
    # print(15 * '=-', '\n')
    for row in range(rows):
        for col in range(cols):
            result = matrix[row][col] % 2
            if result == 0: # even
                call = 0
            else:   # odd
                call = 1
            
            value = matrix[row][col]
            position = str([row, col])
            n_sep = [value, position]
            sep[call].append(n_sep)

    print('\n')

    print(f'The evens are: ')
    print('\n')
    total_evens = 0
    for evens in sep[0]:
        print(f'value: {evens[0]}; position: {evens[1]}')
        total_evens+=evens[0]
    print('\n')
    print(f'Sum of Evens = {total_evens}')
    print('\n')
    print(f'row 1 = {matrix[0]}')
    print(f'Sum of row 1 = {sum(matrix[0])}')
    print('\n')

    row3 = 0
    print(f'col 3 = ', end='')
    for i in range(len(matrix)):
        print(f'[{matrix[i][2]}] ', end='')
        row3+=matrix[i][2]
    print('')
    print(f'Sum of colum 3 = {row3}')
    print('\n')

    return


# e88
def lottery_games():
    games = []
    print('\n')
    dv.sepper('LOTTERY GAME', '-')
    print('\n')
    amount = dv.intValid(input('How many games do you want to generate: '))

    for i in range(amount):
        n_game = sorted(rd.sample(range(1,61), k=6))
        games.append(n_game)

    print('\n')
    dv.sepper('GAMES', '-')
    for ii in games:
        print(f'{games.index(ii) + 1}° game -> ', ii)
        time.sleep(0.5)
    print('\n')

    return


# e89
def grades():
    fake = Faker(locale="pt-br")
    class_1 = []

    # generating list of students
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
        print(f'{iii[0]} -> {np.average(iii[1]):.2f}')#  {iii[1]}')     # for some reason, when I don't print both grades, np.average() return a wrong value

    print('\n')
    while True:
        try:
            student_name = str(input('Type the student name -> '))
            if student_name.title() in names:
                break
            else:
                print(f'Student name not listed. choose one from {names}')
        except Exception as e:
            print(f'Type a valid answer: {e}')
    
    student_name.title()

    # helper function
    def find_name_index(name, lst):
        for index, sublist in enumerate(lst):
            if sublist[0] == name:
                return index
        return -1
    
    chosen_grades = class_1[find_name_index(student_name, class_1)][1]
    print(f'The grades of {student_name} were: {chosen_grades}')

    return

# # Episode 19

# e90
def grades_2():
    fake = Faker(locale='pt-br')
    class_1 = dict()

    length = dv.intValid(input('How many students in this class -> '))
    for i in range(length):
        name = fake.first_name()
        grade = dv.floatValid(input(f'Type the grade for {name}: '))
        class_1[name] = {
            'grade': grade,
            'status': 'PASSED' if grade >= 7 else 'FAILED'
        }

    print('\n')
    for ii in class_1:
        print(ii)
        for iii in class_1[ii]:
            print(f'    {iii}: {class_1[ii][iii]}')
        print('\n')

    return


# e91
def dice():
    fake = Faker(locale='pt-br')
    players = {}
    for i in range(4):
        new_player = fake.first_name()
        players[new_player] = rd.randint(1, 6)

    for ii in players:
        print(ii, ': ', players[ii])

    print('\n')
    players = dict(sorted(players.items(), key=lambda x: x[1], reverse=True))
    print('\n')

    o = i
    for k, v in players.items():
        print(f'{o}° is {k} with {v}')
        time.sleep(1)
        o += 1


# e92
