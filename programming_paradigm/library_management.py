class Book:
    title,author
    _is_checked_out
    def __init__(self,title,author):
        self.title = title
        self.author = author
        self._is_checked_out = False 
    
    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        return not self._is_checked_out

class Library:
    def __init__(self):
        self._books = []

    def add_book(self,book):
        _books.append(book)
        print(f'Available books after setup:{self.title} by {self.author}')
        print(f'{self.title} by {self.author}')

    def check_out_book(self,title): 
        private_books.remove(self.title)
        self._is_checked_out = True
        print(f"Available books after checking out {self.title}:")

    def return_book(self,book):
        private_books.append(book.title)
        self._is_checked_out = False
        print(f"Available books after returning {self.title}:")
          for book in private_books:
            print(f'{book.title} by {book.author}')
      
    def list_available_books(self):
        for book in private_books:
            print(book)
