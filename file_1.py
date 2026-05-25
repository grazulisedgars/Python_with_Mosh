# Identify variables

# Interpreter executes code line by line. If we would assign a new value to price, the previous value would be lost.
price = 10
print(price)

# Exercise 1:
patient = "John Smith"
age = 20
new_patient = True

# These are built in functions in Python.
# input()  # Think as remote control for tv.
# print()

# Exercise 2:
# This will print the string and wait for user input. Once user enters something, it will return that value as a string.
# name = input("What is your name? ")
# # This will concatenate the string "Hello" with the value of name variable and print it.
# print("Hello " + name)
# # Extending exercise 2:
# favourite_color = input("What is your favourite color?")
# print("Your favourite color is " + favourite_color)

# Type conversion

# birth_year = input("Birth year: ")
# # This will print <class 'str'> because input() function returns a string.
# print(type(birth_year))
# age = 2026 - int(birth_year)
# # This will print <class 'int'> because we have converted birth_year to an integer using int() function.
# print(type(age))
# print(age)

# int()  # Converts string to an integer
# float()  # Converts string to a float
# bool() # Converts string to a boolean value (True or False)

# Exercise 3: Ask a user their weight in pounds and convert it to kilograms. (1 pound is 0.45 kg)
# weight_pounds = input("Weight in pounds:")
# weight_kg = float(weight_pounds) * 0.45
# print("Weight in kilograms:", weight_kg)


# Defining strings
# This is a string literal. It is a sequence of characters enclosed in quotes. Can be single or double quotes.
course = "Python for Beginners"
# This will cause an error because the single quote in "Python's" is interpreted as the end of the string. To fix this, we can use double quotes to enclose the string.
course = "Python's Course for Beginners"
# This will cause an error because the double quotes in "Beginners" is interpreted as the end of the string. To fix this, we can use single quotes to enclose the string.
course = 'Python for "Beginners"'
course = '''Hi John, 
Here is our first email to you.'''  # This is a multi-line string. It is enclosed in triple quotes (either single or double). It can span multiple lines and preserve the line breaks.
print(course)
# This will print the first character of the string, which is 'P'. In Python, string indexing starts at 0.
print(course[0])
# This will print the last character of the string, which is '.'.
print(course[-1])
# This will print the characters from index 0 to index 2 (3 is exclusive), which is 'Pyt'.
print(course[0:3])
# This will print the characters from index 1 to the end of the string, which is 'ython for Beginners'.
print(course[1:])
