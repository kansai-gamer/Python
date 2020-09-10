target = "aoki"
names = ["aoki", "takada", "shirai"]
flag = False
for name in names:
    if name == target:
        flag = True
        break

if flag:
    print("Found")
else:
    print("Not found")