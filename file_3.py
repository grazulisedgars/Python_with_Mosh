# If statements

is_hot = False
is_cold = True

# if is_hot == True:
#     # print("It's a hot day")
#     # print("Drink plenty of water")
# elif is_cold == True:
#     # print("It's a cold day")
#     # print("Wear warm clothes")
# else:
#     # print("It's a lovely day")

#     # Exercise: If statements if buyer has good credit, they need to put down 10%. Otherwise, they need to put down 20%.

house_price = 1000000
good_credit = True

if good_credit == True:
    down_payment = house_price * 0.1
else:
    down_payment = house_price * 0.2
# print(f"Down payment: ${down_payment}")

# Logical operators

has_high_income = True
has_good_credit = False

if has_high_income and has_good_credit:  # if both conditions are true message will be printed
    print("Eligible for loan")

if has_high_income or has_good_credit:  # if one of the conditions is true message will be printed
    print("Eligible for loan")

has_good_credit = True
has_criminal_record = False

# if the person has good credit and does not have a criminal record, message will be printed
if has_good_credit and not has_criminal_record:
    print("Criminal is eligible for loan")

# Comparison operators
# >, <, >=, <=, ==, !=

temperature = 15

if temperature > 30:
    print("It's a hot day")
elif temperature < 10:
    print("It's a cold day")
else:
    print("It's neither a hot or cold day")


# Exercise: if name is less than 3 characters, print "Name must be at least 3 characters". If name is more than 50 characters, print "Name can be a maximum of 50 characters". Otherwise, print "Name looks good".

name = "Edgars"

if len(name) < 3:
    print("Name must be at least 3 characters")
elif len(name) > 50:
    print("Name can be a maximum of 50 characters")
else:
    print("Name looks good!")

# Project Weight Converter

weight = input("Weight: ")
unit = input("(L)bs or (K)g: ")

if unit.upper() == "K":
    weight_lbs = int(weight) * 2.2046
    print(f"You are {weight_lbs} lbs")
elif unit.upper() == "L":
    weight_kg = int(weight) * 0.45
    print(f"You are {weight_kg} kilograms")
else:
    print("You've entered a wrong letter")
