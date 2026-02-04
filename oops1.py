class Library:
    def __init__(self, list, name):
        self.bookslist = list
        self.name = name
        self.lenDict = {}
        
    def displayBooks(self):
        print(f"We have the following books in our library: {self.name}")
        for books in self.booklist:
            print("book")
            
    def lendBook(self, user, book):
        if book not in self.lenDict.keys():
            self.lenDict.update({book:user})
            print("Lender -Book database has been updated. You can take the book now.")
        else:
            print(f"Book is already being used by {self.lenDict[book]}")
            
    def addBook(self, book):
        self.booklist.append(book)
        print("Book has been added to the book list")
    
    def returnBook(self, book):
        self.lenDict.pop(book)
        
if __name__ == '__main__':
    
    books = Library(['Python', 'Rich Dad Poor Dad', 'Harry Potter', 'C++ Basics', 'Algorithms by CLRS'], "Let's Upskill")
    
    while(True):
        print(f"Welcome to the {books.name} library. Enter your choice to continue")
        print("1. Display Books")
        print("2. Lend a Book")
        print("3. Add a Book")
        print("4. Return a Book")
        user_choice = input()
        if user_choice not in ['1','2','3','4']
        print("Please enter a valid option")
        continue
    
    else:
        user_choice = int(user_choice)
        
        
    
    if user_choice == 1:
        books.displayBooks()
        
    elif user_choice == 2:
        book = input("Enter the name of the book you want to lend: ")
        user = input("Enter your name: ")
        books.lendBook(user, book)
        
    elif user_choice == 3:
        
        
        
       
        
            