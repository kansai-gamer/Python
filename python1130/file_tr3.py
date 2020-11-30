fruits = {"Apple": 100, "Lemon": 200, "Oragne": 300}
file = "fruits.txt"

f = open(file, "w")
for fruit in fruits:
    f.write(str(fruit))
f.close()