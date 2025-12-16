class Library:
    def __init__(self):
        self.books = []
    
    def add_book(self, book_title):
        self.books.append(book_title)
    
    def show_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            print("Books in library:")
            for i, book in enumerate(self.books, 1):
                print(f"{i}. {book}")


lib = Library()
lib.add_book("Python Crash Course")
lib.add_book("Clean Code")
lib.add_book("The Pragmatic Programmer")
lib.show_books()