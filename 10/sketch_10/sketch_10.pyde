import unittest
class Library():
    availableBooks = list()
    def __init__(self, listOfBooks):
        self.availableBooks = listOfBooks
    def lendBook(self, requestedBook):
        if requestedBook in self.availableBooks:
            print("Customer have borrowed the book.")
            self.availableBooks.remove(requestedBook)
        else:
            print("Sorry, the book client want to boorow is not available in our list.")
    def displayAvailableBooks(self): # przejrzenie zasobu
        clear()
        for number, book in enumerate(self.availableBooks):
            text(book, 20, 20+number*20)
    def addBook(self, returnedBook): # przeywrócenie książki do zasobu
        if returnedBook:
            self.availableBooks.append(returnedBook)
            print("Client have returned the book. Thank You for using our service :)")
 
class Customer():
    book = ""
    haveBook = False
    def requestBook(self, book):
        print("Book You want to borrow is choosen.")
        self.book = book
        self.haveBook = True
        return self.book
    def returnBook(self):
        print("Book which you returning is {}".format(self.book))
        if self.haveBook:
            self.haveBook = False
            return self.book
        else:
            self.book = ""
            return False
 
 
def setup():
    if __name__ == '__main__':
        unittest.main()
 
    size(220,100)
 
def draw():
    library.displayAvailableBooks()
    fill(150)
    rect(100,10,100,20)
    rect(100,40,100,20)
    fill(250)
    text('wypozycz', 120,25)
    text('zwroc', 130, 55)
 
def mouseClicked():
    if mouseX >100 and mouseX<200:
        if mouseY >10 and mouseY <30:
            library.lendBook(Madzia.requestBook("Naocznosc"))
        if mouseY >40 and mouseY <60:
            library.addBook(Madzia.returnBook())
 
class Tests(unittest.TestCase):
    def test1(self):
        Madzia = Customer() # lepiej, gdy obiekty są definiowane bezpośrednio w testach, dzięki temu testy są neizależne od siebie
        self.assertEqual(Madzia.book, "")
    def test2(self):
        books = ["Naocznosc", "Sens Sztuki", "Harry Potter"]
        library = Library(books)
        self.assertTrue(len(library.availableBooks) > 0)
    def test3(self):
        books = ["Naocznosc", "Sens Sztuki", "Harry Potter"]
        library = Library(books)
        self.assertTrue(library.availableBooks[-1] == "Harry Potter") #zamiast podwójnego przeczenia...
        
#1,5pkt
