def set_over_ages(users, age):
    result = []
    for name, age in users.items():
        if age >= age:
            result.append(name)
    return result


users = {"murayama": 41, "tanaka": 21, "yoshida": 18}
result = set_over_ages(users, 18)
for name in result:
    print(name)