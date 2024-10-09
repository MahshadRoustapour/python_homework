#Q1

class Book:
    total_price = 0
    book_num = 0 
    def __init__(self, id, title, year, author, price, discount):
        Book.is_valid(id)
        self.id = id
        self.title = title
        self.year = year
        self.author = author
        self.price = price
        self.discount = discount
        Book.book_num += 1

    def Calculate(self):
        Book.total_price = self.price - self.discount
        print(Book.total_price)

    def __str__(self):
        return f"Title:{self.title}, Author:{self.author}, Year:{self.year}, Price:{Book.total_price}"
    
    @classmethod
    def book_number(cls):
        print(f"{cls.book_num} books created")

    @staticmethod
    def is_valid(id):
        if not len(id) == 4 or not id[:1].isalpha() or not id[2:].isnumeric():
            raise ValueError("invalid")
book1 = Book("Ab21", "pride", 2004, "jane austen", 200, 0.1)
print(vars(book1))
book1.book_number()
book1.Calculate()
    

           

            

