import datetime  # We'll need this library for getting a current year

title_of_the_book = input("Enter the title of the book: ")  # Ask an user for a title of the book
name_of_the_author = input("Enter the name of the author: ")  # Ask an user for a name of the author
publish_year_ot_the_book = int(input("Enter the publish year of the book: "))  # Ask an user for a publish year of the book
total_number_of_pages_in_the_book = int(input("Enter the total number of pages in the book: "))  # Ask an user for a total number of pages in the book

current_year = datetime.datetime.today().year  # Get the current year
age_of_the_book = current_year - publish_year_ot_the_book  # Calculate an age of the book

# Print the sentence that depends of age of the book
if age_of_the_book < 10:
	print("This book is younger than ten years old.")  # If book's age is under 10 years
else:
	print("This book is at least ten years old.")  # If book's age is over 10 years
	
# Print the sentence that depends of number of pages in the book	
if total_number_of_pages_in_the_book<100:
	print("This book is a short book.")  # If the number of pages is below 100
elif total_number_of_pages_in_the_book < 300:
	print("This book is an average book.")  # If the number of pages is between 100 and 300
else:
	print("This book is a long book.")  # If the number of pages exceeds 300
