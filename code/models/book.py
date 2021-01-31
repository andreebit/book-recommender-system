import csv

BOOKS_CSV_FILE = 'data/books.csv'

def get_all():
    books = []
    with open(BOOKS_CSV_FILE, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            books.append({'id': int(row['id']), 'title': row['title'], 'image_link': row['image_link'], 'genre': row['genre'], 'author': row['author']})

    return books


def get_by_id(book_id):
    book = {}
    with open(BOOKS_CSV_FILE, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            if (int(book_id) == int(row['id'])):
                book = {
                    'id': int(row['id']),
                    'title': row['title'],
                    'image_link': row['image_link'],
                    'genre': row['genre'],
                    'author': row['author'],
                    'description': row['Desc']
                }
    
    return book