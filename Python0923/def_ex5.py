def factorial(x):
    t = x
    for i in range(1, x):
        t = t * i
    return t
    
x = 5
y = factorial(x)
print(y)