height = 10

for i in range(1, height+1):
    for j in range(i):
        print("*", end="")
    print()

print("\n")

for i in range(height, 0, -1):
    for j in range(i):
        print("*", end="")
    print()
