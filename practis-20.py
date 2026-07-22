import math


def find_pythagorean_triple():
    n = int(input())
    for a in range(1, n // 3 + 1):
        numerator = math.pow(n, 2) - 2 * n * a
        denominator = 2 * n - 2 * a
        if numerator % denominator == 0:
            b = int(numerator / denominator)
            c = n - a - b
            print(a, b, c)
            return
    print("Impossible")


find_pythagorean_triple()
