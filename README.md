# Дипломная работа по автоматизации UI и API тестов для сайта "Читай-город"

## Оглавление
- [Описание](#описание)
- [Шаги для запуска](#шаги-для-запуска)
- [Получение токена](#получение-токена)
- [Стек технологий](#стек-технологий)
- [Структура проекта](#структура-проекта)
- [Полезные ссылки](#полезные-ссылки)
- [Установка библиотек](#установка-библиотек)


### Шаги
1. **Склонировать проект:** 
    Выполните команду в терминале: `git clone https://github.com/dablbolt/final_task.git`

2. **Перейти в директорию проекта:**
        `cd final_task`

3. **Создать и активировать виртуальное окружение** (рекомендуется для управления зависимостями):  
    - Для Windows:
   `python -m venv venv`
   `venv\Scripts\activate`

4. **Установить зависимости:**  
   Выполните команду:
   `pip install -r requirements.txt`

5. **Получение токена**  
   - Чтобы получить токен, вам необходимо зайти на сайт Читай-город (https://www.chitai-gorod.ru/), 
   через DevTools во вкладке Application в разделе Cookies перейти в https://www.chitai-gorod.ru/
   и найти access-token и это значение применить в token в test_api.py
   - Токен должен быть добавлен в ваш проект, чтобы тесты могли успешно проходить.

6. **Запустить тесты:** 
    - Запустить тесты можно командой `pytest` 
    - Запустить тесты с формированием отчета запускается командой `pytest -v --alluredir=allure-results`
    - Просмотр отчета запускается командой `allure serve allure-results`


## Стек технологий
- **pytest** - основная библиотека для написания и выполнения тестов.
- **selenium** - библиотека для автоматизации UI тестирования.
- **requests** - библиотека для работы с HTTP-клиентом, используемая для API тестирования.
- **allure** - библиотека для генерации отчетов о выполнении тестов.


## Полезные ссылки
- [Документация pytest](https://docs.pytest.org/en/stable/)
- [Документация Selenium](https://www.selenium.dev/documentation/webdriver/)
- [Документация Allure](https://docs.qameta.io/allure/)

## Установка библиотек
Для установки необходимых библиотек, выполните следующие команды в терминале:
- pip install pytest
- pip install selenium
- pip install webdriver-manager
- pip install requests
- pip install allure-pytest

## Описание  включенных тестов 
### API tests
 - Поиск по полному названию книги
 - Поиск по автору книги
 - Поиск по частим названия книги
 - Поиск по названию с цифрами
 - Поиск по названию с точками
### UI tests
 - Поиск по полному названию книги
 - Поиск по автору книги
 - Поиск по частим названия книги
 - Поиск по названию с цифрами
 - Поиск по названию с точками