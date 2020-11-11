class Sale:
    def __init__(self, price, count):
        self.__count = count
        self.__price = price

    def calc(self):
        return self.__price * self.__count

    def print(self):
        print(f"{self.calc():,d}")

class Customer:
    def __init__(self, name):
        self.__name = name

    def print(self):
        print(f"{self.__name}")

class CustomerSale:
    def __init__(self, customer, sale):
        self.__customer = customer
        self.__sale = sale

    def print(self):
        self.__customer.print()
        self.__sale.print()