from src.vacancies_file import VacancyFile
from src.vacancies_filter import VacancyFilter


def test_init():
    assert VacancyFile().filename == "../data/vacancies.json"


def test_vacanсy_filter_set_get_list(vacancy_list_for_filter):
    """Тестирование получения и возвращения списка вакансий."""
    test = VacancyFilter()
    test.vacs = vacancy_list_for_filter
    assert test.vacs == vacancy_list_for_filter


def test_vacancy_filter_title(vacancy_list_for_filter):
    """Тестирование фильтрации вакансий по названию вакансии."""
    test = VacancyFilter()
    test.vacs = vacancy_list_for_filter
    test.filter_title("Продавец")
    assert test.vacs == [vacancy_list_for_filter[1]]


def test_vacancy_filter_description(vacancy_list_for_filter):
    """Тестирование фильтрации вакансий по описанию."""
    test = VacancyFilter()
    test.vacs = vacancy_list_for_filter
    test.filter_description("Технич")
    assert test.vacs == [vacancy_list_for_filter[0]]


def test_vacancy_filter_requirement(vacancy_list_for_filter):
    """Тестирование фильтрации вакансий по требованию."""
    test = VacancyFilter()
    test.vacs = vacancy_list_for_filter
    test.filter_requirement("высшее")
    assert test.vacs == [vacancy_list_for_filter[0]]


def test_vacancy_filter_salary(vacancy_list_for_filter):
    """Тестирование фильтрации вакансий по зарплате."""
    test = VacancyFilter()
    test.vacs = vacancy_list_for_filter
    test.filter_salary(50000)
    assert test.vacs == vacancy_list_for_filter


def test_vacancy_filter_area(vacancy_list_for_filter):
    """Тестирование фильтрации вакансий по местоположению."""
    test = VacancyFilter()
    test.vacs = vacancy_list_for_filter
    test.filter_area("химки")
    assert test.vacs == [vacancy_list_for_filter[1]]


def test_vacancy_sort_not_reverce(vacancy_list_for_filter, vacancy_list_sorted):
    """Тестирование сортировки вакансий по возрастанию зарплаты."""
    test = VacancyFilter()
    test.vacs = vacancy_list_for_filter
    test.sort_by_salary()
    assert test.vacs == vacancy_list_sorted


def test_vacansy_sort_reverce(vacancy_list_sorted, vacancy_list_for_filter):
    """Тестирование сортировки вакансий по убыванию зарплаты."""
    test = VacancyFilter()
    test.vacs = vacancy_list_sorted
    test.sort_by_salary(True)
    assert test.vacs == vacancy_list_for_filter


# def test_get_top_vacs(vacancy_list_for_filter):
#     test = (top_n=5)
#     assert test.top_vacs(vacancy_list_for_filter) == ()
