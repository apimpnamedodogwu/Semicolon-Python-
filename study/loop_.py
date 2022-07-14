# word = "Python"
# index = 0
# while index < len(word):
#     print(word[index])
#     index = index + 1
#
#
# for n in range(1, 4):
#     for j in range(4, 7):
#         print(f"n = {n} and j = {j}")


# for numbers in range(2, 10):
#     print(numbers)

# number = 2
# while number < 10:
#     print(number)
#     number = number + 1

def doubles(number) -> int:
    return number * number


print(doubles(2))

numb = 2
for num in range(0, 3):
    numb = doubles(numb)
    print(numb)
