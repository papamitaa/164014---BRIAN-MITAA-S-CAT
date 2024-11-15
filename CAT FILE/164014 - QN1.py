class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def mark_as_borrowed(self):
        self.is_borrowed = True

    def mark_as_returned(self):
        self.is_borrowed = False

class LibraryMember:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if not book.is_borrowed:
            book.mark_as_borrowed()
            self.borrowed_books.append(book)
            print(f"{self.name} has taken '{book.title}'.")
        else:
            print(f"'{book.title}' has been taken by someone else.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.mark_as_returned()
            self.borrowed_books.remove(book)
            print(f"{self.name} has brought back'{book.title}'.")
        else:
            print(f"{self.name} hasn't returned '{book.title}'.")

    def list_borrowed_books(self):
        if self.borrowed_books:
            print(f"{self.name} has borrowed:")
            for book in self.borrowed_books:
                print(f"- {book.title}")
        else:
            print(f"{self.name} hasn't borrowed any books.")

# BOOKS AVAILABLE
book1 = Book("Chop Rice", "Scooby Doo")
book2 = Book("Enda Uoge", "Bugs Bunny")

# MEMBERS
member1 = LibraryMember("Jemo", "Member 1")
member2 = LibraryMember("Brian", "Member 2")

# MEMBER 1
member1.borrow_book(book1)  
member1.borrow_book(book2)     
member1.list_borrowed_books()   

# MEMBER 2
member2.borrow_book(book1)
member2.borrow_book(book2)  
member2.list_borrowed_books() 

# Bringing back book 1
member1.return_book(book1) 
member1.list_borrowed_books()

# Member 2 taking book 2 now
member2.borrow_book(book1)
member2.list_borrowed_books()
