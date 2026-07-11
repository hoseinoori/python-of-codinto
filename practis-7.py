def Symmetric_number():
    number = str(input("Enter the number: "))
    list_of_number = list(number)
    n = len(list_of_number)
    m = int(n / 2)
    if m == 0:
        return "YES"
    count = 0
    for i in range(m):
        if list_of_number[i] == list_of_number[-i - 1]:
            count += 1
    if count == m:
        return "YES"
    else:
        return "NO"


print(Symmetric_number())
