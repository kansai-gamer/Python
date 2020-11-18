def odd_generator(start = 1, stop = 10):
    index = start
    while index < stop:
        if index % 2 == 1:
            yield index 
        index += 1


og = odd_generator()
for v in og:
    print(v)