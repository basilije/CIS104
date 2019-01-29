coin_value = [1, 5, 10, 25, 50, 100]
coin_list = ["pennies", "nickels", "dimes", "quarters", "half dollars", "dollars"]
value_in_dollars = 0
values_list = []

for coin, value in zip(coin_list, coin_value):
    coin = int(input("How many " + coin + " you have? "))
    values_list.append(coin)
    value_in_dollars += coin*value/100

print()
for coin, value in zip(coin_list, values_list):
    str_to_print = "You have " + str(value) + " " + coin + "."
    if (value == 1):
        str_to_print = str_to_print.replace("s.", ".")
    print(str_to_print)
    
print("\nThe value of all of your coins is $%.2f.\n" % value_in_dollars)