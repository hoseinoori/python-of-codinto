import math


def Calculation():
    x = int(input("Enter the X: "))
    n = int(input("Enter the N: "))
    s = 0
    for i in range(n):
        s += float((math.pow(x, i)) / math.factorial(i))
    print(f"{s:.3f}")
    return


Calculation()
