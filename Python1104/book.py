class Book:
    def __init__(self, title, price,peges):
        self.title = title
        self.price = price
        self.peges = peges
        
    def show(self):
        print(self.title, self.price, self.peges)

class category:
    def __init__(self, name):
        self.name = name
        self.books = []

    def show(self):
        print(self.name)
        for book in self.books:
            book.show()

    def add_book(self, book):
        self.books.append(book)

category1 = category("programming")
category2 = category("english")

book1 = Book("python book", 3000, 300)
book2 = Book("PHP book", 2000, 250)
book3 = Book("Hello english", 1000, 200)

category1.add_book(book1)
category1.add_book(book2)

category1.show()

category2.add_book(book3)
category2.show()