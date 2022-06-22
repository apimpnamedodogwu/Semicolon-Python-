gross_sales = int(input("Enter amount of gross sales here or -1 to quit: "))
stipend = 200
percent = 0.09

while gross_sales != -1:
    sales_commission = stipend + (gross_sales * percent)
    print("Congratulations, you earned ", sales_commission, "last week.")

    gross_sales = int(input("Enter amount of gross sales here or -1 to quit: "))

