from utils import *


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def add_bulk_book(self, list_of_books):
        self.books.extend(list_of_books)

    def display_books(self):
        user_message('=== The available books in the library ===')
        for book in self.books:
            user_message(f'The {book.title} has {book.available_copies} copies in the rack ')
