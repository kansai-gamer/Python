from random import randint

randomnums = randint(0,2)

user = int(input("Please enter a number (0:Goo, 1:Choki, 2:Par) "))

if user == (randomnums - 1) % 3:
    print("Win")

elif user == (randomnums + 1) % 3:
    print("lose")

else:
    print("Draw")

#松岡秀真さんのコードをパク...参考にしました。