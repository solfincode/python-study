class BookShelf:
    def __init__(self,*books):
        self.books = books
    def __str__(self):
        return f"bookshelf with {len(self.books)} books"

class Book:
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return f"book {self.name}"

book1 = Book("harry portter")
book2 = Book("python")
shelf = BookShelf(book1,book2)
print(shelf)