class Book:
    public title,author
    private _is_checked_out
    def __init__(self,title,author):
        self.title = title
        self.author = author
        self._is_checked_out = False 

class Library(Book):
    def __init__(self):
        self._books = []
    def add_book(self):
        private_books.append(self.title)
        print(f'{self.title} by {self.author}')

    def check_out_book(self,title): 
        private_books.remove(self.title)
        self._is_checked_out = True

    def return_book(self,title):
        private_books.append(self.title)
        self._is_checked_out = False
        print(f'{self.title} by {self.author}')

    def list_available_books(self):
        for book in private_books:
            print(book)
