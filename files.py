# files
import os

file = open("data.txt", "w")

file.write("hello, world of python files\n this is testing\n do you read")

file.close()

try:
    file = open("data.txt", "r")
    data = file.read()
    print(data)
    file.close()
except:
    pass
    # print("Something went wrong")


def add():
    pass

if 10 > 11:
    pass


def get_dimens(image):
    return 10, 20, "png"


l, w, ext = get_dimens("image")

# os.remove("data.txt")

# print(os.path.exists("data.txt"))

pops = [10, 9 ,8]

x, y ,z = pops

print(x)
