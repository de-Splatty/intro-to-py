for number in range(10):
    result = number ** 2
    if result % 2 != 0:
        print(result)

for number in range(50):
    result = number * 2
    if result % 2 == 0:
        print(result, "tik")
    else:
        print(result, "tok")

for number in range(20, 0, -1):
    result = number
    print(result)

for number in range(2, 100):
    is_prime = True

    for divider in range(2, number):
        if number % divider == 0:
            is_prime = False
            break

    if is_prime:
        print(number,"prime")

# multiplication table

number = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{number} × {i} = {number * i}")
