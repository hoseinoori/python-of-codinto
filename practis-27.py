def Prime_factorization():
    n = int(input())
    list_numbers = []
    list_pow = []
    for i in range(2, n + 1):
        count = 0
        while n % i == 0:
            count += 1
            n = int(n / i)
        if count > 0:
            list_numbers.append(i)
            list_pow.append(count)
    for i in range(len(list_numbers)):
        if i == (len(list_numbers) - 1):
            print(f"{list_numbers[i]}^{list_pow[i]}", end="")
        else:
            print(f"{list_numbers[i]}^{list_pow[i]}*", end="")
    return


Prime_factorization()
