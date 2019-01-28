first_name = input("What's your first name? ")  # get a first name
last_name = input("What's your last name? ")  # get a last name
age = int(input("Your age? ")) # get an age
confidence = int(input("Your confidence in programmers (0-100)? "))  # get a confidence

# do a neccessary calculations
dog_age = age * 7
confidence_percent = float(confidence / 100)

# print first and last name, age and dog age
print("Hello %s %s, nice to meet you! You might be %i in human years, but in dog years you are %i." % (first_name, last_name, age, dog_age))

# print a sentence that depends of a confidence entered
if confidence_percent < 0.5:
	print("I agree, programmers can't be trusted!")
else:
	print("Writing good code takes hard work!")
