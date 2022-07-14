# import random
from random import randint


def roll_a_dice():
    return randint(1, 6)


total = 0
num = 10_000
for flips in range(num):
    total = total + roll_a_dice()
print(f"The avg number rolled is {total / num}.")
