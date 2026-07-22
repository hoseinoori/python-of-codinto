import math


def Resulting_value():
    n = int(input())
    m = int(input())
    s = 0
    for j in range(1, n + 1):
        for i in range(-10, m + 1):
            s += int((int(math.pow((i + j), 3))) / (math.pow(j, 2)))
    return s


print(Resulting_value())
