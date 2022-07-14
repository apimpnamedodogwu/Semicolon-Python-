food = ["Rice", "Beans"]
food.append("Brocoli")

food.extend(["Bread", "Pizza"])

print(food[:2])
print(food[-1])

breakfast = []
breakfast_meal = "eggs, fruit, orange juice"
breakfast = breakfast_meal.split(",")
print(breakfast)
print(len(breakfast) == 3)

lengths = [len(value) for value in breakfast]
print(lengths)
