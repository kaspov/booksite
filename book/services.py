from book.models import Author, Publisher, Book, Store
from book.clean_data import (AUTHORS , ) 

from book.constants import PUBLISHERS

def createAuthors():
    for author in AUTHORS: 
        Author.objects.create(**author)

def createPublishers():
    for publisher in PUBLISHERS:
        Publisher.objects.create(name=publisher)

# def createBooks():
#     for book in Books: 
#         Book.objects.create(**book)


