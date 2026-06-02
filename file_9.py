# Functions - When building large code we should organise it in smaller reusable chunks. Here comes functions.

def greet_user():
    # This inside the function. Will work only when function called
    print("Hi there!")


print("Start!")  # 1
greet_user()  # 2
print("Finish")  # 3

# Parameters - how to pass information to your functions


def greet_user(name):  # We already reusing function with different parameters
    print(f"Hello {name}!")


greet_user("Mary")
greet_user("Jack")


def hello_user(first_name, last_name):
    print(f"Hello {first_name}, {last_name}")


def calc_cost(total, shipping, discount):
    print(
        f"Total is ${total}, shipping will be ${shipping} with discount of {discount}")


# Positional arguments. Order matters
hello_user("Edgars", "Grazulis")

# Keyword arguments
hello_user(last_name="Germane", first_name="Liva")
# When giving code you can instantly say what these values represent
calc_cost(total=50, shipping=5, discount=0.1)

# For the most part use positional arguments, if you use numerical values, see if you can improve readability by keywords.
# Keyword argument always comes after positional arguments.

# In the video till 2:45:06
