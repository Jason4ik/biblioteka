class Borrower:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.borrowed_books = []

    def info(self):
        return {'name': self.name, 'id':self.id}

