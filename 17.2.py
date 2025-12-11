class Author:
    def __init__(self,name:str,country:str,birthday:str):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = []

    def __str__(self):
        return f"{self.name} ({self.country},{self.birthday})"

    def __repr__(self):
     return f"Author(name='{self.name}',country='{self.country}',birthday='{self.birthday}')"

class Book:
    total_books = 0

    def __init__(self,name:str,year:int,author:Author):
        if not isinstance(author,Author):
            raise TypeError("author must be an instance of Author class")

        self.name = name
        self.year = year
        self.author = author

        Book.total_books += 1
        author.books.append(self)

    def __str__(self):
        return f"{self.name}'({self.year}) by {self.author.name}"

    def __repr__(self):
        return f"Book(name='{self.name}',year={self.year},author='{self.author.name}')"

class Library:
    def __init__(self,name:str):
        self.name = name
        self.books = []
        self.authors = []

    def new_book(self,name:str,year:int,author:Author):
        if author not in self.authors:
            self.authors.append(author)

        book = Book(name,year,author)
        self.books.append(book)
        return book

