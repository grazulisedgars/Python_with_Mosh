# Classes
# Pascal naming convention. For classes start with capital letter

class Point:  # Use clases to identify new types
    def move(self):
        print("Move")

    def draw(self):
        print("Draw")


point1 = Point()
point1.x = 10
point1.y = 20
print(point1.x)
point1.draw()

point2 = Point()  # Completely different from first object
print(point2.x)  # Gives error as this attribute does not have x
