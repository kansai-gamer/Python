def setoverages(users, setage):
    result = []
    for name, age in users.items():
        if age >= setage:
            result.append(name)
    return result


users = {"murayama": 41, "tanaka": 21, "yoshida": 18}
result = setoverages(users, 18)
for name in result:
    print(name)