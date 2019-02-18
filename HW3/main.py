import sys
import msvcrt
from calculator import *


# reset the processing variables to the default value
def resetVariables():
	global first_number_str, second_number_str, current_number, current_operation
	first_number_str = ''  # variable that will keep the first number as string
	second_number_str = ''  # variable thar will keep the second number as string
	current_number = 1  # variable that will keep current number in use (1st or 2nd)
	current_operation = ''  # varibale that will keep the current operation


# print anything without new row at the end
def printWithoutNewRowAtTheEnd(anything):
	try:
		str_anything = str(anything)
	except:
		str_anything = ''
		
	sys.stdout.write(str_anything)
	sys.stdout.flush()

	
# clear the current printing row
def cleanRow():
	printWithoutNewRowAtTheEnd('\r                                 \r')


key_pressed = ''  # nothing is pressed at the begining
row_beggining_symbol = '> '  # symbol that would be printed at the beggining of print row
esc_char = '\x1b'  # escape character
enter_char = chr(13)  # enter character
resetVariables()  # reset all variables
setCurrentValue(0)  # set the curent value to zero

# print the short manual
printWithoutNewRowAtTheEnd('        CALCULATOR:\n\
 S - store number to the memory\n\
 R - read number from the memory\n\
 M - clear the memory\n\
 I - inverse the curent number\n\
 C - clear the calculator\n\
 Enter - do the calculation\n\
 Esc - exit\n\
 Allowed operations: +  -  *  /  ^ \n\n')

printWithoutNewRowAtTheEnd(row_beggining_symbol)  # print the beggining character

while key_pressed != esc_char:  # repeat until ESC is pressed
	key_pressed = str(msvcrt.getwch().upper())  # get the pressed key and convert it to the uppercase

	if key_pressed in ['1','2','3','4','5','6','7','8','9','0','.']:  # if the digit is pressed
		if current_number == 1:  # if the user enters the first number
			if key_pressed == '.' and first_number_str == '':  # if the first key in first number pressed is '.'
				first_number_str = '0'  # set the first number to 0
			if key_pressed != '.'  or len(first_number_str.split('.')) < 2:  # if the digit is pressed or '.' in the first number is first time pressed
				first_number_str += key_pressed  # append the key pressed
				printWithoutNewRowAtTheEnd(key_pressed)  # print the key pressed
				setCurrentValue(first_number_str)  # set the current_value variable to the first number that is currently entered  
		else:  # if the user enter the number after of the operation symbol
			if key_pressed == '.' and second_number_str == '':  # if the first key in the second number pressed is '.'
				second_number_str = '0'  # set the second number to 0
			if key_pressed != '.' or len(second_number_str.split('.')) < 2:  # if the digit is pressed or '.' in the second number is first time pressed		
				second_number_str += key_pressed  # append the key pressed
				printWithoutNewRowAtTheEnd(key_pressed)  # print the key pressed

	if key_pressed in ['+','-','*','/','^']:  # if some of the operations keys are pressed
		if current_number == 1:  # if the current number is the first one
			if first_number_str != '':	# if the first number entered is not an empty string
				printWithoutNewRowAtTheEnd(' ' + key_pressed + ' ')  # print the first number, space symbol, operation symbol and space symbol
				current_number = 2  # switch to enter the second number
		else:  # if the current number is second one
			if second_number_str != '':  # if the second number entered is not an empty string
				result = calculate(second_number_str, current_operation)  # calculate the result with current_value and the second muber
				resetVariables()  # reset the processing variables to the default values
				printWithoutNewRowAtTheEnd('\n' + row_beggining_symbol + str(stringToNumber(result))+ ' ' + key_pressed + ' ')  # print the row as first number and operation with spaces
				first_number_str = result  # put the calculated result to the first number
				current_number = 2  # switch to enter the second number
				
		current_operation = key_pressed  # sets the operation key pressed as the current operation
	
	if key_pressed == enter_char:  # if the enter key is pressed
		if current_number == 2:  # if the user has entered the second number
			if second_number_str == '':  #  if the second number entered is not an empty string
				result = calculate(first_number_str, current_operation)  # calculate the result with current_value and the first number
			else:
				result = calculate(second_number_str, current_operation)  # calculate the result with current_value and the second number
			resetVariables()  # reset the processing variables to the default values
			printWithoutNewRowAtTheEnd('\n' + row_beggining_symbol + str(stringToNumber(result)))  # print the row as first number and operation with spaces
			first_number_str = result  # put the calculated result to the first number
			current_number = 1  # switch to enter the first number
	
	if key_pressed == 'C':  # if the key for clearing the calculator is pressed		
		resetVariables()  # reset the processing variables to the default values
		printWithoutNewRowAtTheEnd('\n' + row_beggining_symbol)  # print the beggining character
		setCurrentValue(0)  # set the curent value to zero
	
	if key_pressed == 'I':  # if the key fot inverting the number is pressed	
		if current_number == 1:  # if the current number is the first one
			first_number_str = str(inverseNumber(first_number_str))  # invert the first number and put it to the first number string variable
			setCurrentValue(first_number_str)  # set the current_value variable to the first number entered
			cleanRow()  # clear the already printed row
			printWithoutNewRowAtTheEnd(row_beggining_symbol + first_number_str)  # print the row with the new first number
		else:
			if second_number_str != '':  # if the second number entered is not an empty string
				first_number_str = str(stringToNumber(first_number_str))  # re-check and convert the first number back
				setCurrentValue(first_number_str)  # set the current_value variable to the first number entered
				second_number_str = str(inverseNumber(second_number_str))  # invert the second number and put it to the second number string variable
				cleanRow()   # clear the already printed row
				printWithoutNewRowAtTheEnd('\r' + row_beggining_symbol + first_number_str + ' ' + current_operation + ' ' + second_number_str)  # print the row with the re-checked first number, current operation and inverted second number

	if key_pressed == 'S':  # if the key for storing the value to memory is pressed
		putNumberToMemory(getCurrentValue())  # get the current_value variable and put it to the memory_value variable

	if key_pressed == 'R':  # if the key for reading the memory value is pressed
		if current_number == 1:  # if the current number is the first one
			first_number_str = str(getNumberFromMemory())  # get the number from the memory and put it converted to the first number string
			setCurrentValue(first_number_str)  # set the current_value variable to the value of first number
			cleanRow()   # clear the already printed row
			printWithoutNewRowAtTheEnd(row_beggining_symbol + first_number_str)  # print the row with the new first number		
		else:  # if the current number is the second one
			second_number_str = str(getNumberFromMemory())  # get the number from the memory and put it converted to the second number string
			cleanRow()   # clear the already printed row
			printWithoutNewRowAtTheEnd('\r' + row_beggining_symbol + first_number_str + ' ' + current_operation + ' ' + second_number_str)  # print the row with the re-checked first number, current operation and inverted second number
	
	if key_pressed == 'M':  # if the key for clearing the memory is pressed	
		clearMemory()  # set the memoy value to zero


