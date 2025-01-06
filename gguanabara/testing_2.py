# e90 -> store name and grade of each student, calculate status, return all
# e91 -> 
from faker import Faker


fake = Faker()
dic = dict()
for i in range(10):
    dic[fake.first_name()] = i + (4*i)

print(dic)