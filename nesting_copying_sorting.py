data = [(1, 2), (3, 4)]


def sum_of_tuple(item):
    num_one, num_two = item[0], item[1]
    return num_one + num_two


row_number = 1
for result in data:
    print(f"Row {row_number} sum: {sum_of_tuple(result)}")
    row_number += 1

numbers = [4, 3, 2, 1]
numbers_copied = numbers[:]
numbers_copied.sort()
print(numbers_copied)