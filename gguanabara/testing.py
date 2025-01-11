# task 92
# name, birth date as datetime, id
# add (with age) in a dict, if id != 0, add also startdate e salary
# calculate age and remaining time for retiring
import time
import random as rd
from dateutil.relativedelta import relativedelta
from faker import Faker
from datetime import datetime, timedelta


fake = Faker(locale='pt-br')

name = []
bdate = []
ctps = []
datestart = []
salary = []


for i in range(100):
    a = fake.first_name()
    b = fake.date_of_birth(minimum_age=18)
    c = rd.choices([fake.ssn(), None], weights=[1 - 0.35, 0.35])[0]
    
    if c != None:
        d = b + timedelta(days=rd.normalvariate(mu=8500, sigma=913))
        e = rd.uniform(35215.12, 789000.00)
    else:
        d = None
        e = None
    
    name.append(a)
    bdate.append(b)
    ctps.append(c)
    datestart.append(d)
    salary.append(e)

people = {
    'name': name,
    'birthdate': bdate,
    'CTPS': ctps,
    'datestart': datestart,
    'salary': salary
}

age_now = []
age_start = []
time_til_retire = []

now = datetime.now().date()

o1 = 0
for ii in people['birthdate']:
    age1 = (now - ii).days//365
    if people['CTPS'][o1] == None:
        age2 = None
        age3 = None
    else:
        age2 = (people['datestart'][o1] - ii).days //365
        age3 = ((ii + relativedelta(years=60)) - people['datestart'][o1]).days
    age_now.append(age1)
    age_start.append(age2)
    time_til_retire.append(age3)

    o1+=1

people['age_now'] = age_now
people['age_start'] = age_start
people['time_til_retire'] = time_til_retire

for i in range(len(people['name'])):
    for ii in people.keys():
        print(f'{ii} is -> {people[ii][i]}')
    print('\n')
    time.sleep(0.8)

