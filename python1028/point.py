class Point:

    z = 0


    @classmethod
    def hello(cls):
        print("hello", cls.z)
        cls.z += 1

    @classmethod
    def warld(cls):
        print("world")

    def __init__(self, x, y):
        self.__x = x
        self.__y = y
    
    def show(self):
        print(f"({self.__x}, {self.__y})")

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y

    def calc(self, point2):
        a = (self.x - point2.x) ** 2
        b = (self.y - point2.y) ** 2
        c = (a + b) ** 0.5
        return c

# point1 = Point(10, 20)

# point1.x = 100
# point1.y = 200

# point1.show()

point1 = Point(0, 0)
point2 = Point(1, 3**0.5)
answer = point1.calc(point2)
print(answer)

Point.hello()
Point.hello()