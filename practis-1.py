def Square():
    n = int(input("Enter the number: "))
    for i in range(n):
        print("*", end="")
    print("")
    for i in range(n - 2):
        print(f"*{" "*(n-2)}*")
    for i in range(n):
        print("*", end="")
    return


Square()
