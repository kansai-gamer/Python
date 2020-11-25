import datetime

file = "datatime.txt"
now = datetime.datetime.now()

f = open(file, "a")
f.write(str(now) + "\n")
f.close