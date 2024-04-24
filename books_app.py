# V 2.2.0

import books_operations as op


while True :
    op.clear()
    print(40*"=")
    print("Press A to add a book")
    print("Press L to list all books")
    print("Press F to find a book")
    print("Press D to delete a book")
    print("Press Q to quit application")
    print(40*"=")
    choice = input("Enter your choice : ").upper()


    if choice == 'A' : 
        op.add_book()
    elif choice == 'L':
        op.list_books()
    elif choice == 'F':
        op.find_book()
    elif choice == 'D':
        op.delete_book()
    elif choice == 'Q':
        break
    else:
        input("\n\nWrong Choice !")