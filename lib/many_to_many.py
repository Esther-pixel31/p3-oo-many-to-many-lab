class Author:
    all = []
    def __init__(self, name):
        if not isinstance(name, str):
            raise Exception()
        self.name = name
        Author.all.append(self)
    
    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]
    
    def books(self):
        return [contract.book for contract in Contract.all if contract.author == self]
    
    def sign_contract(self, book, date, royalties):
        return Contract(self ,book, date, royalties)
    
    def total_royalties(self):
        return sum([contract.royalties for contract in self.contracts()])


class Book:
    all = []
    def __init__(self, title):
        if not isinstance(title, str):
            raise Exception()
        self.title = title
        Book.all.append(self)
        
    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]
    
    def authors(self):
        return [contract.author for contract in Contract.all if contract.book == self]


class Contract:
    all = []
    def __init__(self, author, book,date, royalties):
        if not isinstance(author, Author) or not isinstance(book, Book) or not isinstance(date, str) or not isinstance(royalties, int):
            raise Exception()
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        # author.sign_contract(book, date,royalties)
        Contract.all.append(self)
        
    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if contract.date == date]