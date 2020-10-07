import random

print("課題①: ", random.randint(1,9))

l = (random.sample(range(19), k=5))

print("課題②: ")
[print(f"{i:2}") for i in l]