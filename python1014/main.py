class Myclass:
    #__init__ メソッド コンストラクタ
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def myMethod(self, arg1):
        print("call myMethod", arg1, self.x, self.y)

#Python からか他のファイルからか判定
if __name__ == "__main__":
    
    instance = Myclass(10, 20)
    instance.myMethod(1)