import SortingService

ascending = False
descending = True

title = 'title'
author = 'author'
year = 'year'


class Book:
    def __init__(self, index, title, author, year):
        self.index = index
        self.title = title
        self.author = author
        self.year = year

books = [
    Book(1, 'Java How to Program', 'Deitel & Deitel', 2007),
    Book(2, 'Patterns of Enterprise Application Architecture', 'Martin Fwoler', 2002),
    Book(3, 'Head First Design Patterns', 'Elisabeth Freeman', 2004),
    Book(4, 'Internet & WWW: How to Program', 'Deitel & Deitel', 2007),
]

books_empty = []

books_null = None


def print_sorted_books(sorted_books):
    for book in sorted_books:
        print book.index
        print book.title
        print book.author
        print book.year
        print('')


def scenario1():
    sorted_books = SortingService.sort(books, title, ascending)
    print_sorted_books(sorted_books)


def scenario2():
    sorted_books = SortingService.sort(books, title, descending)
    sorted_books = SortingService.sort(sorted_books, author, ascending)
    print_sorted_books(sorted_books)


def scenario3():
    sorted_books = SortingService.sort(books, title, ascending)
    sorted_books = SortingService.sort(sorted_books, author, descending)
    sorted_books = SortingService.sort(sorted_books, year, descending)
    print_sorted_books(sorted_books)


def scenario4():
    sorted_books = SortingService.sort(books_null, title, ascending)
    print_sorted_books(sorted_books)


def scenario5():
    sorted_books = SortingService.sort(books_empty, title, ascending)
    print_sorted_books(sorted_books)


scenario1()
print('--------------------')
scenario2()
print('--------------------')
scenario3()
print('--------------------')
scenario4()
print('--------------------')
scenario5()