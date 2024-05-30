from os import system 
clear = lambda : system("cls")

from json import load
with open("books_database.json", "r") as database:
    books = load(database)

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
    from pickle import dump
    with open("books_database.info", "wb") as database:
        dump(books, database)
        input("\nBooks database has been saved successfully! ")

def save_json():
    from json import dump
    with open("books_database.json", "w") as database:
        dump(books, database, indent=4) 
        input("\nBooks database has been saved successfully! ")