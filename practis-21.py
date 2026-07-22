import math


def Calculation():
    x = int(input())
    n = int(input())
    if n == 0 or x == 0:
        print(1.000)
        return
    s = 0
    for i in range(n):
        s += float((math.pow(x, i)) / math.factorial(i))
    print(f"{s:.3f}")
    return


Calculation()
