from src.vacancies_list import VacanсyList


def test_vacancy_list_init():
    """Тестирование инициализации"""
    test = VacanсyList()
    assert len(test.vacs_list) == 0


def test_vacancy_list_adding_vac(vacancy_1):
    """Тестирование добавления объекта вакансий в список."""
    test = VacanсyList()
    test.add_vacancy(vacancy_1)
    assert test.show_vacancy_by_index(0) == vacancy_1.vac_full()


def test_vacancy_list_adding_list_obj(vacancy_list):
    """Тестирование добавления списка объектов вакансий в список."""
    test = VacanсyList()
    test.add_vacancy(vacancy_list)
    assert test.show_str_vacs() == (
        "Номер - 1 Вакансия - Инженер, зарплата - 90000, местоположение - Москва, ссылка на вакансию - artemtim.ru.\n"
        "Номер - 2 Вакансия - Инженер, зарплата - 50000, местоположение - Москва, ссылка на вакансию - artemtim.ru.\n"
    )


def test_vacancy_list_export_import(vacancy_list):
    """Тестирование импорта и экспорта списка вакансий."""
    test = VacanсyList()
    test.import_vacancy_list(vacancy_list)
    assert test.export_vacanсy_list() == vacancy_list
    assert test.show_str_vacs() == (
        "Номер - 1 Вакансия - Инженер, зарплата - 90000, местоположение - Москва, ссылка на вакансию - artemtim.ru.\n"
        "Номер - 2 Вакансия - Инженер, зарплата - 50000, местоположение - Москва, ссылка на вакансию - artemtim.ru.\n"
    )
