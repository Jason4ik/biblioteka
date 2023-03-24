""" - book class (title, author, isbn, availability, .info())
 """
import random
class Book:
    def __init__(self, title, author):
        self.title = title 
        self.author = author
        self.isbn = random.randint(1000, 9999)
        self.availability = True

    def info(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Availability: {self.availability}"