class Book:
    def __init__(self, title, price,peges):
        self.title = title
        self.price = price
        self.peges = peges
        
    def show(self):
        print(self.title, self.price, self.peges)

class category:
    def name(self):
        


book1 = Book("python book", 3000, 300)
book2 = Book("PHP book", 2000, 250)
book3 = Book("Hello english", 1000, 200)

book1.show()
book2.show()
book3.show()