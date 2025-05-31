#A- Library Management System
# Sierra ILS

# Class Book:(option 1 in menu sub-system)
class Book:
    Library_name = "Sierra ILS"  # attribute with constant value ,and cannot be changed.
    books = []  # list to store all books

    # Initialize book details.
    def __init__(self, book_ID, title, price, author, pages, publication_date, year):
        self.__book_ID = book_ID # private member. (private attribute)
        self.title = title      
        self.price = price
        self.author = author
        self.pages = pages
        self.publication_date = publication_date
        self.year = year

    # Add book details.
    def add_book(self):
        print("\n    ============== Adding New Book ==============")
        self.__book_ID = int(input("\n    Enter the book ID: "))
        self.title = input("    Enter the title of the book: ")
        self.price = float(input("    Enter the price of the book: "))
        self.author = input("    Enter the author of the book: ")
        self.pages = int(input("    Enter the number of pages in the book: "))
        self.publication_date = input("    Enter the publication date of the book [dd/mm/yyyy]: ")
        self.year = int(input("    Enter the year of publication: "))
        print("    ============================================")
        Book.books.append(self)  # Add the book to the list

    # Display book details.
    def book_details(self):
        print("\n    =================== Book Details ==================")
        details = [
            f"\n    Library Name: {self.Library_name}", 
            f"\n    Book ID: {self.__book_ID}", 
            f"\n    Title: {self.title}", 
            f"\n    Price: {self.price}", 
            f"\n    Author: {self.author}", 
            f"\n    Pages: {self.pages}", 
            f"\n    Publication Date: {self.publication_date}", 
            f"\n    Year: {self.year}"
        ]
        for detail in details:
            print(detail)
        print("    =================================================")

    # Display all books
    @classmethod
    def display_all_books(cls):
        if not cls.books:
            print("\n    No books available in the library!")
            return
            
        print("\n    ============== All Books in Library ==============")
        for i, book in enumerate(cls.books, 1):
            print(f"\n    Book {i}:")
            print(f"    Title: {book.title}")
            print(f"    Author: {book.author}")
            print(f"    Book ID: {book._Book__book_ID}")
        print("\n    =================================================")

    # Change book ID.
    def change_book_id(self, new_id):
        self.__book_ID = new_id
        print(f"Book ID updated to: {self.__book_ID}")
    
# Class EBook(Book):(option 2 in menu sub-system)
class EBook(Book):
    def __init__(self, book_ID, title, price, author, pages, publication_date, year):
        super().__init__(book_ID, title, price, author, pages, publication_date, year)
        self.file_size = 0
        self.number_of_copies = 0
        self.format = "PDF"  # Default format
        EBook.books = []  # list to store all ebooks

    # Add EBook details.
    def add_book(self):
        super().add_book()
        print("\n    ============== Adding EBook Details ==============")
        self.file_size = float(input("\n    Enter the file size of the book: "))
        self.number_of_copies = int(input("    Enter the number of copies: "))
        self.format = input("    Enter the format of the ebook (PDF, EPUB, etc.): ")
        print("    =================================================")
        EBook.books.append(self)  # Add the ebook to the list

    # Display EBook details.
    def book_details(self):
        super().book_details()
        print("\n    ============== EBook Specific Details ==============")
        print(f"\n    File Size: {self.file_size} MB")
        print(f"    Format: {self.format}")
        print(f"    Total Size: {self.compute_file_size()} MB")
        print("    =================================================")
    
    # Compute the total size of the EBook.
    def compute_file_size(self):
        self.total_size = self.file_size * self.number_of_copies
        return self.total_size
    
    # Change the EBook ID.
    def change_book_id(self, new_id):
        super().change_book_id(new_id)

# Helper to display list of books/ebooks
def display_books_list(books_list, is_ebook=False):
    if not books_list:
        print("\n    No books available!")
        return False
        
    print("\n    ============== All Books in Library ==============")
    for i, book in enumerate(books_list, 1):
        print(f"\n    {'E' if is_ebook else ''}Book {i}:")
        print(f"    Title: {book.title}")
        print(f"    Author: {book.author}")
        print(f"    Book ID: {book._Book__book_ID}")
        if is_ebook:
            print(f"    Format: {book.format}")
            print(f"    File Size: {book.file_size} MB")
    print("\n    =================================================")
    return True

# Book subsystem menu
def book_subsystem(book):
    while True:
        print("\n" + "  =================================================================")
        print("                      BOOK SUBSYSTEM MENU:")
        print("  =================================================================")
        
        # Menu options as a list
        book_options = [
            "Add new Book",
            "Display Book Details",
            "Change/Edit book_ID",
            "Exit the sub-system",
            "Exit the Library Management System"
        ]
        
        # Display menu options from the list
        for i, option in enumerate(book_options):
            print(f"    {i+1}. {option}")
            
        print("\n  =================================================================")
        
        option = input("    Enter your choice (1-5): ")
        if not option.isdigit():
            print("\n    Please enter a valid number!")
            continue
            
        option = int(option)
        if option == 1:
            print("\n    Adding a new book...")
            new_book = Book(0, "", 0, "", 0, "", 0)
            new_book.add_book()
            print("\n    Book added successfully!")
            
        elif option == 2:
            if display_books_list(Book.books):
                book_num = input("\n    Enter the book number to display details (or press Enter to skip): ")
                if book_num.isdigit():
                    book_num = int(book_num)
                    if 1 <= book_num <= len(Book.books):
                        Book.books[book_num-1].book_details()
                    else:
                        print("\n    Invalid book number!")
            
        elif option == 3:
            if display_books_list(Book.books):
                book_num = input("\n    Enter the book number to change ID: ")
                if book_num.isdigit():
                    book_num = int(book_num)
                    if 1 <= book_num <= len(Book.books):
                        new_id = input("    Enter new book ID: ")
                        if new_id.isdigit():
                            Book.books[book_num-1].change_book_id(int(new_id))
                        else:
                            print("\n    Please enter a valid book ID!")
                    else:
                        print("\n    Invalid book number!")
                else:
                    print("\n    Please enter a valid number!")
            
        elif option == 4:
            print("\n    Exiting Book subsystem...")
            return
            
        elif option == 5:
            print("\n    Exiting Library Management System...")
            break
            
        else:
            print("\n    Invalid option! Please enter a number between 1-5.")

# EBook subsystem menu
def ebook_subsystem(ebook):
    while True:
        print("\n" + "  =================================================================")
        print("                     EBOOK SUBSYSTEM MENU:")
        print("  =================================================================")
        print()
        
        # Menu options as a list
        ebook_options = [
            "Add new EBook",
            "Display EBook Details",
            "Change/Edit file_size",
            "Check file_size and format",
            "Compute total file size",
            "Exit the sub-system",
            "Exit the Library Management System"
        ]
        
        # Display menu options from the list
        for i, option in enumerate(ebook_options):
            print(f"    {i+1}. {option}")
        
        print("\n  =================================================================")
        print()
        
        option = input("    Enter your choice (1-7): ")
        if not option.isdigit():
            print("\n    Please enter a valid number!")
            continue
            
        option = int(option)
        if option == 1:
            print("\n    Adding a new ebook...")
            new_ebook = EBook(0, "", 0, "", 0, "", 0)
            new_ebook.add_book()
            print("\n    EBook added successfully!")
            
        elif option == 2:
            if display_books_list(EBook.books, True):
                book_num = input("\n    Enter the ebook number to display details (or press Enter to skip): ")
                if book_num.isdigit():
                    book_num = int(book_num)
                    if 1 <= book_num <= len(EBook.books):
                        EBook.books[book_num-1].book_details()
                    else:
                        print("\n    Invalid ebook number!")
            
        elif option == 3:
            if display_books_list(EBook.books, True):
                book_num = input("\n    Enter the ebook number to change file size: ")
                if book_num.isdigit():
                    book_num = int(book_num)
                    if 1 <= book_num <= len(EBook.books):
                        new_size = input("    Enter new file size (MB): ")
                        if new_size.replace('.', '').isdigit():
                            EBook.books[book_num-1].file_size = float(new_size)
                            print(f"\n    File size updated to {new_size} MB")
                        else:
                            print("\n    Please enter a valid file size!")
                    else:
                        print("\n    Invalid ebook number!")
                else:
                    print("\n    Please enter a valid number!")
            
        elif option == 4:
            if display_books_list(EBook.books, True):
                book_num = input("\n    Enter the ebook number to check file info: ")
                if book_num.isdigit():
                    book_num = int(book_num)
                    if 1 <= book_num <= len(EBook.books):
                        print("\n    ============== File Information ==============")
                        print(f"    File Size: {EBook.books[book_num-1].file_size} MB")
                        print(f"    Format: {EBook.books[book_num-1].format}")
                        print("    ============================================")
                    else:
                        print("\n    Invalid ebook number!")
                else:
                    print("\n    Please enter a valid number!")
            
        elif option == 5:
            if display_books_list(EBook.books, True):
                book_num = input("\n    Enter the ebook number to compute total size: ")
                if book_num.isdigit():
                    book_num = int(book_num)
                    if 1 <= book_num <= len(EBook.books):
                        copies = input("    Enter number of copies: ")
                        if copies.isdigit():
                            copies = int(copies)
                            EBook.books[book_num-1].number_of_copies = copies
                            total = EBook.books[book_num-1].compute_file_size()
                            print(f"\n    Total file size for {copies} copies: {total} MB")
                        else:
                            print("\n    Please enter a valid number of copies!")
                    else:
                        print("\n    Invalid ebook number!")
                else:
                    print("\n    Please enter a valid number!")
            
        elif option == 6:
            print("\n    Exiting EBook subsystem...")
            return
            
        elif option == 7:
            print("\n    Exiting Library Management System...")
            break
        else:
            print("\n    Invalid option! Please enter a number between 1-7.")

# Improve the choose_system function to use if conditions
def choose_system():
    Library_name = Book.Library_name
    sub_system = ["Book", "EBook", "Exit the system"]
    
    while True:
        print("\n" + "  =================================================================")
        print(f"==================== WELCOME TO {Library_name} ==========================")
        print("  =================================================================")
        
        for i in range(len(sub_system)):
            print(f"    {i+1}. {sub_system[i]}")
            
        print("\n  =================================================================")

        
        choice = input("    Enter your choice: ")
        if not choice.isdigit():
            print("\n    Please enter a valid number!")
            continue
            
        choice = int(choice)
        if choice == 1:
            print("\n    Entering Book subsystem...")
            book = Book(0, "", 0, "", 0, "", 0)
            book_subsystem(book)
            
        elif choice == 2:
            print("\n    Entering EBook subsystem...")
            ebook = EBook(0, "", 0, "", 0, "", 0)
            ebook_subsystem(ebook)
            
        elif choice == 3:
            print("\n    Thank you for using Sierra ILS!")
            break
        else:
            print("\n    Invalid choice! Please enter a number between 1-3.")

choose_system()

