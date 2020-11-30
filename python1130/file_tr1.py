my_list = list(range(1, 10))
file = "my_list.txt"

f = open(file, "w")
for my_lists in my_list:
    f.write(str(my_lists) + "\n")
f.close()