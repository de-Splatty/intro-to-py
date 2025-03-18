# numbers
from math import *  # the asterisk means everything

print(sqrt(50))
print(round(9.58756343, 4))
print(floor(10.99999999))  # round down
print(ceil(10.00000001))  # round up
print(pow(7, 2))  # 7**2 can also be powered by decimals

radius = 9.25
height = 11.46

volume = 22 / 7 * radius ** 2 * height
print(round(volume, 4))

# surface area

sa = 22 / 7 * radius ** 2 * 2 + (radius * 2 * height)
print(round(sa, 4))



