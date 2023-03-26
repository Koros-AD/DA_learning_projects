#The program reads json file and outputs books with over 500 pages
import json
#opening file
with open('D:\Media/books.json', 'r') as f:
    books = json.load(f)
    
#creating a list "result" for books that fit the criteria
# setting the condition: if pageCount is over 500 add a book to the list
result = []
for book in books:
    if book['pageCount'] > 500:
        result.append(book)
#output
for book in result:
    print(book)
