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
    
    def sign_contract(self, book, date, royalties):
        new_contract = Contract(self, book, date, royalties)
        return new_contract

    def total_royalties(self):
        total = 0
        for contract in self.contracts():
            total += contract.royalties
        return total



class Book:
    all = []
    def __init__(self, title):
        self.title = title

        Book.all.append(self)
    
    def contracts(self):
        book_contracts = []
        for contract in Contract.all:
            if contract.book == self:
                book_contracts.append(contract)
        return book_contracts


    def authors(self):
        book_authors = []
        for contract in self.contracts():
            book_authors.append(contract.author)
        return book_authors
    
        
class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise TypeError("author must be an instance of the Author class")
        self._author = value

    @property
    def book(self):
        return self._book

    @book.setter
    def book(self, value):
        if not isinstance(value, Book):
            raise TypeError("book must be an instance of the Book class")
        self._book = value

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        if not isinstance(value, str):
            raise TypeError("date must be an instance of a str")
        self._date = value

    @property
    def royalties(self):
        return self._royalties

    @royalties.setter
    def royalties(self, value):
        if not isinstance(value, int):
            raise TypeError("royalties must be an instance of an int")
        self._royalties = value

    @classmethod
    def contracts_by_date(cls, target_date):
        matching_contracts = []
        for contract in cls.all:
            if contract.date == target_date:
                matching_contracts.append(contract)
        return matching_contracts

        