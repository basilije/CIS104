import msvcrt

def resetVariables():
    global key_pressed, first_text, second_text, entering_number, first_dot_is_entered, second_dot_is_entered, operation
    first_text = ""
    second_text = ""
    entering_number = 1
    first_dot_is_entered = False
    second_dot_is_entered = False
    operation = ""
    key_pressed = ""

resetVariables()
while key_pressed != 'X':
    key_pressed= str(msvcrt.getch().decode("utf-8")).upper()
    if (key_pressed >="0" and key_pressed <="9") or key_pressed == ".":
        if entering_number == 1:
            if key_pressed != "." or not(first_dot_is_entered):
                first_text += key_pressed
                if key_pressed != ".":
                    print(key_pressed, end="")
            if key_pressed == ".":
                if not(first_dot_is_entered):
                    print(key_pressed, end="")   
                    first_dot_is_entered = True
                      
        else:
            if key_pressed != "." or not(second_dot_is_entered):
                second_text += key_pressed
                if key_pressed != ".":
                    print(key_pressed, end="")
            if key_pressed == ".":
                if not(second_dot_is_entered):
                    print(key_pressed, end="")
                    second_dot_is_entered = True
               

    if key_pressed in ["+", "-", "*", "/", "^"] and entering_number == 1:
        operation = key_pressed
        entering_number = 2
        print(key_pressed, end="")

    if key_pressed == "I":
        if entering_number == 1:
            first_number = float(first_text)
            first_number = 0-first_number
            first_text = str(first_number)
            print("\n=", first_text, end="")

    if key_pressed == "C":
        resetVariables()
        print("\n=", end="")

    if key_pressed == "S":
        if entering_number == 1:
            memory_text = first_text
            print("\n=", first_text, end="")

    if key_pressed == "R":
        if entering_number == 1:
            first_text = ""
            second_text = ""
            entering_number = 1
            first_dot_is_entered = False
            second_dot_is_entered = False
            operation = ""
            key_pressed = ""
            
            first_text = memory_text
            print("\n=", first_text, end="")

    if key_pressed == "C":
        memory_text = ""
        print("\n")

    if key_pressed == chr(13):
        result = ""
        if operation == "+":
            result = float(first_text) + float(second_text)
        if operation == "-":
            result = float(first_text) + float(second_text)
        if operation == "*":
            result = float(first_text) * float(second_text)
        if operation == "/":
            result = float(first_text) / float(second_text)
        if operation == "^":
            result = float(first_text) ** float(second_text)
        if result != "":
            print("\n=", result, end="")

            entering_number = 1
            first_dot_is_entered = False
            second_dot_is_entered = False
            operation = ""
            key_pressed = ""            
            first_text = str(result)
            second_text = ""
