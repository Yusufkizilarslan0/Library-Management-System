class library:
    def __init__(self):
        self.file = open("books.txt","a+")

    def __del__(self):
        self.file.close()

    def list_books(self):
        self.file.seek(0)
        books = self.file.read().splitlines()
        if not books:
            print("No books available.")
        else:
            for book in books:
                book_info = book.split(",")
                print(f"Title: {book_info[0]}, Author: {book_info[1]}, Release Year: {book_info[2]}, Pages: {book_info[3]}")

    def add_book(self):
        title = input("Enter book title: ").title()
        author = input("Enter book author: ").title()
        release_year = input("Enter release year: ")
        pages = input("Enter number of pages: ")
        book_info = f"{title},{author},{release_year},{pages}\n"
        self.file.write(book_info)
        print("Book added successfully.")


    def remove_book(self):
        title = input("Enter the title of the book you want to remove: ").title()
        self.file.seek(0)
        books = self.file.read().splitlines()
        updated_books = [book for book in books if title not in book]
        self.file.seek(0)
        self.file.truncate()
        for book in updated_books:
            self.file.write(book + '\n')
            print("Book removed successfully.")

lib = library()

while True:
    print("*** MENU ***")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")
    print("4) press q to exit")
    choice = input("Enter your choice (1/2/3/4): ")

    if choice == "1":
        lib.list_books()
    elif choice == "2":
        lib.add_book()
    elif choice == "3":
        lib.remove_book()
    elif choice == "4" :
        break
    elif choice == "q":
        break
    else:
        print("Invalid choice. Please enter 1, 2, 3, 4, or q.")
