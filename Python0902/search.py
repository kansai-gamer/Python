target = "Arai"
names = ["Arai", "Hirose", "Nakamori"]
flag = False
for name in names:
    if name == target:
        flag = True


if flag == True:
    print("Found")
else:
    print("Not found")