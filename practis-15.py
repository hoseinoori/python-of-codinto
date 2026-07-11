def game(num):
    number = str(num)
    l_numbers = [int(char) for char in number]
    ma = max(l_numbers)
    mi = min(l_numbers)
    return ma - mi
