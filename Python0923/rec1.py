def my_func(x):
    if x >= 0:
        print(x)
        my_func(x - 1)


my_func(10)