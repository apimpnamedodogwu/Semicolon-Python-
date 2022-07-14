user_input = int(input("Enter a number here: "))
for number in range(1, user_input + 1):
    if user_input % number == 0:
        print(f"{number} is a factor of {user_input}")


for letter in range(3):
    user = input("A letter: ")
    if user == "q" or user == "Q":
        break
    print("Try again!")
else:
    print("Oops, your chance has run out!")

for num in range(3, 51):
    if num % 3 == 0:
        continue
    else:
        print(f"{num} is not a multiple of 3.")
