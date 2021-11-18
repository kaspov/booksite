from book.models import Author, Publisher, Book, Store
import random

import json

def loadBooks():
    with open('book/bookList.json') as f: 
        return json.load(f)

def getpubdate():
    publication_date = [
            f"{random.randint(1950,2021)}-{random.randint(1,12)}-{random.randint(1,31)}"
            for _ in range(100) ] 

def getrating():
    ratings = [ random.uniform(0,5) for _ in range(100) ] 


