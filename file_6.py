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

# In the video 2:01:56
