class MyClass:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
    def myMethod(self, arg1):
        print("call myMethod", arg1, self.__x, self.__y)
    def get_x(self):
        return self.__x
    def set_x(self, x):
        self.__x = x
    def get_y(self):
        return self.__y
    def set_y(self, y):
        self.__y = y
if __name__ == "__main__":
    instance = MyClass(10, 20)
    instance.set_x(100)
    instance.set_y(200)
    instance.myMethod(1)
    print(instance.get_x())
    print(instance.get_y())