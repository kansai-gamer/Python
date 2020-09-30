def search(scores, target):
    exist = False
    count = 1

    for score in scores:
        if target == score:
            exist = True
            break
        count = count + 1

    return exist, count


scores = [3, 6, 4, 5, 8, 2, 7, 9,]
target = 9
result = search(scores, target)
print(target, result[1], result[0])