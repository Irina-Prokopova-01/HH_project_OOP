import re

from src.API_HH import HH
from src.vacancies_file import VacancyFile


class VacancyFilter:
    """Класс фильтрует список объектов вакансий по заданным признакам, сортирует по зарплате
    (по-умолчанию по возростанию).
    Возвращает отфильтрованный и отсортированный список."""

    def __init__(self):
        self.__vacs = []

    @property
    def vacs(self):
        return self.__vacs

    @vacs.setter
    def vacs(self, vacs):
        if isinstance(vacs, list):
            # self.__vacs = []
            self.__vacs = vacs
            # print(vacs)
        else:
            raise ValueError("Некорректные данные")

    def filter_salary(self, salary):
        """Метод проводит фильтрование списка объектов вакансий по зарплате(более заданного значения)."""
        temp = filter(lambda x: x.salary >= salary, self.__vacs)
        self.__vacs = list(temp)

    def filter_title(self, word):
        """Метод проводит фильтрование списка объектов вакансий по названию вакансии (совпадению заданного слова)."""
        pattern = rf"{word}"
        temp = filter(
            lambda x: re.findall(pattern, x.title, re.IGNORECASE), self.__vacs
        )
        self.__vacs = list(temp)

    def filter_description(self, word):
        """Метод проводит фильтрование списка объектов вакансий по описанию вакансии (совпадению заданного слова)."""
        pattern = rf"{word}"
        temp = filter(
            lambda x: re.findall(pattern, x.description, re.IGNORECASE), self.__vacs
        )
        self.__vacs = list(temp)

    def filter_requirement(self, word):
        """Метод проводит фильтрование списка объектов вакансий
        по требованию к вакансии (совпадению заданного слова)."""
        pattern = rf"{word}"
        temp = filter(
            lambda x: re.findall(pattern, x.requirement, re.IGNORECASE), self.__vacs
        )
        self.__vacs = list(temp)

    def filter_area(self, word):
        """Метод проводит фильтрование списка объектов вакансий по местоположению (совпадению заданного слова)."""
        pattern = rf"{word}"
        temp = filter(lambda x: re.findall(pattern, x.area, re.IGNORECASE), self.__vacs)
        self.__vacs = list(temp)

    def sort_by_salary(self, direction=False):
        """Метод сортирует список объектов вакансий по зарплате (по-умолчанию по возрастанию)"""
        self.__vacs.sort(key=lambda x: x.salary, reverse=direction)


if __name__ == "__main__":
    # vac_1 = Vacancy("Менеджер", "url", "Продажа оборудования", "Без опыта работы.", "Москва", None)
    # vac_2 = Vacancy("Менеджер", "url", "Разработчик Python", "Без опыта работы.", "Москва", 30000)
    # v_filter = VacancyFilter()
    # data = [vac_1, vac_2]
    # v_filter.vacs = data
    # print(*v_filter.vacs)
    # # print(data)
    # v_filter.filter_requirement('Менеджер')
    # print(v_filter.vacs)
    # v_filter.filter_description('Продажа')
    # # print(v_filter.vacs)
    # # v_filter.filter_area('Москва')
    # # v_filter.filter_salary('30000')

    hh = HH()
    # a = hh.export_vac_list()
    # hh.load_vacancies('менеджер')
    file_v = VacancyFile()
    file_v.import_vacancy_list(hh.vacancies)
