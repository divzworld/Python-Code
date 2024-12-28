# que.  Create a simple menu-driven program for a library system.
class library :
    def __init__(self, books):
        self.books = books

    def book_available(self):
        print("\nAvailable Books:")
        for book in self.books:
            print(f"\t* {book}")

    def borrow_book(self, bookname):
        if bookname in self.books:
            print(f"\nYou have successfully borrowed the book: {bookname}")
            self.books.remove(bookname)
        else:
            print("\nSorry, this book is not currently available! Please check back later.")

    def return_book(self, bookname):
        self.books.append(bookname)
        print(f"\nThank you for returning the book: {bookname}")
        


if __name__ == "__main__" :
    obj = library(["Algorithms","DSA","Java","Python","C","CPP"])
    while (True) :
        """\n *** Welcome To Central Library ! ***
        Choose Your option wisely
        01 . To check available books 
        02 . To Borrow Book 
        03 . To Add/Return Book
        04 . Exit """
        try:
            choice = int(input("Enter your option: "))
            if choice == 1:
                obj.book_available()
            elif choice == 2:
                book_to_borrow = input("Enter the book name you want to borrow: ")
                obj.borrow_book(book_to_borrow)
            elif choice == 3:
                book_to_return = input("Enter the book name you want to return: ")
                obj.return_book(book_to_return)
            elif choice == 4:
                print("\nThank you for visiting Central Library. Goodbye!")
                break
            else:
                print("\nInvalid Option. Please choose a valid option.")
        except ValueError:
            print("\nInvalid Input. Please enter a number between 1 and 4.")