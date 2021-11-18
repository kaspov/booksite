import json
import random

with open("bookList.json") as f:
    books = json.load(f)

authors = { } 

for book in books:

    author = book['author'] 
    age_key = 'age'
    age_value = random.randint(20,80)
    book_key = 'book'
    book_value = book['title']

    if author not in authors:
        authors[author]  = { age_key : age_value,
                             book_key : [book_value]  
                            } 
    else: 
        authorsBookList = authors[author][book_key] 
        authorsBookList.append(book_value)


#this outputs a json file
with open('authors.json', "w") as outfile:
    json.dump(authors, outfile)

# now i want to create a list and each author will have his id

authorList = [ ] 

for author,author_val in authors.items():
    age, books = author_val.values()
    authorList.append([author,age, books])

