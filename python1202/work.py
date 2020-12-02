while True:
    nuber_s = input("Nuber: ")
    try:
        number = int(nuber_s)
        if len(str(number)) == 0:
            raise ValueError()
        elif len(str(number)) <= 5:
            break
        else:
            print("5文字以下で入力してください")
    except ValueError as e:
        print("エラーもう一度入力してください")
        print(e)


print(number)

#len関数使わずにやろうとしてハマったの内緒です