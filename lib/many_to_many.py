class Author:
    all = []

    def __init__(self, name):
        self.name = name

        Author.all.append(self)
    
    def contracts(self):
        author_contracts = []
        for contract in Contract.all:
            if contract.author == self:
                author_contracts.append(contract)
        return author_contracts
    
    def books(self):
        author_books = []
        for contract in self.contracts():
            author_books.append(contract.book)
        return author_books
    
    def sign_contracts(self, book, date, royalties):
        new_contract = Contract(self, book, date, royalties)
        return new_contract

    def total_royalties(self):
        pass
    
       


class Book:
    all = []
    def __init__(self, title):
        self.title = title

        Book.all.append(self)
    
        

class Contract:
    all = []
    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date =  date
        self.royalties = royalties

        Contract.all.append(self)
        