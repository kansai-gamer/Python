class MyNotFoundError(targets, fruits):
    pass

def search(target, fruits):
    if target == fruits:
        return "Found"
    else:
        return "NotFound"

fruits = ["Lemon", "Orange", "Grape", "Banana", "Peach"]
targets = ["Orange", "Apple", "Lemon"]

for target in targets:
    try:
        print(search(fruits, targets))
    except MyNotFoundError as e:
        print(e)