from abc import ABC, abstractmethod

class LibraryItem(ABC):
    def __init__(self, ID, title, author):
        self.ID = ID
        self.title = title
        self.author = author
    
    @abstractmethod
    def display_details(self):
        pass

class Book(LibraryItem):
    def __init__(self, ID, title, author, pages, genre):
        super().__init__(ID, title, author)
        self.pages = pages
        self.genre = genre

    def display_details(self):
        return f"id: {self.ID}, title: {self.title}, author: {self.author}, pages: {self.pages}, genre: {self.genre}"
    
class Magazine(LibraryItem):
    def __init__(self, ID, title, author, issue_number, publication_date):
        super().__init__(ID, title, author)
        self.issue_number = issue_number
        self.publication_date = publication_date

    def display_details(self):
        return f"id: {self.ID}, title: {self.title}, issue number: {self.issue_number}, publication date: {self.publication_date}"
    
class Article(LibraryItem):
    def __init__(self, ID, title, author, publication_date, summary):
        super().__init__(ID, title, author)
        self.publication_date = publication_date
        self.summary = summary

    def display_details(self):
        return f"id: {self.ID}, title: {self.title}, publication date: {self.publication_date}, and summary: {self.summary}"

b1 = Book("123", "b1", "Jane Austen", 277, "Romantic")
print(b1.display_details())

