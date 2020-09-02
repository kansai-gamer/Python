#not
i = 1
while i <= 9:
    j = 1
        if j == 5:
            continue
    while j <= 9:
        print(i * j, end=" ")
        j += 1
    print()
    i += 1