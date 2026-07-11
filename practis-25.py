def Profit_calculation():
    m, d, c, b, a = map(int, input("Enter the numbers: ").split())
    a_m = m * c + a
    b_m = m * d + b
    max_m = max(b_m, a_m)
    a_profit = a_m - a
    b_profit = b_m - b
    max_profit = max(b_profit, a_profit)
    if (max_profit == a_profit and max_m == a_m) or (
        max_profit == b_profit and max_m == b_m
    ):
        return "Eyval baba!"
    else:
        return "Naaa, eshtebahe!"


print(Profit_calculation())
