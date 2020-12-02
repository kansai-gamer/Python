x = int(input("X: "))
y = int(input("Y: "))
try:
    z = x / y
    print(z)
except ZeroDivisionError as e:
    print("エラー" , e)
else:
    print("正常動作")
finally:
    print("実行結果を開発チームに報告してください")