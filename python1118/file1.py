names = ["Alice", "Bob", "Charlie", "Dave"]

f = open("names.txt", mode="w")

for i, name in enumerate(names):
    f.write(str(i + 1) + "," + name + "\n")

f.close()