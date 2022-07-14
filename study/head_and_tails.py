import random


# def coin_flip():
#     if random.randint(0, 1) == 0:
#         return "Heads"
#     else:
#         return "Tails"
#
#
heads_tally = 0
tails_tally = 0
#
# for a_flip in range(10_000):
#     if coin_flip() == "Heads":
#         heads_tally = heads_tally + 1
#     else:
#         tails_tally = tails_tally + 1
#
# ratio = heads_tally / tails_tally
# print(f"The ratio of heads to tail is {ratio}.")


def unfair_coin_flip(prob_of_tails):
    if random.random() < prob_of_tails:
        return "Tails"
    else:
        return "Heads"


for a_flip in range(10_000):
    if unfair_coin_flip(.7) == "Heads":
        heads_tally = heads_tally + 1
    else:
        tails_tally = tails_tally + 1

ratio = heads_tally / tails_tally
print(f"The ratio of heads to tail is {ratio}.")
