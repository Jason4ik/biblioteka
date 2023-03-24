from os import system
from book import Book
from borrower import Borrower


system('clear')

class Library:
    def __init__(self):
        self.books = []
        self.borrowers = []

    def add_book(self):
        title = input('Insert title of book to add: ')
        author = input('Insert the author of that book: ')
        self.books.append(Book(title, author))
