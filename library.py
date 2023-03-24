from os import system
from book import Book
from borrower import Borrower
import time


system('clear')

class Library:
    def __init__(self):
        self.books = []
        self.borrowers = []

    def add_borrower(self, name):
        self.borrowers.append(Borrower(name, len(self.borrowers) + 1))

    def add_book(self, title, author):
        self.books.append(Book(title, author))

    def find_book(self, title, author):
        for book in self.books:
            if book.title == title and book.author == author:
                print("Book is found! Displaying an info..")
                inf = book.info()
                print(f"""Title: {inf["Title"]}
Author: {inf["Author"]}
ISBN: {inf["ISBN"]}
Availability: {inf["Availability"]}""")



    def loan_book(self, title, author, name_of_borrower):
        print('Searching for a book...')
        for ind, book in enumerate(self.books):
            info = book.info()
            if info["Title"] == title and info["Author"] == author:
                time.sleep(0.5)
                print("Book is found!\nChecking availability...")
                if info["Availability"]:
                    time.sleep(0.5)
                    print(f'Book is available!\nNow you borrowed book {info["Title"]} from {info["Author"]}!')
                    for inx, borr in enumerate(self.borrowers):
                        borr_inf = borr.info()
                        if borr_inf["name"] == name_of_borrower:
                            borr_inf
                    self.books[ind].availability = False
                    return 1
                else:
                    time.sleep(0.5)
                    print("Sorry, book is already taken.")
                    return 1
        time.sleep(0.5)
        print("Sorry, but book doesn't exist in library.")

    def return_book(self):
        pass
        
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