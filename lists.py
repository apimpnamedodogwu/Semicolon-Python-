print(list("Tola"))
colors = ["red", "orange", "magenta", "aqua", "blue"]
colors[1:4] = ["yellow", "green"]
colors.extend(["purple", "black", "grey"])
print(colors)

# A list comprehension is a shorthand for a for loop
numbers = (1, 2, 3, 4, 5)
squares = [num ** 2 for num in numbers]
print(squares)

# same result, different approach
squares_ = []
numbers_ = (2, 4, 6, 8, 10)
for a_num in numbers_:
    squares_.append(a_num ** 2)
print(squares_)

# review exercises
food = ["rice", "beans"]
food.append("broccoli")
food.extend(["bread", "pizza"])
print(food[:2])

meal = "eggs, fruit, orange juice"
breakfast = meal.split(", ")
print(breakfast)
print(len(breakfast))

lengths = [len(food_length) for food_length in breakfast]
print(lengths)