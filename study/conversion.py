user_input = input("Enter a number here: ")
double_result = int(user_input) * 10
print(double_result)


user_input = input("Enter a number here: ")
double_result = float(user_input) * 10.0
print(double_result)

number_of_phones = 3
print("I have " + str(number_of_phones) + " phones at home!")

user_input = input("Enter the first number here: ")
user_input_two = input("Enter the second number here: ")
result = float(user_input) * float(user_input_two)
print("The product of " + str(user_input) + " and " + str(user_input_two) + " is", result)

weight = 0.2
animal = "newt"
# print(str(weight) + " kg is the weight of the " + animal)
# print("{} kg is the weight of the {}".format(weight, animal))
print(f"{weight} kg is the weight of the {animal}")
