# calc

# x = input("Provide for X:")
# b = input("Provide for B:")

# convert string to number
while True:
    try:
        num1 = float(input("Enter X:"))
        num2 = float(input("Enter Y:"))
        if num2 == 0:
            print("indivisible by zero. Try again.")
            continue
            result = num1 / num2
            print(result)
    except ValueError:
        print("Invalid input. Please enter numbers only.")
# int calculates only whole numbers while float calculates both whole and decimals
