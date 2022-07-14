#
# try:
#     user_input = int(input("Enter a number here: "))
#     print(f"You entered {user_input}.")
# except ValueError:
#     print("Please, enter an integer!")


try:
    entry = input("Enter a word here: ")
    entry__ = int(input("Enter a number here: "))
    print(entry[entry__])

except IndexError:
    print("Index out of bounds!")
