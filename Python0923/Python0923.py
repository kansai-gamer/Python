def my_sum(*args):
    x = sum(args)
    return x

x = 10
y = 20
z = my_sum(x, y)
print(z)