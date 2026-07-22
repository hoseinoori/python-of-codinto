import math


def Least_significant_nonzero_digit():
    n = int(input())
    n_factorial = math.factorial(n)
    while n_factorial % 10 == 0:
        n_factorial = int(n_factorial / 10)
    return n_factorial % 10


print(Least_significant_nonzero_digit())
