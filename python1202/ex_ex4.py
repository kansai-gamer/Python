import io

try:
    with open("not_exist.txt", "w") as f:
        print(f.read())
except ValueError as e:
    print(e)
finally:
    print("end")