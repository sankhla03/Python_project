
class Library:
    def __init__ (self):
        self.noOfbook = 0
        self.books = []

    def addbook(self, name):
        self.books.append(name)
        self.noOfbook = len(self.books) 

    def showinfo(self):
        print(f"the library has {self.noOfbook}books, the books as ")
        for i in self.books:
            print(i)

l = Library()
l.addbook("Ashok")
l.addbook("Ashok1")
l.addbook("Ashok2")
l.addbook("Ashok3")
l.showinfo()