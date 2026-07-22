def Check_size():
    n, m = map(int, input().split())
    x, y = map(int, input().split())
    if n >= x and m >= y:
        return "yes"
    else:
        return "no"


print(Check_size())
