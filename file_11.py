# Classes
# Pascal naming convention. For classes start with capital letter

class Point:  # Use clases to identify new types
    def move(self):
        print("Move")

    def draw(self):
        print("Draw")


# point1 = Point()
# point1.x = 10
# point1.y = 20
# print(point1.x)
# point1.draw()

# point2 = Point()  # Completely different from first object
# print(point2.x)  # Gives error as this attribute does not have x


# Constructors
# __init__ short for initialize

class Point:
    def __init__(self, x, y):  # self is reference to current object.
        self.x = x
        self.y = y

    def move(self):
        print("Move")

    def draw(self):
        print("Draw")


point = Point(10, 20)
print(point.x)

# Exercise


class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"what's up? {self.name}")


john = Person("John Smith")
john.talk()

bob = Person("Bob Bobo")
bob.talk()


# Inheritance -mechanisms to reusing code.

class Dog:
    def walk(self):
        print("walk")


class Cat:
    def walk(self):
        print("walk")

# How to solve above problem?


class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal):
    pass  # Telling python language to not worry about empty class


class Cat(Mammal):
    pass


dog1 = Dog()
dog1.walk()

# Another option


class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal):
    def bark(self):
        print("bark")


class Cat(Mammal):
    def be_annoying(self):
        print("annoying")


dog2 = Dog()
dog2.bark()

cat1 = Cat()
cat1.be_annoying()
