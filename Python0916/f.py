def over20ages(users):
    result = []
    for name, age in users.items():
        if age >= 20:
            result.append(name)
    return result


users = {"murayama": 41, "tanaka": 21, "yoshida": 18}
result = over20ages(users)
for name in result:
    print(name)