def Comparison():
    num_1 = int(input("Enter the number 1: "))
    num_2 = int(input("Enter the number 2: "))
    if num_2 == num_1:
        print(num_1, "=", num_2)
        return
    y_1 = num_1 % 10
    y_2 = num_2 % 10
    if y_1 > y_2:
        print(num_2, "<", num_1)
        return
    elif y_2 > y_1:
        print(num_1, "<", num_2)
        return
    d_1 = int(num_1 / 10) % 10
    d_2 = int(num_2 / 10) % 10
    if d_1 > d_2:
        print(num_2, "<", num_1)
        return
    elif d_2 > d_1:
        print(num_1, "<", num_2)
        return
    s_1 = int(num_1 / 100)
    s_2 = int(num_2 / 100)
    if s_1 > s_2:
        print(num_2, "<", num_1)
        return
    elif s_2 > s_1:
        print(num_1, "<", num_2)
        return


Comparison()
