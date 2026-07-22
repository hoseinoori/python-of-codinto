def Calculator():
    num1 = int(input())
    char = str(input())
    num2 = int(input())
    if char == "+":
        return num1 + num2
    else:
        return num2 * num1


print(Calculator())
