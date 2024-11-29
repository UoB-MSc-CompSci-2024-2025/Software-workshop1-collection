from user import *
from library import *
from book import *

# User's list
user1 = User(name='Logesh')
user2 = User(name='Sharma')
user_list = [user1, user2]

# Load books to the library stock
library_stock = Library()
# books to add
book1 = Book(title='Computer system', author='Todd', total_copies=1, available_copies=1)
book2 = Book(title='SWW1', author='Jacqui', total_copies=10, available_copies=10)
book3 = Book(title='AIML', author='Max', total_copies=20, available_copies=20)

library_stock.add_bulk_book([book2, ])

if __name__ == '__main__':
    # display books
    library_stock.display_books()

    # create users

    # Borrow books
    user_borrowing_book = Book(title='SWW1')

    # user 1 Borrow books
    user1.borrow(user_borrowing_book, library_stock, user_list)

    # user 2 Borrow books
    user2.borrow(user_borrowing_book, library_stock, user_list)

    library_stock.display_books()

    user1.return_book(user_borrowing_book, library_stock, user_list)

    library_stock.display_books()
