import sys


# function that sets the current_value variable to the number entered as string
def setCurrentValue(num_str):
	global current_value	
	current_value = stringToNumber(num_str)


# function that returns the current_value variable
def getCurrentValue():
	global current_value
	return current_value	


# functions that prints the error text and beeps
def printAndBeepError():
	sys.stdout.write(' Error!\a')
	sys.stdout.flush()	


# function that do the basic operation with the current_value
def calculate(num_str, operator):
	global current_value
	result = ''  # set the result as empty string
	try:
		first_num = float(current_value)  # first operand is current_value
		second_num = float(num_str)  # get second operand from the function input parameter
		
		#  do the neccesary operation with two operands
		if operator == '+':
			result = first_num + second_num
		if operator == '*':
			result = first_num * second_num
		if operator == '-':
			result = first_num - second_num
		if operator == '/':
			result = first_num / second_num
		if operator == '^':
			result = first_num ** second_num
			
		if str(result) == 'inf':  # if something went wrong
			printAndBeepError()  # print and beep error
			result = ''  # set the result as empty string
		else:  # if everything looks ok
			setCurrentValue(result)  # set the current_value variable to the value of result
	except:  # if something went wrong
		printAndBeepError() # print and beep error
	return str(result)  # also return the result as string

	
# function that convert string to number with or without decimals if possible
def stringToNumber(s):
	res = ''
	try:
		res = float(s)  # return the number as float,
		if int(res) == res:  # but if the number looks as integer
			res = int(res)  # return it as integer
	except:  # if something went wrong 
		pass  # do nothing (return the empty string)
	return res


# function that put number to the memory_value variable
def putNumberToMemory(num):
	global memory_value
	memory_value = num


# function that return the value of the memory_value variable
def getNumberFromMemory():
	global memory_value
	return memory_value


# function that sets the memory_value variable to 0
def clearMemory():
	global memory_value
	memory_value = 0


# function that return the inverse of the number entered 
def inverseNumber(number_str):
	return stringToNumber(str(0. - stringToNumber(number_str)))

