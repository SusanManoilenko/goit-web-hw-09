# Импорт необходимых модулей и функций
from scraper import quotes_scraper, db_loader, models

def main():
    # Вызов функций из импортированных модулей
    quotes_scraper.scrape_quotes()
    db_loader.load_data()
    models.setup_models()

if __name__ == "__main__":
    main()
