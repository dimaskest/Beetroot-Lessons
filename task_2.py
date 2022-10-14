class Author:
    def __init__(self, name, country, birthday, books: list) -> None:
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = books

    def __str__(self) -> str:
        return f"{self.name}, {self.country}, {self.birthday}"


class Library:
    def __init__(self, name: str, books: list, authors: list) -> None:
        self.name = name
        self.books = books
        self.authors = authors

    def add_new_book(self, name: str, year: int, author: Author):
        book = Book(name, year, author)
        self.books.append(book)
        return book

    def group_by_author(self, auth: Author):
        return [book for book in self.books if book.author == auth]

    def group_by_year(self, year: int):
        return [book for book in self.books if book.year == year]

    def __str__(self) -> str:
        return f"Library name is {self.name}, books: {self.books} by authors {self.authors}"


class Book:
    def __init__(self, name, year, author: Author) -> None:
        self.name = name
        self.year = year
        self.author = author

    def __str__(self) -> str:
        return f"{self.name}, {self.year}, {self.author}"


auth = Author("Dmytro", "Ukraine", "08.08.2022", [])
auth2 = Author("Ivan", "Ukraine", "10.10.2022", [])

library = Library("Library", [], [])
library.add_new_book("qwerty", 1900, auth)
library.add_new_book("1984", 1900, auth2)

for book in library.group_by_year(1900):
    print(book)