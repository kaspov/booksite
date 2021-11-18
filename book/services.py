from book.models import Author, Publisher, Book, Store
from book.clean_data import ( Books, AuthorModel ) 

from book.constants import PUBLISHERS

## book-> publisher ( FK ) 
## book -> author ( MM ) 
## book -> store ( MM ) 


def createAuthors():
    for author in AuthorModel: 
        Author.objects.create(**author)

def createPublishers():
    for publisher in PUBLISHERS:
        Publisher.objects.create(name=publisher)

def createBooks():
    for book in Books: 
        try: 
            Book.objects.create(**book)
        except Exception:
            print('error !! error !! ' )





        
        





def createStores():
    pass

