import pytest

from src.vacancies import Vacancy


def test_vacancies_init(vacancy_1, vacancy_2):
    """Тестирование инициализации."""
    assert vacancy_1.title == "Инженер"
    assert vacancy_1.description == "Работа с технической документацией"
    assert vacancy_1.link == "artemtim.ru"
    assert vacancy_1.area == "Москва"
    assert vacancy_1.salary == 50000
    assert vacancy_2.salary == 90000
    assert vacancy_2.title == "Инженер 1кат"
    assert vacancy_2.area == "Москва"
    assert vacancy_2.description == "Работа с технической документацией"
    assert vacancy_2.link == "artemtim.ru"
    assert (
        str(vacancy_1)
        == "Вакансия - Инженер, зарплата - 50000, местоположение - Москва, ссылка на вакансию - artemtim.ru."
    )


def test_ordering(vacancy_1, vacancy_2, vacancy_3):
    assert vacancy_1 < vacancy_2
    assert vacancy_2 >= vacancy_1
    assert vacancy_2 == vacancy_3

def test_lt_(vacancy_1, vacancy_2, vacancy_3):
    assert Vacancy.__lt__(vacancy_1, vacancy_2) is True
    assert Vacancy.__lt__(vacancy_2, vacancy_3) is False