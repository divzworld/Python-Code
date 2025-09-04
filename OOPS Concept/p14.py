# Build a class `Library` using **Aggregation** and **Encapsulation** that manages a list of books with add/remove/display operations.
"""
Aggregation is a type of "has-a" relationship between two classes where:

One object uses another object.

But the used object can exist independently of the container.
"""


class Library :
    def __init__(self) :
        self.__library = ["Atomic Habits","Do epic shit","Ikigai","Before coffee gets cold","Think like a monk"]

    def addBook(self, bookname) :
        self.__library.append(bookname)
        return f"{bookname} Added successfully !"

    def removeBook(self, bookremove) :
        if bookremove in self.__library :
            self.__library.remove(bookremove)
            return f"{bookremove} Book removed successfully !"
        else :
            return f"{bookremove} Not Found !"

    def showBooks(self) :
        return "\n".join (f"-{book}" for book in self.__library)
    
    
class Books() :
    def __init__(self,library) :
        self.library = library # Aggregation

    def addBook(self, name) :
        return self.library.addBook(name)

    def removeBook(self, name) :
        return self.library.removeBook(name)

    def showBooks(self) :
        return self.library.showBooks()
    
lib = Library()
book = Books(lib)


"""
-------- Option Guide --------
1. Add Book
2. Remove Book
3. Books List Show
4. Exit
"""
while True :
    option = int(input(" Select option from 1 to 4 : "))
    if option == 1 :
        name = input(" Enter the name of book : ")
        result1 = book.addBook(name)
        print(result1)
    elif option == 2 :
        result2 = book.removeBook("Ikigai")
        print(result2)
    elif option == 3 :
        result3 = book.showBooks()
        print(result3)
    elif option == 4 :
        break
    else :
        print(" Invalid Option please enter in range 1 to 4 !")