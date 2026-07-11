def time_of_arar():
    a, b, l = map(int, input("Enter the numbers: ").split())
    t = int(l / 2)
    if l % 2 == 0:
        tim = t * a + t * b
    else:
        tim = (t + 1) * a + t * b
    return tim


print(time_of_arar())
