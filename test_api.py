import requests
import allure
from config import base_url, HEADERS


API_URL = f"{base_url}/api/v1/recommend/semantic"


def perform_search(phrase, test_title, step_description):
    """Общая функция для выполнения поиска через API и проверки результата.

    Args:
        phrase: Текст запроса для поиска (например, название книги или автора)
        test_title: Заголовок теста для отчёта Allure
        step_description: Описание шага для отчёта Allure
    """
    with allure.feature("Поиск книг"):
        with allure.title(test_title):
            with allure.step(step_description):
                res = requests.get(
                    f"{API_URL}?phrase={phrase}&perPage=48",
                    headers=HEADERS
                )
            with allure.step("Проверить, что статус-код ответа равен 200"):
                assert res.status_code == 200, (
                    f"Ожидался статус-код 200, но получен {res.status_code}"
                )


# Тестовые случаи
TEST_CASES = [
    ("Ребенок Розмари", "Поиск по названию книги", "Выполнить поиск по названию книги 'Ребенок Розмари'"),
    ("Айра Левин", "Поиск по автору книги", "Выполнить поиск по автору 'Айра Левин'"),
    ("Ребенок", "Поиск по части названия книги", "Выполнить поиск по части названия 'Ребенок'"),
    ("1984", "Поиск по названию книги из чисел", "Выполнить поиск по названию '1984'"),
    ("s.n.u.f.f.", "Поиск по названию книги с точками", "Выполнить поиск по названию 's.n.u.f.f.'")
]

if __name__ == "__main__":
    for phrase, title, description in TEST_CASES:
        perform_search(phrase, title, description)
