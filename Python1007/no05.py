import math
number1 = 18
number2 = 12
# https://note.nkmk.me/python-gcd-lcm/ 参考元
#least common multipleはなぜか無いので参考元を見ながら作る

def lcm (x, y):
    return (x * y) // math.gcd(x, y) #掛けた後、割る

print(lcm(number1, number2))