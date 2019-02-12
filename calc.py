def calculator(first_num, second_num, operator):
    if operator == "+":
        result = first_num + second_num
    if operator == "*":
        result = first_num * second_num
    if operator == "-":
        result = first_num - second_num
    if operator == "/":
        result = first_num / second_num
    if operator == "^":
        result = pow(first_num, second_num)
    return result