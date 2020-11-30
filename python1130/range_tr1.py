def count_down_generator():
    start = 5
    stop = -1
    index = start
    while index > stop:
        yield index
        index -= 1

for i in count_down_generator():
    print(i)