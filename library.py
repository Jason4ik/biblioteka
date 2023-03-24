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
        print('Searching for a book...')
        for ind, book in enumerate(self.books):
            info = book.info()
            if info["Title"] == title and info["Author"] == author:
                print("Book is found!\nChecking availability...")
                if info["Availability"]:
                    print(f'Book is available!\nNow you borrowed book {info["Title"]} from {info["Author"]}!')
                    self.books[ind].availability = False
                    return 1
                else:
                    print("Sorry, book is already taken.")
                    return 1
        print("Sorry, but book doesn't exist in library.")
        
# MENU HERE
while True:
    print("""LIBRARY MENU:
[1] Books list
[2] Add a book
[3] Find a book
[4] Loan a book
[5] Borrowers list
[6] Add a borrower
[7] Find a borrower
[8] Exit""")