scores = [80, 60]
file_name = "score.txt"

with open(file_name, 'w') as f:
    x = " ".join([str(s) for s in scores])
    f.write(x)