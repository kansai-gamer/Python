class Car:
    def __init__(self, name, gas):
        self.gas = gas
        self.name = name
        self.distance = 0

    def goto(self):
        print(self.name, "BOOM")

        self.gas -= 1
        self.distance += 20

class FireTruck(Car):
    def __init__(self, name, gas, water):
        super().__init__(name, gas)
        self.water = water

    def spray_water(self):
        print(self.name, "==============")
        self.water -= 1

if __name__ == "__main__":
    myfire = FireTruck("fire", 100, 100)
    myfire.spray_water()
    print(myfire.name, myfire.water)