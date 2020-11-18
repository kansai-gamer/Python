names = ["Alice", "Bob", "Charlie", "Dave"]



f = open("names.txt", mode="w")

i = 1
for name in names:
    i += 1
    f.write(str(i) + "," + name + "\n")
f.close()