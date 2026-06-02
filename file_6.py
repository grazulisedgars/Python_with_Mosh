# Lists

names = ["John", "Bob", "Bruno"]
print(names)
print(names[1])
print(names[1:])
names[0] = "John"


# Exercise: Write a program to find the largest number in the list

numbers = [1, 2, 3, 4, 5]

largest_number = numbers[0]

for i in numbers:
    if i > largest_number:
        largest_number = i
print(largest_number)

# Two dimensional lists

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[0][0])

# Row will contain 1 list from matrix
for row in matrix:
    for item in row:
        print(item)
