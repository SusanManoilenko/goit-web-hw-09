
import requests
from bs4 import BeautifulSoup
import json
import time

# Базовый URL сайта
base_url = 'http://quotes.toscrape.com/'


# Функция для получения данных с отдельной страницы
def scrape_page(page_url):
    response = requests.get(page_url)
    soup = BeautifulSoup(response.text, 'lxml')

    quotes = soup.find_all('div', class_='quote')
    authors = set()

    for quote in quotes:
        text = quote.find('span', class_='text').text.strip('“”')
        author = quote.find('small', class_='author').text
        author_url = quote.find('a')['href']
        tags = [tag.text for tag in quote.find_all('a', class_='tag')]

        quote_data.append({
            'tags': tags,
            'author': author,
            'quote': text
        })

        authors.add((author, base_url + author_url))

    return authors


# Функция для получения данных об авторе
def scrape_author(author_url):
    response = requests.get(author_url)
    soup = BeautifulSoup(response.text, 'lxml')

    name = soup.find('h3', class_='author-title').text.strip()
    birth_date = soup.find('span', class_='author-born-date').text
    birth_location = soup.find('span', class_='author-born-location').text.strip("in ")
    description = soup.find('div', class_='author-description').text.strip()

    return {
        'fullname': name,
        'born_date': birth_date,
        'born_location': f"in {birth_location}",
        'description': description
    }


# Инициализация списков для сохранения цитат и авторов
quote_data = []
author_data = []

# Скрапинг всех страниц
page_num = 1
while True:
    page_url = base_url + 'page/' + str(page_num) + '/'
    print(f"Scraping {page_url}...")
    authors = scrape_page(page_url)

    for author, author_url in authors:
        if not any(a['fullname'] == author for a in author_data):
            author_info = scrape_author(author_url)
            author_data.append(author_info)

    next_button = BeautifulSoup(requests.get(page_url).text, 'lxml').find('li', class_='next')
    if not next_button:
        break

    page_num += 1
    time.sleep(1)

# Сохранение данных в JSON файлы
with open('data/quotes.json', 'w', encoding='utf-8') as f:
    json.dump(quote_data, f, ensure_ascii=False, indent=4)

with open('data/authors.json', 'w', encoding='utf-8') as f:
    json.dump(author_data, f, ensure_ascii=False, indent=4)

print("Scraping completed and data saved!")
