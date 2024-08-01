
# Пример моделей данных для использования с базой данных

class Quote:
    def __init__(self, text, author, tags):
        self.text = text
        self.author = author
        self.tags = tags

class Author:
    def __init__(self, fullname, born_date, born_location, description):
        self.fullname = fullname
        self.born_date = born_date
        self.born_location = born_location
        self.description = description
