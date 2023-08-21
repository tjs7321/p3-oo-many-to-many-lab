class Author:

    all = []
    
    def __init__(self, name):
        self.name = name
        Author.all.append(self)

    def contracts(self):
        return [c for c in Contract.all if c.author == self]
    
    def books(self):
        return [b.book for b in Contract.all if b.author == self]
    
    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)
    
    def total_royalties(self):
        return sum([r.royalties for r in Contract.all if r.author == self])

class Book:
    
    all = []
    
    def __init__(self, title):
        self.title = title
        Book.all.append(self)
    
    def contracts(self):
        return [c for c in Contract.all if c.book == self]
    
    def authors(self):
        return [c.author for c in Contract.all if c.book == self]


class Contract:

    all = []
    
    def __init__(self, author, book, date, royalties):
        if isinstance(author, Author) and isinstance(book, Book):
            self.author = author
            self.book = book
        else: raise Exception("Must be author/book class.")
        if isinstance(date, str):
            self.date = date
        else: raise Exception("Date does not match date format")
        if isinstance(royalties, int):
            self.royalties = royalties
        else: raise Exception("Royalties value must be an integer.")
        Contract.all.append(self)

    @classmethod
    def contracts_by_date(cls):
        def date_sort(e):
            return e.date
        return sorted([c for c in cls.all], key=date_sort)