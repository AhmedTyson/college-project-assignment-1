# Library Management System using Python (OOP)

A console-based library management system built with Python, utilizing object-oriented programming principles. This project enables users to manage both physical books and ebooks, providing an interactive menu-driven interface for adding, viewing, and editing book and ebook details.

---

## Features

- **Book Management**
  - Add new books with details (ID, title, author, price, pages, publication date, year)
  - Display all books or specific book details
  - Edit book IDs

- **EBook Management**
  - Add new ebooks with additional attributes (file size, number of copies, format)
  - Display all ebooks or specific ebook details
  - Edit ebook file size
  - Check ebook file size and format
  - Compute total file size for multiple copies

- **User-Friendly Menus**
  - Separate subsystems for books and ebooks
  - Clear, interactive prompts for all operations

---

## Usage Example

1. **Start the program**  
   Run the script in your terminal:
   ```
   python Sierra_ILS.py
   ```

2. **Main Menu**  
   Select a subsystem:
   ```
   ==================== WELCOME TO Sierra ILS ==========================
       1. Book
       2. EBook
       3. Exit the system
   Enter your choice: 1
   ```

3. **Book Subsystem Example**  
   ```
   ==================== BOOK SUBSYSTEM MENU ============================
       1. Add new Book
       2. Display Book Details
       3. Change/Edit book_ID
       4. Exit the sub-system
       5. Exit the Library Management System
   Enter your choice (1-5): 1
   ```

4. **EBook Subsystem Example**  
   ```
   =================== EBOOK SUBSYSTEM MENU ============================
       1. Add new EBook
       2. Display EBook Details
       3. Change/Edit file_size
       4. Check file_size and format
       5. Compute total file size
       6. Exit the sub-system
       7. Exit the Library Management System
   Enter your choice (1-7): 1
   ```

---

Feel free to explore the menus to add, view, and manage your library's books and ebooks!
