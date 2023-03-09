import json

with open('D:\Media/books.json', 'r') as f:
    books = json.load(f)

result = []
for book in books:
    if book['pageCount'] > 500:
        result.append(book)

for book in result:
    print(book)