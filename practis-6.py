def Health_Guide():
    string = str(input("Enter the string: "))
    R = string.count("R")
    Y = string.count("Y")
    G = string.count("G")
    if R >= 3:
        return "nakhor lite"
    elif R >= 2 and Y >= 2:
        return "nakhor lite"
    elif R == 5 or Y == 5:
        return "nakhor lite"
    else:
        return "rahat baash"


print(Health_Guide())
