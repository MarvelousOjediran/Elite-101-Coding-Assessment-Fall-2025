from library_books import library_books
from datetime import datetime, timedelta

# -------- Level 1 --------
# TODO: Create a function to view all books that are currently available
# Output should include book ID, title, and author

def print_available_books(books_list):
    #prints any available books
    print("Available Books:")
    print(f"{'ID':<8} {'Title':<25} {'Author':<20}")
    #used to put margins between the categories
    print("-" * 60)

    for book in books_list:
        if book.get('available'):
            print(f"{book['id']:<8} {book['title']:<25} {book['author']:<20}")



print_available_books(library_books)

# -------- Level 2 --------
# TODO: Create a function to search books by author OR genre
# Search should be case-insensitive
# Return a list of matching books

def search_books(books):
    """Search books by author or genre (case-insensitive)."""
    term = input("Enter author or genre: ").lower()
    
    print(f"\nBooks matching")
    print(f"{'ID':<6} {'Title':<20} {'Author':<15} {'Genre':<12}")
    #used to put margins
    print("-" * 60)
    
    for book in books:
        author = book['author'].lower()
        genre = book['genre'].lower()
        #changes all book genres and authors to lowercase to match the input of the term

        if term in author or term in genre:
            print(f"{book['id']:<6} {book['title']:<20} {book['author']:<15} {book['genre']:<12}")
#if the term is in the author or genre  it will print


# -------- Level 3 --------
# TODO: Create a function to checkout a book by ID
# If the book is available:
#   - Mark it unavailable
#   - Set the due_date to 2 weeks from today
#   - Increment the checkouts counter
# If it is not available:
#   - Print a message saying it's already checked out

def checkout_book(books):
    """Check out a book by ID."""
    book_id = input("Enter book ID to checkout: ").strip()
    #collects book id of user

    # Find the book
    for book in books:
        if book['id'] == book_id.lower:
            if book['available']:
                # checks if id exists then its available or else it says not found
                book['available'] = False
                book['due_date'] = (datetime.now() + timedelta(weeks=2)).strftime('%Y-%m-%d')
                #if id exists and its available it changes the availability to false and gives it a 2 week due date 
                book['checkouts'] += 1
                print(f"Book '{book['title']}' checked out successfully!")
                print(f"Due date: {book['due_date']}")
                #says the book is checked out and displays new due date
            else:
                print(f"Book '{book['title']}' is already checked out.")
                print(f"Due date: {book['due_date']}") 

                #if book is already checked out it says then shows the due date
            return
    
    print("Book ID not found.")
checkout_book(library_books)
# -------- Level 4 --------
# TODO: Create a function to return a book by ID
# Set its availability to True and clear the due_date

def return_book(books):
    """Return a book by ID and reset its availability."""
    book_id = input("Enter book ID to return: ").strip()
    #gets book id from user input
    for book in books:
        if book['id'] == book_id:
            #if the book id exists and its not available it is now set to available because it is returned and change it to have no due date
            if not book['available']:
                book['available'] = True
                book['due_date'] = None
                print(f"Book '{book['title']}' returned successfully!")
            else:
                #if the book is already available it will just say its already avaiable
                print(f"Book '{book['title']}' is already available.")
            return
    
    print("Book ID not found.")




# TODO: Create a function to list all overdue books
# A book is overdue if its due_date is before today AND it is still checked out


def list_overdue_books(books):
    #sets the due date for books to today and makes an empty list
    today = datetime.now().strftime('%Y-%m-%d')
    overdue_books = []
    #checks  if books are not available and the due date is set to before today then adds the book to the empty list
    for book in books:
        if not book['available'] and book['due_date'] and book['due_date'] < today:
            overdue_books.append(book)


    #if the list exists with some values, it will prince all the over due books in the format of id, title, author, due date
    if overdue_books:
        print("Overdue Books:")
        print(f"{'ID':<6} {'Title':<20} {'Author':<15} {'Due Date':<12}")
        print("-" * 60)
        for book in overdue_books:
            print(f"{book['id']:<6} {book['title']:<20} {book['author']:<15} {book['due_date']:<12}")
    else:
        print("No overdue books found.")
        #if none of the books are overdue it will print no overdue books
# -------- Level 5 --------
# TODO: Convert your data into a Book class with methods like checkout() and return_book()
# TODO: Add a simple menu that allows the user to choose different options like view, search, checkout, return, etc.

# -------- Optional Advanced Features --------
# You can implement these to move into Tier 4:
# - Add a new book (via input) to the catalog
# - Sort and display the top 3 most checked-out books
# - Partial title/author search
# - Save/load catalog to file (CSV or JSON)
# - Anything else you want to build on top of the system!

if __name__ == "__main__":
    # You can use this space to test your functions
    pass
