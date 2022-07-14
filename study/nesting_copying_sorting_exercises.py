data = ((1, 2), (3, 4))
sum_one = 0
sum_two = 0
for num in data:
    sum_one = sum(data[0])
    sum_two = sum(data[1])

print(f"Row 1 sum: {sum_one}")
print(f"Row 2 sum: {sum_two}")

numbers = [4, 3, 2, 1]
numbers_copy = numbers[:]
numbers.sort()
print(numbers)
