pennies = int(input("How many pennies do you have? "))  # enter number of pennies
nickels = int(input("How many nickels do you have? "))  # enter number of nickels
dimes = int(input("How many dimesdo you have? "))  # enter number of dimes
quarters = int(input("How many quarters do you have? "))  # enter number of quarters
half_dollars = int(input("How many half dollars do you have? "))  # enter number of half dollars
dollars = int(input("How many dollars do you have? "))  # enter number of dollars

# print number of pennies
if pennies == 1:
    print("\nYou have %i pennie." % pennies)
else:
    print("\nYou have %i pennies." % pennies)

# print number of nickels
if nickels == 1:
    print("You have %i nickel." % nickels)
else:
    print("You have %i nickels." % nickels)

# print number of dimes
if dimes == 1:
    print("You have %i dime." % dimes)
else:
    print("You have %i dimes." % dimes)

# print number of quarters
if quarters == 1:
    print("You have %i quarter." % quarters)
else:
    print("You have %i quarters." % quarters)

# print number of half dollars
if half_dollars == 1:
    print("You have %i half_dollar." % half_dollars)
else:
    print("You have %i half_dollars." % half_dollars)  

# print number of dollars
if dollars == 1:
    print("You have %i dollar." % dollars)
else:
    print("You have %i dollars." % dollars) 

  
# calculate value of all coins
value_of_all_coins = pennies * 0.01 + nickels * 0.05 + dimes * 0.1 + quarters * 0.25 + 0.5 * half_dollars + dollars

# printing value of all coins
print("\nThe value of all of your coins is $%.2f.\n" % value_of_all_coins)
