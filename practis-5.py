def max_number():
    n = int(input("Enter the number: "))
    numbers = [int(n) for n in input("Enter the numbers: ").split()]
    return max(numbers)


print(max_number())
