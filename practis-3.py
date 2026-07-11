def number_of_pieces():
    K = 1
    M = 1
    R = 2
    E = 2
    H = 2
    S = 8
    k, m, r, e, h, s = map(int, input("Enter the number: ").split())
    print(K - k, M - m, R - r, E - e, H - h, S - s)
    return


number_of_pieces()
