import random


def toss():
    if random.randint(0, 1) == 0:
        return "Heads!"
    else:
        return "Tails!"


tails = 0
heads = 0
num_of_rolls = 10_000

for tosses in range(num_of_rolls):
    if toss() == "Heads!":
        heads = heads + 1
    else:
        tails = tails + 1

    while toss() == "Heads!":
        heads = heads + 1
    else:
        tails = tails + 1

    while toss() == "Tails!":
        tails = tails + 1
    else:
        heads = heads + 1

print(f"The average number of tosses per game is {(heads + tails) / num_of_rolls}.")
print(f"The average of heads to tails is {heads / tails}.")
