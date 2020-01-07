class TooManyPagesReadError(ValueError):
    pass


class Book:
    def __init__(self,name:str,page_count:int):
        self.name = name
        self.page_count = page_count
        self.page_read = 0
    
    def __repr__(self):
        return(
            f"<Book {self.name}, read {self.page_read} pages out of {self.page_count}"
        )
    def read(self,pages:int):
        if self.page_read + pages > self.page_count:
            raise TooManyPagesReadError(
            f"You only have {self.page_count} pages"
        )
        self.page_read +=pages
        print(f"You have now read {self.page_read} pages out of {self.page_count}")

try:
    iphone101 = Book("iphone101",40)
    iphone101.read(230)
except TooManyPagesReadError as e:
    print(e)