def fizzbuzz_ganerator(start, stop):
    index = start
    while index < stop:
        if index % 3 == 0 and index % 5 == 0:
            print("FizzBuzz")
        
        elif index % 3 == 0:
            print("Fizz")

        elif index % 5 == 0:
            print("Buzz")
        
        else:
            yield index
        index += 1


for i in fizzbuzz_ganerator(1, 16):
    print(i)

# Fizz Buzz忘れたのでググりました。
# https://qiita.com/Sekky0905/items/7e2b13f2a001384c7fc4