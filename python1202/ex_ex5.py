class MyNotFoundError(Exception):
    pass

def search(fruits, target):
    while True:
        if target in fruits:
            return f"{target} is found."
        else:
            raise MyNotFoundError(f"{target} is not found.")

fruits = ["Lemon", "Orange", "Grape", "Banana", "Peach"]
targets = ["Orange", "Apple", "Lemon"]

for target in targets:
    try:
        print(search(fruits, target))
    except MyNotFoundError as e:
        print(e)