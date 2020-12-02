file_name = "score.txt"

with open(file_name, 'r') as f:
    lines = f.readlines()
    total = 0
    for line in lines:
        items = line.split(" ")
        total += sum([int(item) for item in items])
    print(total)

    