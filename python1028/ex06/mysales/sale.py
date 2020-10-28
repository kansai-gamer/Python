import datetime

class Sale:
    def __init__(self, price, count):
        self.price = price
        self.count = count

    def calc(self):
        return self.price * self.count

    def print(self):
        print(f"{self.calc():,d}")

class DailySale(Sale):
    def get_data(self):
        return datetime.date.today()

    def print(self):
        x = self.get_data()
        print(x, end=" ")
        super().print()