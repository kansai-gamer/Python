member = input("MEMBER:")
price = int(input("PRICE: "))
gpoint = price // 500
npoint = price // 1000
if(member == "gold"):
    if price >= 500:
        print("POINT: ", gpoint)
elif(member == "normal"):
    if price >= 1000:
        print("POINT: ", npoint)