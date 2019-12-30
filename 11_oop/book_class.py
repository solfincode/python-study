class Book:
    TYPES=("hardcover","paperback")

    def __init__(self,name,btype,weight):
        self.name = name
        self.btype = btype
        self.weight= weight
    def __repr__(self):
        return f"<Book {self.name},{self.btype}, weigthing {self.weight}g>"
    @classmethod
    def hardcover(cls,name,page_weight):
        return Book(name,Book.TYPES[0],page_weight + 100)

book = Book.hardcover("Harry porter",1500)
print(book)