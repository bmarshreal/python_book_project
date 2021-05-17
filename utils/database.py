""""
Concerned with storing and retrieving books from a list
"""

books = []


def add_book(name, author):
    books.append({'name':name, 'author':author, 'read':False})


def get_all_books():
    return books


def mark_book_as_read(name):
    for book in books:
        if book['name'] == name:
            book['read'] = True


# def delete_book(name): #BAD PRACTICE to change a list while iterating over it!
#     for book in books:
#         if book['name'] == name:
#             books.remove(book)

def delete_book(name):
    global books
    # We need to state that the variable books is global
    books = [book for book in books if book['name'] != name]
    # Add each book to new list if ['name'] != name
