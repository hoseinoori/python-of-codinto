def max_number():
    n = int(input())
    numbers = [int(n) for n in input().split()]
    return max(numbers)


print(max_number())
