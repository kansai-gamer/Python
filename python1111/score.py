f = open("score.csv", mode="r")
score = f.read()
f.close()
print(score)

date = score.split(",")

date_int = [int(s) for s in date]

f = open("result.txt", mode="w")
f.write(date_int)
f.close()
