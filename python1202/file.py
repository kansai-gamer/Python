scores_list = [[80, 60], [70, 50], [60, 40]]
file_name = "score.txt"

with open(file_name, 'w') as f:
    for scores in scores_list:
        x = " ".join([str(s) for s in scores])
        f.write(x + "\n")