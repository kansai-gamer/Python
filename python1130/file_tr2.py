file = "my_list.txt"

with open(file, "r") as f:
    lines = f.readlines()
    f.close()
print(sum([int(line.strip()) for line in lines]))