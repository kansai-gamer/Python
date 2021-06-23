print("問題1\n")
for i in range(1,5):
    for j in range(i):
        print("*",end="")
    print("")

print("\n問題2\n")

for i in range(1,5):
    for j in range(5 - i):
        print("*",end="")
    print("")

print("\n問題3\n")

for i in range(1,3):
    for j in range(i):
        print("*",end="")
    print("")

for i in range(3):
    for j in range(3 - i):
        print("*",end="")
    print("")

print("\n問題4\n")

for i in range(1,4):
    for j in range(4):
        print("*",end=" ")
    print("")

print("\n問題5\n")

for i in range(5):
    if i % 2:
        for j in range(4):
            print(" *",end="")
        print("")
    else:
        for j in range(5):
            print("*",end=" ")
        print("")

print("\n問題6\n")

for i in range(1,32):
    print(i,end=" ")
    if i % 7 == 0:
        print("")