class MyRequiredError(Exception):
    pass

class MyLengthError(Exception):
    pass

def validate(value, count):
    if len(value) == 0:
        raise MyRequiredError()
    if len(value) > count:
        raise MyLengthError()

try:
    value = input("input: ")
    validate(value, 5)
    print(value)

except MyRequiredError as e:
    print("MyRequiredError")

except MyLengthError as e:
    print("MyLengthError")