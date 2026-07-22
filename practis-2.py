def Score():
    in_score = int(input())
    day = int(input())
    if day == 7:
        return in_score
    elif day == 0:
        return 20
    else:
        if day >= in_score:
            return 0
        else:
            return in_score - day


print(Score())
