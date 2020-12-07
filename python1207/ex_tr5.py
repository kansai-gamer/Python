class loginError(Exception):
    pass

def login(id,password):
    if id != "alice" or password != "secret":
        raise loginError()
    return True

try:
    id = input("ID: ")
    password = input("PASSWORD: ")
    if login(id, password):
        print("LOGIN OK")
except loginError as e:
    print("LOGIN ERROR")