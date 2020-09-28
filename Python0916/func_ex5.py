from random import randint
randomnums = randint(0,3)
print(randomnums)
nums = input("Please enter a number (0:Goo, 1:Choki, 2:Par) ")
if nums == randomnums:
    print("Draw")