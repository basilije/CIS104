pennies = int(input("Enter number of pennies: "))  # enter number of pennies
nickels = int(input("Enter number of nickels: "))  # enter number of nickels
dimes = int(input("Enter number of dimes: "))  # enter number of dimes
quarters = int(input("Enter number of quarters: "))  # enter number of quarters
half_dollars = int(input("Enter number of half dollars: "))  # enter number of half dollars
dollars = int(input("Enter number of dollars: "))  # enter number of dollars

# calculate value of all coins
value_of_all_coins = pennies * 0.01 + nickels * 0.05 + dimes * 0.1 + quarters * 0.25 + 0.5 * half_dollars + dollars

# printing value of all coins
print("The value of all of your coins is $%.2f." % value_of_all_coins)
