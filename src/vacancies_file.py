import json
import os
from abc import ABC, abstractmethod

from config import DATA_DIR
from src.vacancies import Vacancy
from src.API_HH import HH


class ReadWriteFile(ABC):
    """Абстрактный класс по чтению/записи файла."""

    @abstractmethod
    def read_file(self):
        pass

    @abstractmethod
    def write_file(self):
        pass

    @abstractmethod
    def export_vacancy_list(self):
        pass

    @abstractmethod
    def import_vacancy_list(self):
        pass


class VacancyFile(ReadWriteFile):
    """Класс работает с записью/чтением списка вакансий в файл, принимает/возвращает список вакансий.
    Родительский класс - ReadWriteFile."""

    filename: str

    def __init__(self, filename="../data/vacancies.json"):
        self.filename = filename
        self.fullname = os.path.join(DATA_DIR, filename)
        self.vacs_list = []

    def read_file(self) -> list:
        """Метод читает указанный файл и сохраняет список объектов вакансий из файла."""
        with open(self.fullname, "r", encoding="UTF-8") as file:
            temp_info = json.load(file)
            print('Файл прочитан')
        self.vacs_list = [Vacancy(**item) for item in temp_info]
        return self.vacs_list

    def write_file(self) -> None:
        """Метод записывает обработанный список вакансий в исходный файл, тем самым изменяя список в нём."""
        try:
            temp_vac_list = []
            for item in self.vacs_list:
                temp_vac_list.append(
                    {
                        "title": item.title,
                        "salary": item.salary,
                        "area": item.area,
                        "description": item.description,
                        "requirement": item.requirement,
                        "link": item.link,
                    }
                )
            with open(self.fullname, "w", encoding="utf-8") as file:
                json.dump(temp_vac_list, file, ensure_ascii=False, indent=4)
            print("Файл успешно записан.")
        except Exception as e:
            raise e
            # raise ValueError("При записи файла произошла ошибка!")

    def export_vacancy_list(self):
        """Метод возвращает список объектов вакансий."""
        return self.vacs_list

    def import_vacancy_list(self, new_list):
        """Метод принимает новый список объектов вакансий и заменяет им старый."""
        self.vacs_list = new_list


if __name__ == "__main__":
    hh = HH()
    # a = hh.export_vac_list()
    hh.load_vacancies('менеджер')
    file_v = VacancyFile()
    file_v.import_vacancy_list(hh.vacancies_short)
    # print(file_v.write_file())
    print(*file_v.read_file())

