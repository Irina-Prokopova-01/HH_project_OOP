import pytest

from src.vacancies import Vacancy


@pytest.fixture
def vacancy_list():
    return [
        Vacancy(
            title="Инженер",
            link="artemtim.ru",
            area="Москва",
            salary=90000,
            description="Работа с технической документацией",
            requirement="Опрыт работы от 3 лет. Высшее образование.",
        ),
        Vacancy(
            title="Инженер",
            link="artemtim.ru",
            area="Москва",
            salary=50000,
            description="Работа с технической документацией",
            requirement="Опрыт работы от 3 лет. Высшее образование.",
        ),
    ]


@pytest.fixture
def vacancy_list_for_filter():
    return [
        Vacancy(
            title="Инженер 1кат",
            link="artemtim.ru",
            salary=90000,
            area="Москва",
            description="Работа с технической документацией",
            requirement="Опрыт работы от 3 лет. Высшее образование.",
        ),
        Vacancy(
            title="Продавец",
            link="artemtim.ru",
            area="Химки",
            salary=50000,
            description="Продажа томатов",
            requirement="Опрыт работы от 2 лет.",
        ),
    ]


@pytest.fixture
def vacancy_list_sorted():
    return [
        Vacancy(
            title="Продавец",
            link="artemtim.ru",
            area="Химки",
            salary=50000,
            description="Продажа томатов",
            requirement="Опрыт работы от 2 лет.",
        ),
        Vacancy(
            title="Инженер 1кат",
            link="artemtim.ru",
            salary=90000,
            area="Москва",
            description="Работа с технической документацией",
            requirement="Опрыт работы от 3 лет. Высшее образование.",
        ),
    ]


@pytest.fixture
def vacancy_1():
    return Vacancy(
        title="Инженер",
        link="artemtim.ru",
        area="Москва",
        salary=50000,
        description="Работа с технической документацией",
        requirement="Опрыт работы от 3 лет. Высшее образование.",
    )


@pytest.fixture
def vacancy_2():
    return Vacancy(
        title="Инженер 1кат",
        link="artemtim.ru",
        area="Москва",
        salary=90000,
        description="Работа с технической документацией",
        requirement="Опрыт работы от 3 лет. Высшее образование.",
    )


@pytest.fixture
def file_name():
    return "test_file_name.json"