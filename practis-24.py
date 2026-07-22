def Ice_cube_tray():
    a, b, c, d, e, f = map(int, input().split())
    lis_ice = [d, e, f]
    lis_bax = [a, b]
    lis_ice.remove(max(lis_ice))
    if (lis_ice[0] <= lis_bax[0] and lis_ice[1] <= lis_bax[1]) or (
        lis_ice[1] <= lis_bax[0] and lis_ice[0] <= lis_bax[1]
    ):
        return "zende mimuni"
    else:
        return "dari mimiri"


print(Ice_cube_tray())
