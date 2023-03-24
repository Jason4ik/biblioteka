""" - book class (title, author, isbn, availability, .info())
 """
class Book:
    def __init__(self, title, author, isbn, availability = True):
        self.title = title 
        self.author = author
        self.isbn = isbn
        self.availability = availability
