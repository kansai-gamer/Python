x = 10
y = "20"

try:
    z = x + y
    print(z)
except TypeError as e:
    print("TypeError:", e)