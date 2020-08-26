user_id = input("USER ID:")
pw = input("PASSWORD: ")

if(user_id == "Alice"):
    if(pw == "pass"):
        print("Success")
    else:
        print("Error")
else:
    print("Error")