file = open('Python0909\score.txt')
lines = file.readlines()

total = sum([int(lines.rstrip()) for lines in lines ])
print(total)
file.close()