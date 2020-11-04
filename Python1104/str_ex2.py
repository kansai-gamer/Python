numbers = ["One", "Two", "Three", "Four", "Five"]
i = 0

for number in numbers:
    i = i + 1
    if(i % 2 == 0):
        print(number.lower())
    else:
        print(number.upper())