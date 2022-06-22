user_input = float(input("Enter a number here: "))
result = round(user_input, 2)
print(f"{user_input} rounded to 2 decimal places is {result}.")

user_input = int(input("Enter a number here: "))
result = abs(user_input)
print(f"The absolute value of {user_input} is {result}.")

keyboard = float(input("Enter a number here: "))
keyboard_two = float(input("Enter a number here: "))
diff = keyboard - keyboard_two
result = diff.is_integer()
print(f"The difference between {keyboard} and {keyboard_two} is an integer? {result}!")

keyboard = float(input("Enter a number here: "))
keyboard_two = float(input("Enter a number here: "))
diff = keyboard - keyboard_two
result = diff.is_integer()
print(f"The difference between {keyboard} and {keyboard_two} is an integer? {result}!")