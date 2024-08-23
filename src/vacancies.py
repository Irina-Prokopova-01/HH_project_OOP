from functools import total_ordering


@total_ordering
class Vacancy:
    """Класс, описывающий вакансию и её основные характеристики"""

    title: str
    link: str
    salary: int | float
    area: str
    description: str
    requirement: str

    def __init__(self, title, link, description, requirement, area, salary=0):
        self.title = title
        self.link = link
        self.salary = salary
        self.area = area
        self.description = description
        self.requirement = requirement

    def __str__(self):
        title = f"Вакансия - {self.title}"
        salary = f"зарплата - {self.salary}"
        area = f"местоположение - {self.area}"
        link = f"ссылка на вакансию - {self.link}"
        return f"{title}, {salary}, {area}, {link}."

    def vac_full(self):
        title = f"Вакансия - {self.title}"
        salary = f"зарплата - {self.salary}"
        area = f"местоположение - {self.area}"
        description = f"описание - {self.description}"
        requirement = f"требования - {self.requirement}"
        link = f"ссылка - {self.link}"
        return f"{title}, {salary}, {area}, {description}, {requirement}, {link}"

    def __eq__(self, other):
        if isinstance(other, Vacancy):
            return self.salary == other.salary
        else:
            return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Vacancy):
            return self.salary < other.salary
        else:
            return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Vacancy):
            return self.salary >= other.salary
        else:
            return NotImplemented
