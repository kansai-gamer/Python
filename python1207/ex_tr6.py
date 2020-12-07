class Duplicateinput(Exception):
    pass

input_list = []
i = 0
while True:
    value = input("Input: ")
    input_list.append(value)
    if i > 0:
        if input_list[i] == input_list[i - 1]:
            print(input_list)
            break
    i += 1