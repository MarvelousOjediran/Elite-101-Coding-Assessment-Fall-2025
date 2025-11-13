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
        if book['id'] == book_id:
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

# -------- Level 4 --------
# TODO: Create a function to return a book by ID
# Set its availability to True and clear the due_date

# TODO: Create a function to list all overdue books
# A book is overdue if its due_date is before today AND it is still checked out


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
