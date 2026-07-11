def Check_size():
    n, m = map(int, input("Enter size of tshert: ").split())
    x, y = map(int, input("Enter size of winner: ").split())
    if n >= x and m >= y:
        return "yes"
    else:
        return "no"


print(Check_size())
