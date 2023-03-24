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
                return 1
        print("Book doesn\'t found.")


    def find_borrower(self, name_of_the_borrower):
        for ind, borr in enumerate(self.borrowers):
            if borr.name == name_of_the_borrower:
                print("Borrower found! Displaying info...")
                inf = borr.info()
                print(f"""Name: {inf["name"]}
ID: {inf["id"]}
Borrowed books:""")
                for book in self.borrowers[ind].borrowed_books:
                    print(f"\t\t{book}")


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
                    self.books[ind].availability = False
                    for indx, borr in enumerate(self.borrowers):
                        if borr.name == name_of_borrower:
                            self.borrowers[indx].borrowed_books.append(book)
                    return 1
                else:
                    time.sleep(0.5)
                    print("Sorry, book is already taken.")
                    return 1
        time.sleep(0.5)
        print("Sorry, but book doesn't exist in library.")

    def return_book(self, title, author, name_of_borrower):
        print("Searching for a book...")
        for ind, book in enumerate(self.books):
            inf = book.info()
            if inf["Title"] == title and inf["Author"] == author:
                print("Book is found!")
                self.books[ind].availability = True
                for indx, borrower in enumerate(self.borrowers):
                    if borrower.name == name_of_borrower:
                        del self.borrowers[indx].borrowed_books[book]
                        return 1
        print("Book is not borrowed.")
        

library = Library()

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
        system('clear')
        print("""Our books in Library are now:
-------------------""")
        for book in library.books:   
            print(f"- '{book.title}' from {book.author}, ISBN {book.isbn}, available:{book.availability}")
        print("-------------------")
    elif option == "2":
        title = input("The title of the new book: ")
        author = input("The author of the new book: ")
        library.add_book(title, author)
        print (f"'{title}' from {author} is just added in Library.")
    elif option == "3":
        pass
    elif option == "4":
        pass
    elif option == "5":
        system('clear')
        print("""Our borrower in Library are now:
-------------------""")
        for borrower in library.borrowers:   
            print(f"{borrower.id} - {borrower.name}, {len(borrower.borrowed_books)} books borrowed.")
        print("-------------------")
    elif option == "6":
        name = input("The name of the new borrower: ")
        library.add_borrower(name)
        print (f"'{name}' is just added in Librarys list of debtors.")
    elif option == "7":
        pass
    if option != "8":
        input("Press Enter to continue...")
        continue
    elif option == "8":
        print("Thank you for visiting!")
        exit()
    else:
        print("Please enter just the above options!")
        time.sleep(2)
    
