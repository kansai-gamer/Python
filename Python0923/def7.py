def calc(f, x, y):
    print("Calc", f(x, y))

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

calc(add, 2, 3)
calc(sub, 2, 3)