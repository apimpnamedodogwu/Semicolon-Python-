amount_of_gallons = int(input("Enter amount of gallons here or -1 to terminate: "))
sum_of = 0

while amount_of_gallons != -1:
    miles_driven = int(input("Enter miles driven here: "))

    miles_per_gallon = miles_driven / amount_of_gallons
    print("The miles per gallon for this trip is", miles_per_gallon)

    sum_of = sum_of + miles_per_gallon
    print("The sum of the various MPG is", sum_of)

    amount_of_gallons = int(input("Enter amount of gallons here or -1 to terminate: "))
