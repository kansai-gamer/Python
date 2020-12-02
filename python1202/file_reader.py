file_name = "score.txt"

with open(file_name, 'r') as f:
    r = f.read()

total = r.split()
print(total)
print(sum(total))