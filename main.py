from typing import Optional


class Book:
    def __init__(self, id: int, name: str, pages: int):
        if not isinstance(id, int):
            raise TypeError("id should be int")
        if not isinstance(name, str):
            raise TypeError("name should be str")
        if not isinstance(pages, int):
            raise TypeError("pages should be int")

        if id < 0:
            raise ValueError("id should be >= 0")
        if pages < 0:
            raise ValueError("page should be >= 0")

        self.id = id
        self.name = name
        self.pages = pages

    def __str__(self):
        return f'Книга "{self.name}"'

    def __repr__(self):
        return f"Book(id={self.id}, name='{self.name}', pages={self.pages})"


class Library:
    def __init__(self, book_list: Optional[list[Book]] = None):
        if book_list is None:
            book_list = []

        if not isinstance(book_list, list):
            raise TypeError("Incorrect book_list type")

        if not all(isinstance(book, Book) for book in book_list):
            raise TypeError("Incorrect values type in book_list, should be Book")

        self.book_list = book_list

    def get_next_book_id(self) -> int:
        if not self.book_list:
            return 1
        last_book = self.book_list[-1]
        return last_book.id + 1

    def get_index_by_book_id(self, book_id: int) -> int:
        if not isinstance(book_id, int):
            raise TypeError("book_id should be int")
        if book_id < 0:
            raise ValueError("book_id should be >= 0")
        for index, book in enumerate(self.book_list):
            if book.id == book_id:
                return index
        raise ValueError("Книги с запрашиваемым id не существует")
