from os import system 
clear = lambda : system("cls")

books = []

def add_book():
    clear()
    book = {}
    global books
    book["title"] = input("Enter title of the book : ")
    book["author"] = input("Enter author of book : ")
    book["pages"] = int(input("Enter number of pages : "))
    book["price"] = float(input("Enter price of book : "))
    book["isbn"] = input("Enter ISBN of the book : ")
    books.append(book)
    input("\nThe book successfully added to database. ")

def list_books():
    clear()
    for book in books:
        print("Title: ", book["title"])
        print("Author: ", book["author"])
        print("Pages: ", book["pages"])
        print("Price: ", book["price"])
        print("ISBN: ", book["isbn"])
        print("-----------------")
    input("\nPress enter to back manu ...")


def find_book():
    clear()
    isbn = input("Enter ISBN to search book : ")
    for book in books:
        if book["isbn"] == isbn:
            print("Title: ", book["title"])
            print("Author: ", book["author"])
            print("Pages: ", book["pages"])
            print("Price: ", book["price"])
            print("ISBN: ", book["isbn"])
            input("------------------------------")
            break
    else:
        input("\n\nThis book does not exist in books database! Press enter to continue")

def delete_book():
    clear()
    isbn = input("Enter ISBN to delete book: ")
    for book in books:
        if book["isbn"] == isbn:
            books.remove(book)
            input("\n\nThe book has been deleted successfully!")
            break
    else:
        input("\n\nThis book does not exist in books database! Press enter to continue")


def save_books():
    with open("books_database.txt", "w") as database:
        database.writelines(books)
        input("Books database has been saved successfully! ")