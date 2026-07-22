def Atalmatal_game():
    n, m = map(int, input().split())
    count = 1
    t = 1
    while True:
        t += m
        if t % n == 1:
            break
        count += 1
    return count


print(Atalmatal_game())
