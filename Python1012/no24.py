rows = 9
columns = 9
symbol1 = "*"
symbol2 = " "

i = 1
while i <= rows:
    j = 1
    i += 1
    if i % 6 == 0:
        print()
    else:
        while j <= columns:
            j += 1
            if j % 6 == 0:
                print(symbol2, end='')
            else:
                print(symbol1, end='')