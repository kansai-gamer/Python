try:
    filename = input("File name:")
    with open(filename, "r") as f:
        print(f.read())
except FileNotFoundError:
    print(f"{filename} is not found.")