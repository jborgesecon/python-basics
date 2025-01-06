from faker import Faker


fake = Faker(locale="pt-br")

class_1 = dict()

prompt = int(input('type the amount you want: '))
for i in range(prompt):
    name = fake.first_name()
    grade = float(input(f'type the average for {name}: '))
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