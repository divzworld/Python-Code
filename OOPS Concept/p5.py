# Create a class `Book` with a method to set and get book details. Use **Getter and Setter methods** to access private variables.
class Book :
    def __init__(self, bookName, bookAuthor, price, language) :
        self.__bookName = bookName
        self.__bookAuthor = bookAuthor
        self.__price = price
        self.__language = language

    # getter method
    @property    
    def bookDetails (self) -> str :
        return f"{self.__bookName},{self.__bookAuthor},{self.__price},{self.__language}"


    # setter method - setter can access only one value and does not return value
    @bookDetails.setter
    def bookDetails (self,details : dict) -> dict :
        if not isinstance(details, dict): # Datatype should be dictionary only
            raise TypeError("Details must be provided as a dictionary.")
        
        self.__bookName = details.get("bookName", self.__bookName)
        self.__bookAuthor = details.get("bookAuthor", self.__bookAuthor)
        self.__price = details.get("price", self.__price)
        self.__language = details.get("language", self.__language)


    def __str__(self) :
        return f"Book Name :{self.__bookName},\tBook Author :{self.__bookAuthor},\tPrice :{self.__price},\tLanguage :{self.__language}"


obj = Book("Atomic Habits", "James Clear", 12.99, "English")
print(obj)

obj.bookDetails = {
    "bookName": "Ikigai",
    "bookAuthor": "Héctor García",
    "price": 9.99,
    "language": "English"
}
print(obj)

obj.bookDetails = {
    "bookName": "The Power of Now",
    "bookAuthor": "Eckhart Tolle",
    "price": 14.99,
    "language": "English"
}
print(obj)

obj.bookDetails = {
    "bookName": "Rich Dad Poor Dad",
    "bookAuthor": "Robert T. Kiyosaki",
    "price": 10.50,
    "language": "English"
}
print(obj)