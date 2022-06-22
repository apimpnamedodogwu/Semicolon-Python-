acct_number = int(input("Enter account number or -1 to quit: "))

while acct_number != -1:

    starting_balance = int(input("Enter starting balance here: "))
    debit = int(input("Total of all items charged: "))
    credit = int(input("Total of all credits applied: "))
    credit_limit = int(input("Allowed credit limit: "))

    newBalance = (starting_balance + debit - credit)
    print("Your new balance is ", newBalance)
    if newBalance > credit_limit:
        print("You have exceeded your credit limit.")
    else:
        print("Your are still withing your credit limit.")

    acct_number = int(input("Enter account number or -1 to quit: "))
