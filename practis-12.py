def Sum_of_Breaths():
    n = int(input("Enter the number: "))
    list_in_1 = list(map(int, input("Enter the numbers: ").split()))
    list_in_2 = list(map(int, input("Enter the numbers: ").split()))
    sum_of_in = 0
    for i in range(n):
        sum_of_in += list_in_1[i] * list_in_2[i]
    return sum_of_in


print(Sum_of_Breaths())
