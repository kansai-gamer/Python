total = 0
scores = [80, 60, 70, 90, 100]

for score in scores:
    total = total + score

print(total)

ave = total / len(scores)

print(ave)

dis = 0
for score in scores:
    dis += (score - ave) ** 2
dis = dis / len(scores)
print(dis)