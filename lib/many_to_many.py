

class Author:
    all = []

    def __init__(self, name):
        self.name = name
        Author.all.append(self)

    # properties (validation) 
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise Exception("name must be a string")
        if len(value.strip()) == 0:
            raise Exception("name cannot be empty")
        self._name = value.strip()

    # relationship methods 
    def contracts(self):
        return [c for c in Contract.all if c.author is self]

    def books(self):
        books = [c.book for c in self.contracts()]
        unique = []
        for b in books:
            if b not in unique:
                unique.append(b)
        return unique

    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        return sum(c.royalties for c in self.contracts())


class Book:
    all = []

    def __init__(self, title):
        self.title = title
        Book.all.append(self)

    #  properties (validation)
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not isinstance(value, str):
            raise Exception("title must be a string")
        if len(value.strip()) == 0:
            raise Exception("title cannot be empty")
        self._title = value.strip()

    # relationship methods 
    def contracts(self):
        return [c for c in Contract.all if c.book is self]

    def authors(self):
        authors = [c.author for c in self.contracts()]
        unique = []
        for a in authors:
            if a not in unique:
                unique.append(a)
        return unique


class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

    #  properties (validation) 
    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise Exception("author must be an instance of Author")
        self._author = value

    @property
    def book(self):
        return self._book

    @book.setter
    def book(self, value):
        if not isinstance(value, Book):
            raise Exception("book must be an instance of Book")
        self._book = value

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        if not isinstance(value, str):
            raise Exception("date must be a string")
        if len(value.strip()) == 0:
            raise Exception("date cannot be empty")
        self._date = value.strip()

    @property
    def royalties(self):
        return self._royalties

    @royalties.setter
    def royalties(self, value):
        if not isinstance(value, int):
            raise Exception("royalties must be an integer")
        if value <= 0:
            raise Exception("royalties must be greater than 0")
        self._royalties = value

    # class method 
    @classmethod
    def contracts_by_date(cls, date):
        if not isinstance(date, str):
            raise Exception("date must be a string")
        return [c for c in cls.all if c.date == date]