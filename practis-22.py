def Literal_translation(lin1, lin2):
    if lin1 == "*****":
        return "T"
    elif lin1 == "oo*oo":
        return "A"
    elif lin1 == "*ooo*" and lin2 == "oo*oo":
        return "X"
    elif lin1 == "**o**":
        return "M"
    else:
        return "N"


def Translation():
    lin1_in = str(input())
    lin2_in = str(input())
    lin3_in = str(input())
    li_1 = [lin1_in[i : i + 5] for i in range(0, len(lin1_in), 5)]
    li_2 = [lin2_in[i : i + 5] for i in range(0, len(lin2_in), 5)]
    # li_3 = [lin3_in[i : i + 5] for i in range(0, len(lin3_in), 5)]
    for i in range(len(li_1)):
        print(Literal_translation(li_1[i], li_2[i]), end="")
    return


Translation()
