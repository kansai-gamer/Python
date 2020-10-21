#クラスの定義
class Bottle:
    #データ属性 water, opened
    def __init__(self):
        self.water = 10
        self.opened = False

    def drink(self):
        self.water -= 5

    def open(self):
        self.opened = True

#インスタンスの生成
# my_Bottle 
my_bottle = Bottle()

# drinkメソッドを呼び出す

my_bottle.drink()

print(my_bottle.water)