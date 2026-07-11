def Light_status():
    n = int(input("Enter the number: "))
    if n == 1:
        return 0
    count = 0
    in_1 = int(input("Enter status: "))
    for i in range(n - 1):
        in_2 = int(input("Enter status: "))
        if in_1 != in_2:
            count += 1
        in_1 = in_2
    return count


print(Light_status())
