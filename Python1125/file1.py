names = ["Alice", "Bob", "Charlie"]
f = open("names.txt", mode="w", newline="\n")
for name in names:
    f.write(name + "\n")
f.close()