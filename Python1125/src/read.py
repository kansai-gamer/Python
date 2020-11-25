file_name = "../data/hello.txt"

f = open(file_name, "r")
str = f.read()
f.close
print(str)
