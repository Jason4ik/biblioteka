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















# MENU HERE
while True:
    print("""LIBRARY MENU:
[1] Books list
[2] Add a book
[3] Find a book
[4] Loan a book
[5] Borrowers list
[6] Add a borrower
[7] Find a borrower """)