apple = {"name": "apple", "price": 100}
banana = {"name": "banana", "price": 200}
cherry = {"name": "cherry", "price": 300}

fruits = [apple, banana, cherry]

f = open("data/apple.txt", mode="w")
f.write(str(apple["price"]))

f = open("data/banana.txt", mode="w")
f.write(str(banana["price"]))

f = open("data/cherry.txt", mode="w")
f.write(str(cherry["price"]))


for fruit in fruits:
    file_name = fruit["name"]
    price = fruit["price"]
    path = "data/" + file_name + ".txt"
    with open(path, mode="w") as f:
        f.write(str(price))