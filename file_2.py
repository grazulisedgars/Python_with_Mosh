# Formatted strings

import math
first_name = "John"
last_name = "Smith"
# not a good way to format strings
message = first_name + ' [' + last_name + '] is a coder'
msg = f"{first_name} [{last_name}] is a coder"  # better way to format strings
# print(message)
# print(msg)

# String methods
course = "Python for Beginners"
print(len(course))
print(course.upper())
print(course.lower())
print(course.title())  # converts the first character of each word to upper case
# returns the index of the first occurrence of the specified value
print(course.find("o"))
print(course.find("O"))  # returns -1 if the value is not found
# replaces a specified value with another value
print(course.replace("Beginners", "Absolute Beginners"))
# returns True if the specified value is found in the string, otherwise returns False
print('Python' in course)


# Arithmetic operations
print(10 + 3)
print(10 - 3)
print(10 * 3)
print(10 / 3)
print(10 // 3)  # floor division, returns the number without the remainder
print(10 % 3)  # modulus operator, returns the remainder of the division
# exponentiation operator, returns the value of 10 raised to the power of 3
print(10 ** 3)

# Augmented assignment operator
x = 10
x = x + 3
print(x)

x += 3  # equivalent to x = x + 3
x -= 3  # equivalent to x = x - 3
x *= 3  # equivalent to x = x * 3
print(x)

# Order of operations
# Exponentiation
# Multiplication or division
# Addition or subtraction
# Parentheses can be used to change the order of operations

# Math functions

x = 2.9
print(round(x))  # rounds the number to the nearest integer
print(abs(-2.9))  # returns the absolute value of a number, always positive

print(math.ceil(2.9))  # rounds the number up to the nearest integer
print(math.floor(2.9))  # rounds the number down to the nearest integer
