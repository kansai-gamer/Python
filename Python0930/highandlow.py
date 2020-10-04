import random
random = int((random.uniform(1, 1000)))

count = 0

while True:
    str = int(input("Number : "))
    if str == random:
        print("OK !!")
        count = count + 1
        break
    elif int(str) <= random:
        print("High !")
        count = count + 1
    elif int(str) >= random:
        print("Low !")
        count = count + 1

print(count)