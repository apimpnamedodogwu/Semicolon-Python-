import random

nouns = ["fossil", "horse", "aardvark", "judge", "chef", "mango",
         "extrovert", "gorilla"]
verbs = ["kicks", "jingles", "bounces", "slurps", "meows",
         "explodes", "curdles"]
adjectives = ["furry", "balding", "incredulous", "fragrant",
              "exuberant", "glistening"]
prepositions = ["against", "after", "into", "beneath", "upon",
                "for", "in", "like", "over", "within"]
adverbs = ["curiously", "extravagantly", "tantalizingly",
           "furiously", "sensuously"]


def make_a_poem() -> str:
    noun_one = random.choice(nouns)
    noun_two = random.choice(nouns)
    noun_three = random.choice(nouns)

    while noun_one == noun_two:
        noun_two = random.choice(nouns)
    while noun_one == noun_three or noun_two == noun_three:
        noun_three = random.choice(nouns)

    verb_one = random.choice(verbs)
    verb_two = random.choice(verbs)
    verb_three = random.choice(verbs)

    while verb_one == verb_two:
        verb_two = random.choice(verbs)
    while verb_one == verb_three or verb_two == verb_three:
        verb_three = random.choice(verbs)

    adj_one = random.choice(adjectives)
    adj_two = random.choice(adjectives)
    adj_three = random.choice(adjectives)

    while adj_one == adj_two:
        adj_two = random.choice(adjectives)
    while adj_one == adj_three or adj_two == adj_three:
        adj_three = random.choice(adjectives)

    prep_one = random.choice(prepositions)
    prep_two = random.choice(prepositions)

    while prep_one == prep_two:
        prep_two = random.choice(prepositions)

    adv = random.choice(adverbs)

    if "aeiou".find(adj_one[0]) != -1:
        preamble = "An"
    else:
        preamble = "A"

    poem = (
        f"{preamble} {adj_one} {noun_one}\n\n"
        f"{preamble} {adj_one} {noun_one} {verb_one} {prep_one} the {adj_two} {noun_two}\n"
        f"{adj_one}, the {noun_one} {verb_two}\n"
        f"the {noun_two} {verb_three} {prep_two} a {adj_three} {noun_three}"
    )

    return poem


a_poem = make_a_poem()
print(a_poem)
