import os
from abc import ABC, abstractmethod

import requests

from config import DATA_DIR
from src.vacancies import Vacancy


class Parser(ABC):
    """Абстрактный класс по работе с API сервисами."""

    @abstractmethod
    def load_vacancies(self):
        pass

    @abstractmethod
    def export_vac_list(self):
        pass


class HH(Parser):
    """Класс для работы с API сервиса HeadHunter.
    Получает список вакансий по ключевому слову.
    Полученный список приводит к необходимому виду.
    Класс является дочерним классом класса Parser."""

    def __init__(self, filename="../data/vacancies.json"):
        self.url = "https://api.hh.ru/vacancies"
        self.headers = {"User-Agent": "HH-User-Agent"}
        self.params = {"text": "", "page": 0, "per_page": 100}
        self.vacancies = []
        self.vacancies_short = []
        self.fullname = os.path.join(DATA_DIR, filename)
        # print(self.vacancies)

    def load_vacancies(self, keyword):
        """Метод загружает вакансии с сервиса HH. Формирует из загруженных данных список объектов
        вакансий с полями: название, ссылка, зарплата, описание, требования, место."""
        self.params["text"] = keyword
        while self.params.get("page") != 2:
            response = requests.get(self.url, headers=self.headers, params=self.params)
            vacancies = response.json()["items"]
            self.vacancies.extend(vacancies)
            self.params["page"] += 1
            # print(vacancies)
        for vacancie in self.vacancies:
            if vacancie["name"]:
                title = vacancie["name"]
            else:
                title = "Не указано."
            if vacancie["alternate_url"]:
                link = vacancie["alternate_url"]
            else:
                link = "Не указано."
            if vacancie["snippet"]["responsibility"]:
                description = vacancie["snippet"]["responsibility"]
            else:
                description = "Не указано."
            if vacancie["snippet"]["requirement"]:
                requirement = vacancie["snippet"]["requirement"]
            else:
                requirement = "Не указано."
            if vacancie["salary"]:
                if vacancie["salary"]["from"]:
                    salary = vacancie["salary"]["from"]
                elif vacancie["salary"]["to"]:
                    salary = vacancie["salary"]["to"]
                else:
                    salary = 0
            else:
                salary = 0
            if vacancie["area"]["name"]:
                area = vacancie["area"]["name"]
            else:
                area = "Не указано."
            self.vacancies_short.append(
                Vacancy(
                    title=title,
                    link=link,
                    description=description,
                    requirement=requirement,
                    salary=salary,
                    area=area,
                )
            )

    def export_vac_list(self):
        """Метод возвращает обработанный список вакансий."""
        return self.vacancies_short
