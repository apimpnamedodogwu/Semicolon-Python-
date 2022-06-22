count_number = 1
number = 0
second_largest = 0

first_largest = number

while count_number <= 10:
    number = int(input("Enter number here: "))
    count_number += 1

    if number > first_largest:
        second_largest = first_largest
        first_largest = number

print(second_largest, first_largest)
