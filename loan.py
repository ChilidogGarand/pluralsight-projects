
# Get loan details
money_owed = float(input("How many smackeroos do you owe?\n"))
apr = float(input("What kinda interest did the loan shark give you?\n"))
payment = float(input("How much can you pay every month without your kids starving?\n"))
months = int(input("How many months do you think they'll let you keep your thumbs?\n"))

# Divide APR / 100 to get a decimal, then by 12 to get the monthly rate
monthly_rate = apr/100/12

for i in range(months):
    # Add in the interest
    interest_paid = money_owed * monthly_rate
    money_owed = money_owed + interest_paid

    if (money_owed - payment < 0):
        print("The last payment is", money_owed)
        print("You paid off the load in", i+1, "months")
        break
    
    # Make a payment
    money_owed = money_owed - payment

    # Print results
    print("Paid", payment, "of which", interest_paid, "was interest.", end=' ')
    print("Now I owe", money_owed)
