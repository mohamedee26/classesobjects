class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    def show_info(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Pages:", self.pages)

book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
book2 = Book("Harry Potter", "J.K. Rowling", 352)
book3 = Book("Harry Botter", "M.K. Rolling", 163)
book1.show_info()
print()
book2.show_info()

