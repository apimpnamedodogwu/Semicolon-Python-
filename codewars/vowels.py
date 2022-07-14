def vowel_count(words):
    count = 0
    for letter in words:
        if letter in "aeiou":
            count += 1
    return count


print(vowel_count("bread"))
