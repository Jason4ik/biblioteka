from os import system
from book import Book
from borrower import Borrower
import time


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
    system('clear')
    print("""LIBRARY MENU:
-------------------
[1] Books list
[2] Add a book
[3] Find a book
[4] Loan a book
[5] Borrowers list
[6] Add a borrower
[7] Find a borrower
[8] Exit
-------------------""")
    option = input("Select your option: ")
    if option == "1":
        pass
    elif option == "2":
        pass
    elif option == "3":
        pass
    elif option == "4":
        pass
    elif option == "5":
        pass
    elif option == "6":
        pass
    elif option == "7":
        pass
    elif option == "8":
        pass
    else:
        print("Please enter just the above options!")
        time.sleep(2)
    
