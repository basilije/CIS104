from calc import calculator
first_text = ""
operations = ["+", "-", "*", "/", "^"]
while True:
    calculation_text = first_text + input("Enter your calculation: " + first_text)
    for o in operations:
        if len(calculation_text.split(o)) == 2:
            first_text = str(calculator(float(calculation_text.split(o)[0]), float(calculation_text.split(o)[1]), o))