class Book:
    def __init__(self, title, author=None, total_copies=None, available_copies =None):
        self.title = title
        self.author = author
        self.total_copies = total_copies
        self.available_copies = available_copies

    def borrow_book(self):
        self.available_copies -= 1

    def return_book(self):
        self.available_copies += 1
