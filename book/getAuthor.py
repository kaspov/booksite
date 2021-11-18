import json
import random
from book.models import Book, Author

Authors = { } 
AuthorList = [ ] 
Books = [ ] 
AuthorModel = [] 

with open("book/bookList.json") as f:
    books = json.load(f)

for book in books:
    author = book['author'] 
    age_key, age_value = 'age', random.randint(20,80)
    book_key, book_value = 'book', book['title']
    
    newbook =  { 
        'name': book['title'], 
        'author':author, 
        'price': random.uniform(250,2500), 
        'rating': random.uniform(0,5), 
        'pubyear': book['year']
        }

    Books.append(newbook)

    if author not in Authors:
        Authors[author]  = { age_key : age_value,
                             book_key : [book_value]  
                            } 
    else: 
        AuthorsBookList = Authors[author][book_key] 
        AuthorsBookList.append(book_value)



for author,author_val in Authors.items():
    age, books = author_val.values()
    AuthorList.append({
                    'name': author, 
                    'age': age, 
                    'book': books
                    })


for author in AuthorList: 
    AuthorModel.append({
             'name': author['name'], 
             'age': author['age']
             }) 

