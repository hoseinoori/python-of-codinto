import math


def Sum_of_digits(n):
    list_number = [int(char) for char in n]
    sum_numbers = sum(list_number)
    return sum_numbers


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True


def Prime_number():
    n = str(input("Enter the number: "))
    s = Sum_of_digits(n)
    number = int(n) + 1
    count = 0
    while True:
        if is_prime(number):
            count += 1
            if count == s:
                break
        number += 1
    return number


print(Prime_number())
