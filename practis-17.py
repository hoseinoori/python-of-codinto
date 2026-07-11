import math


def GCD():
    n = int(input("enter the number 1: "))
    m = int(input("enter the number 2: "))
    return math.gcd(m, n)


print(GCD())
