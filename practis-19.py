def separator(l_number):
    l_O = []
    l_E = []
    for num in l_number:
        if num % 2 == 0:
            l_E.append(num)
        else:
            l_O.append(num)
    t_number = (l_E, l_O)
    return t_number
