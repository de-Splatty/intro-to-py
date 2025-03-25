# functions
import math


def greet():
    print('Hello, functions')


def area_circle(radius):
    result = 22 / 7 * radius ** 2
    result = round(result)
    print(result)


def volume_of_cylinder(height, radius, precision=2):
    v = 22 / 7 * radius ** 2 * height
    v = round(v, precision)
    print(f"radius is {radius}, height is {height}, volume is {v}")


def area_triangle(a, b, c):
    """calculates the area of a triangle then returns the results"""
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    area = round(area, 4)
    print(f"If a is {a}, b is {b}, and c is {c}, the area is {area}")
    return area


def factorial(num):
    result = 1
    while num > 0:
        result = result * num
        num = num - 1
    return result


print(factorial(4))


def add_numbers(*args):
    sum = 0
    for num in args:
        sum += num
    return sum


print(add_numbers(2, 5))
print(add_numbers(3, 4, 5, 6))


def extract_numbers(text):
    """Extracts numbers from a given string."""
    return ''.join(re.findall(r'\d+', text))


text = "abc123def"
result = extract_numbers(text)
print(result)

# f is for formatting
# one doesn't have to specify the precision as lon as a default value is given
# use a function == call function

# area_triangle(21, 30, 18)
# area_triangle(43, 54, 30)

# volume_of_cylinder(14, 7)
# volume_of_cylinder(100, 34, 4)
# volume_of_cylinder(radius=27, height=79, precision=2)  # name parameters

# area_circle(7)
# area_circle(64)
# area_circle(314.45)

# greet()
# greet()
# greet()
