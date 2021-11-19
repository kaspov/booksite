import json
import random
from book.models import Book, Author

authors = { } 
authors_books = [ ] 
books = [ ] 
author_model = [] 

with open("book/bookList.json") as f:
    book_from_json = json.load(f)

for book in book_from_json:

    author = book['author'] 
    age_key, age_value = 'age', random.randint(20,80)
    book_key, book_value = 'book', book['title']
    price = round(random.uniform(250,2500),2)
    rating =  round(random.uniform(0,5),1)

    book_info =  { 
        'name': book['title'], 
        'pages': book['pages'], 
        'price': price, 
        'rating': rating, 
        'pubdate': f"{book['year']}-{random.randint(1,12)}-{random.randint(1,30)}"  
        }

    books.append(book_info)

    if author not in authors:
        authors[author]  = { age_key : age_value,
                             book_key : [book_value]  
                            } 
    else: 
        authors_list_of_books = authors[author][book_key] 
        authors_list_of_books.append(book_value)



for author,author_val in authors.items():
    age, books = author_val.values()
    authors_books.append({
                    'name': author, 
                    'book': books
                    })

    author_model.append({
             'name': author['name'], 
             'age': author['age']
             }) 



