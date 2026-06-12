# Generating random values module

import random

for i in range(3):
    print(random.random())

for x in range(3):
    print(random.randint(10, 20))

members = ['John', 'Mary', 'Bob', 'Mosh']
leader = random.choice(members)
print(leader)


# Exercise: Roll dice

for i in range(2):
    dice_roll = random.randint(1, 6)
    print(dice_roll)


class Dice:
    def roll(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        return (first, second)


dice = Dice()
print(dice.roll())
