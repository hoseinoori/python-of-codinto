import math


def Khayyam_Triangle():
    n = int(input("Enter the number: "))
    for i in range(n):
        for j in range(i + 1):
            print(
                int(
                    (math.factorial(i))
                    / ((math.factorial(j)) * (math.factorial(i - j)))
                ),
                end=" ",
            )
        print("")
    return


Khayyam_Triangle()
