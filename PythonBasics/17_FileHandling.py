with open("data.txt", "w") as f:
    for i in range(1, 6):
        s = input(f"Student name {i}: " )
        f.write(s + "\n")


with open("data.txt") as f:
    for x in f:
        print(x)