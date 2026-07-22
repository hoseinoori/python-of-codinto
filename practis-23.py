import math


def Count_Perfect_Square(l, r):
    sqrt = 0
    count = 0
    for i in range(l, r + 1):
        sqrt = math.sqrt(i)
        sqrt = int(sqrt * 100000)
        if sqrt % 100000 == 0:
            count += 1
    return count


def Perfect_Square():
    q = int(input())
    lis_in = []
    lis_out = []
    for i in range(q):
        lis_in.append(str(input()))
        l, r = map(int, str(lis_in[i]).split())
        lis_out.append(Count_Perfect_Square(l, r))
    for i in range(len(lis_out)):
        print(lis_out[i])


Perfect_Square()
