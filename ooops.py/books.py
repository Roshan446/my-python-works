class Book:
    name: str
    author: str
    page: int
    price: int
    
    def __init__(self, name, author, page, price):
        self.name = name
        self.author = author
        self.page = page
        self.price = price
    def display_book(self):
        print(self.name, self.author, self.page, self.price)
    def __str__(self):
        return self.name 
obj1 = Book("harry potter", "J.k rowlings", 890, 900)
obj1.display_book()
print(obj1)