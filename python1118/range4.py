def my_range(start, end, step=1):
    index = start
    while index < end:
        print("yield", index)
        yield index
        index += step

# for i in my_range(1, 10):
#     print(i)

x = my_range(1, 10)
print(x)
print(x.__iter__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())

#クラス
#インスタンス