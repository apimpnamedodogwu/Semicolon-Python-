def invest(amount, rate, years):
    for year in range(1, years + 1):
        amount = amount * (1 + rate)
        print(f"Year{year}: ${round(amount, 2)}")


amount_ = int(input("Enter amount here: "))
rate_ = int(input("Enter rate here: "))
year_ = int(input("Enter the years(s) here: "))
(invest(amount_, rate_, year_))
