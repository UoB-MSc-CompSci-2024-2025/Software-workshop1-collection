from utils import user_message


def update_borrow_records(user, book, library_stocks):
    if user.borrowing_limit <= 3:
        for book_from_stock in library_stocks.books:
            if book.title == book_from_stock.title:
                if book_from_stock.available_copies > 0:
                    book_from_stock.borrow_book()
                    user.borrowed_books.append(book)
                    user.borrowing_limit -= 1
                else:
                    user_message('The stocks are not available for the book you are searching')
    else:
        user_message('You have exceeded the borrowing limit, sorry!\n'
                     'Please return the book which you completed the reading')


class User:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []
        self.borrowing_limit = 3

    def borrow(self, book, library_stocks, users):
        for user in users:
            if self.name == user.name:
                update_borrow_records(user, book, library_stocks)
                break
            else:
                users.append(self)
                update_borrow_records(self, book, library_stocks)
                break

    def return_book(self, book, library_stocks, users):
        returned = False

        for user in users:
            if self.name == user.name:
                for borrowed_book in user.borrowed_books:
                    if book.title.lower() == borrowed_book.title.lower():
                        user.borrowed_books.remove(book)
                        returned = True
                    else:
                        user_message(f'We think you are returning book which is not borrowed by this {user.name}')
                break

        if returned:
            for book_from_stock in library_stocks.books:
                if book.title.lower() == book_from_stock.title.lower():
                    book_from_stock.return_book()
