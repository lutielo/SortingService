from SortingServiceException import SortingServiceException
from operator import attrgetter


def sort(books, attribute, direction):
    try:
        return sorted(books, key=attrgetter(attribute), reverse=direction)
    except TypeError:
        raise SortingServiceException("A set of books is needed")