# python classes

name = "adkins"
print(name.upper())


# object == variable data+ functions

class Rectangle:
    # constructor
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        result = self.length * self.width
        print(f"the area of a rectangle is {result}")

    def perimeter(self):
        result = 2 * (self.length + self.width)
        print(f"The perimeter of the rectangle is {result}")


r1 = Rectangle(23, 75)

r2 = Rectangle(68.28, 30.75)

r1.area()
r1.perimeter()

r2.area()
r2.perimeter()
