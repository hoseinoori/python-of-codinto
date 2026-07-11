def Calculator():
    num1 = int(input("Enter the number 1: "))
    char = str(input("Enter the character: "))
    num2 = int(input("Enter the number 2: "))
    if char == "+":
        return num1 + num2
    else:
        return num2 * num1


print(Calculator())
