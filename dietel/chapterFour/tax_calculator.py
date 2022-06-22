citizen_counter = 1
tax_rate_one = 0.15
tax_rate_two = 0.20

while citizen_counter <= 3:
    earnings = int(input("Enter earnings here: "))
    citizen_counter = citizen_counter + 1
    if earnings <= 30000:
        tax = earnings * tax_rate_one
        print("Your tax is ", tax)

    if earnings > 30000:
        earnings = earnings - 30000
        taxV1 = earnings * tax_rate_two
        taxV2 = 30000 * tax_rate_one
        sum_of = taxV1 + taxV2
        print("Your total tax earning is ", sum_of)
