# Return statements
# def square(number):
#     return number*number


# result = square(3)
# print(result)

# Reusable functions
# Functions should not worry about receiving input and printing output


def emoji_converter(message):
    words = message.split(" ")
    emojis = {
        ':)': '😊',
        ':(': '😒'
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output


# message = input(">")

# print(emoji_converter(message))


# Exceptions (We use try, except blocks to handle exceptions)

try:
    age = int(input("Age: "))
    income = 20000
    risk = income / age
    print(age)
except ZeroDivisionError:
    print("Age cannot be 0")
except ValueError:
    print("Invalid value")
