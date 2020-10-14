class Bottle:
    def __init__(self):
        # データ属性・・・状態（フィールド、プロパティともいう）
        self.water = 200
        self.opened = False
    # メソッド（関数）・・・動作、振る舞い
    def drink(self):
        if self.opened == True:
            if self.water >= 10:
                self.water -= 10
            else:
                print("ERROR BOTTLE IS EMPTY!")    
        else:
            print("ERROR NOT OPENED!")
    def open(self):
        self.opened = True
my_bottle = Bottle()
my_bottle.open() # フタを開ける
for i in range(1, 30):
    my_bottle.drink() # 飲む
print(my_bottle.opened)
print(my_bottle.water)
