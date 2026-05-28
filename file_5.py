# For loops

# For loop variable that will store information in this case from "Python"
# for item in "Python":
#     print(item)

# Iterate over list items, can also be numbers
# for item in ['Mosh', 'John', 'Sarah']:
#     print(item)

# If we have a large list of numbers we can iterate over range

# for item in range(10):
#     print(item)

# for item in range(5, 10):
#     print(item)

# Exercise: calculate the total price

prices = [10, 20, 30]

total = 0

for items in prices:
    total = total + items
print(f"Total: {total}")

# Nested loops - add loop inside another loop

# for x in range(3):
#     for y in range(3):
#         print(x, y)


# Challenge

numbers = [2, 2, 2, 2, 5]

# My attempt
for i in numbers:
    i = "x" * i
    print(i)

# Solution with nested loop
for i in numbers:
    output = ""
    for count in range(i):
        output = output + "x"
    print(output)
