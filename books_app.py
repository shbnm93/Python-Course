# V 1.0.0

def add_book():
    book = {}
    global books
    book["title"] = input("Enter title of the book : ")
    book["author"] = input("Enter author of book : ")
    book["pages"] = int(input("Enter number of pages : "))
    book["price"] = float(input("Enter price of book : "))
    book["isbn"] = input("Enter ISBN of the book : ")
    books.append(book)

def list_books():
    for book in books:
        print("Title: ", book["title"])
        print("Author: ", book["author"])
        print("Pages: ", book["pages"])
        print("Price: ", book["price"])
        print("ISBN: ", book["isbn"])
        print("-----------------")


def find_book():
    pass

def delete_book():
    pass

# ----------------------main-------------------------
books = []
while True :
    print(40*"=")
    print("Press A to add a book")
    print("Press L to list all books")
    print("Press F to find a book")
    print("Press D to delete a book")
    print("Press Q to quit application")
    print(40*"=")
    choice = input("Enter your choice : ").upper()


    if choice == 'A' : 
        add_book()
    elif choice == 'L':
        list_books()
    elif choice == 'F':
        find_book()
    elif choice == 'D':
        delete_book()
    elif choice == 'Q':
        break
    else:
        print("Wrong choice !")