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
    def __init__(self, price, count, date=None):
        super().__init__(price, count)
        self.date = datetime.date.today()
        pass

    def get_date(self):
        return self.date

    def print(self):
        print(f"{self.get_date()} {self.calc():,d}")
