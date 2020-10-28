class MyClass:

    #データ属性（クラス変数 or クスデータ属性）
    a = 1000

    #コンストラクタ 
    def __init__(self, x, y):
        #データ属性（インスタンス変数、インスタンスデータ属性）
        self.__x = x
        self.__y = y

    #インスタンスメソッド
    def myMethod(self, arg1):
        print("call myMethod", arg1, self.__x, self.__y)


    @classmethod
    def myClassMethod(cls, arg1):
        print("call myClassMethod", arg1, cls.a)

    @staticmethod
    def mystaticmethod(arg1):
        print("call mystaticmethod", arg1)

if __name__ == "__main__":
    instance = MyClass(100, 200)
    instance.myMethod(1)
    MyClass.myClassMethod(10)
    MyClass.mystaticmethod(100)