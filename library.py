from os import system
from book import Book
from borrower import Borrower


system('clear')

class Library:
    def __init__(self):
        self.books = []
        self.borrowers = []

    def add_book(self, title, author):
        self.books.append(Book(title, author))

    def loan_book(self, title, author):
        print('Checking availability of book...')
        
