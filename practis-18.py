def gcd_ladder_recursive(a, b, d=2):
    if a == 0:
        return b
    if b == 0:
        return a
    if d > min(a, b):
        return 1
    if a % d == 0 and b % d == 0:
        return d * gcd_ladder_recursive(a // d, b // d, d)
    return gcd_ladder_recursive(a, b, d + 1)


num1 = abs(int(input("Enter the number 1: ")))
num2 = abs(int(input("Enter the number 2: ")))

print(gcd_ladder_recursive(num1, num2))
