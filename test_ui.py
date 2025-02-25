import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import base_url_ui


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def perform_search(driver, query, test_title, step_description):
    """Общая функция для выполнения поиска на сайте и проверки результатов.

    Args:
        driver: Экземпляр WebDriver для управления браузером
        query: Текст запроса для поиска (например, название книги)
        test_title: Заголовок теста для отчёта Allure
        step_description: Описание шага для отчёта Allure
    """
    @allure.feature("Поиск на сайте")
    @allure.title(test_title)
    def _perform_search():
        with allure.step("Открыть главную страницу"):
            driver.get(base_url_ui)

        with allure.step(step_description):
            search_input = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "header-search__input"))
            )
            search_input.send_keys(query)

        with allure.step("Нажать кнопку поиска"):
            search_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "header-search__button"))
            )
            search_button.click()

        with allure.step("Проверить, что отображаются результаты поиска"):
            result_text = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="__layout"]/div/div[3]/div[1]/p'))
            ).text
            assert "Показываем результаты по запросу" in result_text

    _perform_search()


# Тестовые случаи
TEST_CASES = [
    ("Ребенок Розмари", "Поиск по названию книги", "Ввести в поиск название книги 'Ребенок Розмари'"),
    ("Айра Левин", "Поиск по автору книги", "Ввести в поиск автора 'Айра Левин'"),
    ("Ребенок Роз", "Поиск по части названия книги", "Ввести в поиск часть названия 'Ребенок Роз'"),
    ("1984", "Поиск по названию книги из чисел", "Ввести в поиск название '1984'"),
    ("s.n.u.f.f.", "Поиск по названию книги с точками", "Ввести в поиск название 's.n.u.f.f.'")
]


@pytest.mark.parametrize("query, title, description", TEST_CASES)
def test_search(driver, query, title, description):
    perform_search(driver, query, title, description)
