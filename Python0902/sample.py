# score = 80
# score2 = 70
# score3 = 90

# total = score + score2 + score3
# average = total / 3
# print(average)
scores = [80, 70, 90, 100, 50, 90, 70, 50, 60, 40, 11, 23, 45]
i = 0
total = 0
while i < len(scores):
    total = total + scores[i]
    i += 1
print(total)