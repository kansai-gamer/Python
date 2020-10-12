rows = 9
columns = 9
symbol1 = "*"
symbol2 = " "

i = 1
while i <= rows:
    j = 1
    while j <= columns:
        j += 1
        if j % 2 == 0:
            print(symbol1, end='')
        else:
            print(symbol2, end='')
    print()
    i += 1