# web_scraping_14_04_2022

### Базовое
Сохранить зависимости:
- `pip freeze > requirements.txt`

Установить зависимости из файла:
- `pip install -r requirements.txt`

Библиотека dotenv - [python-dotenv](https://pypi.org/project/python-dotenv/)

### Работа со Scrapy
- [Pipeline для работы с MongoDB](https://docs.scrapy.org/en/latest/topics/item-pipeline.html#write-items-to-mongodb)

### Необязательное
- [pre-commit и git hooks](https://pre-commit.com/)
- [black; документацию можно найти далее](https://pypi.org/project/black/)
- [isort; аналогично](https://pypi.org/project/isort/)
- [flake8; аналогично](https://pypi.org/project/flake8/)


#### (Optional; Актуально для `lesson_2`) Запуск локального сервера
Чтобы запустить локальный сервер из папки `local_server` необходимо выполнить следующие шаги:
1. `pip install flask`
2. перейти в командной строке в папку `local_server`; например, cd `local_server/`
3. `flask run`
