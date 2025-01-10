import random as rd
from faker import Faker


# 4 players
# dice
# store player, value in dict
# sort dict
# print Champion (highest dice value)

fake = Faker(locale='pt-br')
players = dict()
for i in range(4):
    new_player = fake.first_name()
    players[new_player] = rd.randint(1,6)

for ii in players:
    print(ii, players[ii])


print('\n')
players = dict(sorted(players.items(), key=lambda x: x[1], reverse=True))
for k, v in players.items():
    print(k, ' -> ', v)

