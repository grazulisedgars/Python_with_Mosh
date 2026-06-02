# Tuples - similar to list. However we cannot ammend or change anything in them

numbers = (1, 2, 3)  # Cannot change tuples
print(numbers[0])

# Unpacking

coordinates = (1, 2, 3)
# u = coordinates[0] * coordinates[1] * coordinates[2]
# x = coordinates[0]
# y = coordinates[1]
# z = coordinates[2]

# x*y*z
# Identical to what we have above. Python interpreter reads it and knows
x, y, z = coordinates

# Can also be used for lists

coordinates2 = [4, 5, 6]
u, i, o = coordinates2
print(i)


# Dictionaries - key and value pairs

customer = {
    'name': 'John Smith',
    'age': 30,
    'is_verified': True
}

print(customer['name'])  # Returns value, when calling key
customer['name'] = 'Jack Smith'  # Updating key 'name' with new value
customer['birthdate'] = 'Jan 1 1900'  # Adding new key
print(customer['birthdate'])

# Exercise: Write a program. Upon input in terminal inserting numbers program returns values as string. For example 1 will come out as one.

phone = input("Phone: ")
phone_number = []
separator = ","

for digit in phone:
    if digit == '1':
        digit = "One"
    elif digit == '2':
        digit = "Two"
    elif digit == '3':
        digit = "Three"

    phone_number.append(digit)

phone_number = separator.join(phone_number)
print(phone_number)

# Teachers version

digits_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four"
}

output = ""
for ch in phone:
    output += digits_mapping.get(ch, "!") + " "
print(output)


# Dictionaries (Emojis) - There is a dictionary that maps smile faces

message = input(">")
words = message.split(' ')  # Whenever in string is space it splits it
emojis = {
    ":)": "😊",
    ":(": " 😒"
}
output = ""
for word in words:
    output += emojis.get(word, word) + " "
print(output)
