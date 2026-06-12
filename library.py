from colorama import init, Fore, Style
import os
import time

init(autoreset=True)

BOOKS_FILE = "books.txt"
ISSUED_FILE = "issued_books.txt"


# Create files with default books
def initialize_files():
    if not os.path.exists(BOOKS_FILE):
        with open(BOOKS_FILE, "w") as file:
            file.write("""Python Programming
Data Science Basics
Artificial Intelligence
Machine Learning
Computer Networks
Database Management Systems
Operating Systems
Data Structures and Algorithms
Cloud Computing
Web Development
""")

    if not os.path.exists(ISSUED_FILE):
        open(ISSUED_FILE, "w").close()


# Loading Animation
def loading():
    print(Fore.YELLOW + "\nLoading", end="")
    for _ in range(3):
        time.sleep(0.4)
        print(".", end="")
    print("\n")


# Welcome Screen
def welcome():
    print(Fore.CYAN + Style.BRIGHT + """
╔════════════════════════════════════════════════════╗
║                                                    ║
║          📚 LIBRARY MANAGEMENT SYSTEM 📚           ║
║                                                    ║
║            Manage Your Books Efficiently          ║
║                                                    ║
║                Developed Using Python             ║
║                                                    ║
╚════════════════════════════════════════════════════╝
""")


# Menu
def menu():
    print(Fore.BLUE + "=" * 55)
    print(Fore.YELLOW + Style.BRIGHT + "                 MAIN MENU")
    print(Fore.BLUE + "=" * 55)

    print(Fore.GREEN + "1. ➕ Add Book")
    print(Fore.CYAN + "2. 📖 View Books")
    print(Fore.MAGENTA + "3. 🔍 Search Book")
    print(Fore.YELLOW + "4. 📤 Issue Book")
    print(Fore.BLUE + "5. 📥 Return Book")
    print(Fore.WHITE + "6. 📊 Statistics")
    print(Fore.RED + "7. ❌ Exit")

    print(Fore.BLUE + "=" * 55)


# Add Book
def add_book():
    book = input("\nEnter Book Name: ").strip()

    if book == "":
        print(Fore.RED + "❌ Book name cannot be empty!")
        return

    with open(BOOKS_FILE, "a") as file:
        file.write(book + "\n")

    print(Fore.GREEN + "✅ Book Added Successfully!")


# View Books
def view_books():
    with open(BOOKS_FILE, "r") as file:
        books = file.readlines()

    print(Fore.YELLOW + "\n📚 AVAILABLE BOOKS")
    print("-" * 40)

    if not books:
        print(Fore.RED + "No books available.")
        return

    for index, book in enumerate(books, start=1):
        print(Fore.WHITE + f"{index}. {book.strip()}")

    print("-" * 40)


# Search Book
def search_book():
    keyword = input("\nEnter Book Name to Search: ").lower()

    with open(BOOKS_FILE, "r") as file:
        books = file.readlines()

    found = False

    for book in books:
        if keyword in book.lower():
            print(Fore.GREEN + f"✅ Book Found: {book.strip()}")
            found = True

    if not found:
        print(Fore.RED + "❌ Book Not Found!")


# Issue Book
def issue_book():
    book_name = input("\nEnter Book Name to Issue: ")

    with open(BOOKS_FILE, "r") as file:
        books = file.readlines()

    updated_books = []
    found = False

    for book in books:
        if book.strip().lower() == book_name.lower():
            found = True
        else:
            updated_books.append(book)

    if found:
        with open(BOOKS_FILE, "w") as file:
            file.writelines(updated_books)

        with open(ISSUED_FILE, "a") as file:
            file.write(book_name + "\n")

        print(Fore.GREEN + "📤 Book Issued Successfully!")
    else:
        print(Fore.RED + "❌ Book Not Available!")


# Return Book
def return_book():
    book_name = input("\nEnter Book Name to Return: ")

    with open(ISSUED_FILE, "r") as file:
        issued_books = file.readlines()

    updated_issued = []
    found = False

    for book in issued_books:
        if book.strip().lower() == book_name.lower():
            found = True
        else:
            updated_issued.append(book)

    if found:
        with open(ISSUED_FILE, "w") as file:
            file.writelines(updated_issued)

        with open(BOOKS_FILE, "a") as file:
            file.write(book_name + "\n")

        print(Fore.GREEN + "📥 Book Returned Successfully!")
    else:
        print(Fore.RED + "❌ This Book Was Not Issued!")


# Statistics
def statistics():
    with open(BOOKS_FILE, "r") as file:
        available_books = len(file.readlines())

    with open(ISSUED_FILE, "r") as file:
        issued_books = len(file.readlines())

    total_books = available_books + issued_books

    print(Fore.MAGENTA + "\n📊 LIBRARY STATISTICS")
    print("-" * 40)
    print(Fore.GREEN + f"📚 Total Books     : {total_books}")
    print(Fore.CYAN + f"📖 Available Books : {available_books}")
    print(Fore.YELLOW + f"📤 Issued Books    : {issued_books}")
    print("-" * 40)


# Main Function
def main():
    initialize_files()
    welcome()

    while True:
        menu()

        choice = input(Fore.YELLOW + "\nEnter Your Choice: ")

        if choice == "1":
            loading()
            add_book()

        elif choice == "2":
            loading()
            view_books()

        elif choice == "3":
            loading()
            search_book()

        elif choice == "4":
            loading()
            issue_book()

        elif choice == "5":
            loading()
            return_book()

        elif choice == "6":
            loading()
            statistics()

        elif choice == "7":
            print(Fore.GREEN + "\n🙏 Thank You For Using Library Management System!")
            break

        else:
            print(Fore.RED + "❌ Invalid Choice! Please Try Again.")


if __name__ == "__main__":
    main()
