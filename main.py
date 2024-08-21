from storage import Storage
from book_manager import BookManager
from user_manager import UserManager
from checking import CheckManager
from library import Library
import cli
from logger import logger

def main():
    storage = Storage()
    book_manager = BookManager(storage)
    user_manager = UserManager(storage)
    check_manager = CheckManager(storage)
    library = Library(book_manager, user_manager,check_manager)

    while True:
        cli.main_menu()
        choice = input("Select an option: ")
        
        if choice == "1":
            manage_books(book_manager)
        elif choice == "2":
            manage_users(user_manager)
        elif choice == "3":
            check_out_book(library)
        elif choice == "4":
            check_in_book(library)
        elif choice == "5":
            track_book_availability(library)
        elif choice == "0":
            break

def manage_books(book_manager:BookManager):
    while True:
        cli.book_menu()
        choice = input("Select an option: ")
        
        if choice == "1":
            title = input("Enter title: ")
            author = input("Enter author: ")
            isbn = int(input("Enter ISBN: "))
            book_manager.add_book(title, author, isbn)
            logger.info("Book entry added")
        elif choice == "2":
            isbn = int(input("Enter ISBN: "))
            title = input("Enter new title (or leave empty to keep unchanged): ")
            author = input("Enter new author (or leave empty to keep unchanged): ")
            book_manager.update_books(isbn, title, author)
            logger.info("Book entry updated")
        elif choice == "3":
            isbn = int(input("Enter ISBN: "))
            book_manager.delete_books(isbn)
            logger.info("Book entry deleted")
        elif choice == "4":
            books = book_manager.list_books()
            print(books)
        elif choice == "5":
            title = input("Enter title: ")
            books = book_manager.find_books_by_title(title)
            print(books)
        elif choice == "6":
            author = input("Enter author: ")
            books = book_manager.find_books_by_author(author)
            print(books)
        elif choice == "7":
            author = input("Enter ISBN: ")
            books = book_manager.find_books_by_isbn(author)
            print(books)
        elif choice == "0":
            break

def manage_users(user_manager:UserManager):
    while True:
        cli.user_menu()
        choice = input("Select an option: ")
        
        if choice == "1":
            name = input("Enter name: ")
            user_id = input("Enter user ID: ")
            user_manager.add_user(user_id,name)
            logger.info("User entry added")
        elif choice == "2":
            user_id = input("Enter user ID: ")
            name = input("Enter new name (or leave empty to keep unchanged): ")
            user_manager.update_user(user_id, name)
            logger.info("user entry updated")
        elif choice == "3":
            user_id = input("Enter user ID: ")
            user_manager.delete_user(user_id)
            logger.info("user entry deleted")
        elif choice == "4":
            users = user_manager.list_users()
            print(users)
        elif choice == "5":
            user_id = input("Enter user ID: ")
            result=user_manager.find_user_by_id(user_id)
            print(result)
        elif choice == "0":
            break

def check_out_book(library:CheckManager):
    user_id = input("Enter user ID: ")
    isbn = int(input("Enter ISBN of the book to check out: "))
    success = library.check_out_book(isbn,user_id)
    if success:
        print("Book checked out successfully!")
    else:
        print("Unable to check out the book. Please check the user ID and ISBN.")

def check_in_book(library:CheckManager):
    # user_id = input("Enter user ID: ")
    isbn = int(input("Enter ISBN of the book to check in: "))
    success = library.check_in_book(isbn)
    if success:
        print("Book checked in successfully!")
    else:
        print("Unable to check in the book. Please check the user ID and ISBN.")

def track_book_availability(library:Library):
    name = input("Enter name to check availability: ")
    availability = library.check_availability(name)
    # if len(availability)>0:
    #     print(f"Book is {'available' if availability else 'not available'}.")
    # else:
    #     print("Book not found.")
    print(availability)

if __name__ == "__main__":
    main()