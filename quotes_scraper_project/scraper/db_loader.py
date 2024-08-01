
import json
from pymongo import MongoClient

# Подключение к MongoDB (пример)
client = MongoClient('mongodb://localhost:27017/')
db = client['quotes_db']

# Загрузка данных из JSON файлов
with open('data/quotes.json', 'r', encoding='utf-8') as f:
    quotes = json.load(f)
    db.quotes.insert_many(quotes)

with open('data/authors.json', 'r', encoding='utf-8') as f:
    authors = json.load(f)
    db.authors.insert_many(authors)

print("Data loaded into the database successfully!")
