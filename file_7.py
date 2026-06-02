# list methods (functions)

numbers = [5, 2, 1, 7, 4]

numbers.append(20)  # We can add to the list
print(numbers)

numbers.insert(0, 10)  # Pass two values. First index (position), second value
print(numbers)

numbers.remove(4)  # Remove an item
print(numbers)

numbers.pop()  # Removes last item in the list
print(numbers)

print(numbers.index(5))  # Prints the index where is 5

print(50 in numbers)  # False because there is no 50 in the list

print(numbers.count(20))  # Counts how many 20s are in the list

numbers.sort()  # Sorts in ascending order
numbers.reverse()  # Sorts in descending order
print(numbers)

numbers2 = numbers.copy()
numbers.append(11)
print(numbers)

numbers.clear()  # Clears the whole list
print()


# Exercise Write a program that removes duplicates in the list

list = [1, 2, 3, 4, 5, 5, 6, 6]
unique_numbers = []

for i in list:
    if i not in unique_numbers:
        unique_numbers.append(i)
print(unique_numbers)
