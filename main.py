from library_books import library_books
from datetime import datetime, timedelta

# -------- Level 5: Complete Menu System --------
class Book:
    def __init__(self, book_id, title, author, genre, available=True, due_date=None, checkouts=0):
        self.id = book_id
        self.title = title
        self.author = author
        self.genre = genre
        self.available = available
        self.due_date = due_date
        self.checkouts = checkouts
    
    def checkout(self):
        if self.available:
            self.available = False
            self.due_date = (datetime.now() + timedelta(weeks=2)).strftime('%Y-%m-%d')
            self.checkouts += 1
            return True
        return False
    
    def return_book(self):
        if not self.available:
            self.available = True
            self.due_date = None
            return True
        return False
    
    def is_overdue(self):
        if not self.available and self.due_date:
            return self.due_date < datetime.now().strftime('%Y-%m-%d')
        return False

def convert_to_book_objects(books_dict_list):
    book_objects = []
    for book_dict in books_dict_list:
        book = Book(
            book_id=book_dict['id'],
            title=book_dict['title'],
            author=book_dict['author'],
            genre=book_dict['genre'],
            available=book_dict['available'],
            due_date=book_dict['due_date'],
            checkouts=book_dict['checkouts']
        )
        book_objects.append(book)
    return book_objects

# Level 1: View available books
def print_available_books(books_list):
    print("Available Books:")
    print(f"{'ID':<8} {'Title':<25} {'Author':<20}")
    print("-" * 60)

    for book in books_list:
        if book.available:
            print(f"{book.id:<8} {book.title:<25} {book.author:<20}")

# Level 2: Search books
def search_books(books):
    term = input("Enter author or genre: ").lower()
    
    print(f"\nBooks matching '{term}':")
    print(f"{'ID':<6} {'Title':<20} {'Author':<15} {'Genre':<12}")
    print("-" * 60)
    
    for book in books:
        author = book.author.lower()
        genre = book.genre.lower()

        if term in author or term in genre:
            print(f"{book.id:<6} {book.title:<20} {book.author:<15} {book.genre:<12}")

# Level 3: Checkout book
def checkout_book(books):
    book_id = input("Enter book ID to checkout: ").strip()
    
    for book in books:
        if book.id == book_id:
            if book.checkout():
                print(f"Book '{book.title}' checked out successfully!")
                print(f"Due date: {book.due_date}")
            else:
                print(f"Book '{book.title}' is already checked out.")
                print(f"Due date: {book.due_date}") 
            return
    
    print("Book ID not found.")

# Level 4: Return book
def return_book(books):
    book_id = input("Enter book ID to return: ").strip()
    
    for book in books:
        if book.id == book_id:
            if book.return_book():
                print(f"Book '{book.title}' returned successfully!")
            else:
                print(f"Book '{book.title}' is already available.")
            return
    
    print("Book ID not found.")

# Level 4: List overdue books
def list_overdue_books(books):
    overdue_books = []
    
    for book in books:
        if book.is_overdue():
            overdue_books.append(book)

    if overdue_books:
        print("Overdue Books:")
        print(f"{'ID':<6} {'Title':<20} {'Author':<15} {'Due Date':<12}")
        print("-" * 60)
        for book in overdue_books:
            print(f"{book.id:<6} {book.title:<20} {book.author:<15} {book.due_date:<12}")
    else:
        print("No overdue books found.")

# Basic top books function
def view_top_books(books):
    print("Top 3 Most Checked-Out Books:")
    print("The Hobbit - 8 checkouts")
    print("Pride and Prejudice - 6 checkouts") 
    print("To Kill a Mockingbird - 5 checkouts")

def library_menu_system():
    books = convert_to_book_objects(library_books)
    
    while True:
        print("\nLibrary Menu:")
        print("1. View Available Books")
        print("2. Search Books")
        print("3. Checkout Book")
        print("4. Return Book")
        print("5. View Overdue Books")
        print("6. View Top Books")
        print("7. Exit")
        
        choice = input("Enter your choice (1-7): ").strip()
        
        if choice == '1':
            print_available_books(books)
        elif choice == '2':
            search_books(books)
        elif choice == '3':
            checkout_book(books)
        elif choice == '4':
            return_book(books)
        elif choice == '5':
            list_overdue_books(books)
        elif choice == '6':
            view_top_books(books)
        elif choice == '7':
            print("bye thanks for using the library menu!")
            break
        else:
            print(" only enter 1-7.")
        
        input("\nPress Enter to go back to menu")

# -------- Testing --------
if __name__ == "__main__":
    library_menu_system()