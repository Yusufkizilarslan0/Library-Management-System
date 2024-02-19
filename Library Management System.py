
class Library:
    def __init__(self):
        self.file = open("books.txt", "a+")

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
                print(f"Title: {book_info[0]}, Author: {book_info[1]}")

    def add_book(self):
        title = input("Enter book title: ").title()
        author = input("Enter book author: ").title()
        release_year = input("Enter release year: ")

        if len(release_year) != 4:
            print("Please enter a 4-digit number.")
            return
        else:
            print("Please wait.")

        try:
            released_year = int(release_year)
        except ValueError:
            print("Invalid input! Please use an integer for the release year.")
            return

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
        for i in updated_books:
            self.file.write(i + '\n')
        if title not in books:
            print("Book not found. Please check the title and try again.")
        else:
            print("Book removed successfully.")

    def all_remove_book(self):
        correct_password = 1234
        entered_password = int(input("If you want to delete all books, please enter the password: "))
        if entered_password == correct_password:
            self.file.seek(0)
            self.file.truncate()
            print("All books removed.")
        else:
            print("Wrong password!")

lib = Library()

while True:
    print("*** MENU ***")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")
    print("4) Press 'q' to exit")
    print("5) All Remove Books")
    choice = input("Enter your choice (1/2/3/4): ")

    if choice == "1":
        lib.list_books()
    elif choice == "2":
        lib.add_book()
    elif choice == "3":
        lib.remove_book()
    elif choice == "q":
        break
    elif choice == "5":
        lib.all_remove_book()
    else:
        print("Invalid choice. Please enter 1, 2, 3, 4, or q.")
