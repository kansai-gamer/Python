import datetime

file = "datatime.txt"
now = datetime.datetime.now()

f = open(file, "w")
f.write(str(now))
f.close