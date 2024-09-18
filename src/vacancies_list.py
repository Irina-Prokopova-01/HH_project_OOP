from src.vacancies import Vacancy


class VacanсyList:
    """Класс работает со списком вакансий - добавляет/удаляет вакансии,
    выводит сокращённое/расширенное отображение вакансий, выводит топ вакансий по зарплате.
    """

    def __init__(self):
        self.vacs_list = []

    def show_vacancy_list(self):
        """Метод выводит расширенную информацию о вакансиях из списка объектов вакансий с номерами."""
        if len(self.vacs_list) == 0:
            return []
        num = 0
        result_info = ""
        for item in self.vacs_list:
            num += 1
            title = f"Вакансия - {item.title}"
            salary = f"зарплата - {item.salary}"
            area = f"местоположение - {item.area}"
            description = f"описание - {item.description}"
            requirement = f"требования - {item.requirement}"
            link = f"ссылка - {item.link}"
            result_info += f"Номер - {num} {title}, {salary}, {area}, {description}, {requirement}, {link}\n"
        return result_info

    def show_str_vacs(self):
        """Метод выводит сокращённую информацию о вакансиях из списка объектов вакансий с номерами."""
        if len(self.vacs_list) == 0:
            return []
        num = 0
        result_info = ""
        for item in self.vacs_list:
            num += 1
            result_info += f"Номер - {num} {str(item)}\n"
        # print(result_info)
        return result_info

    def show_vacancy_by_index(self, index):
        """Метод выводит расширенную информацию о вакансии по заданному индексу."""
        item = self.vacs_list[index - 1]
        title = f"Вакансия - {item.title}"
        salary = f"зарплата - {item.salary}"
        area = f"местоположение - {item.area}"
        description = f"описание - {item.description}"
        requirement = f"требования - {item.requirement}"
        link = f"ссылка - {item.link}"
        return f"{title}, {salary}, {area}, {description}, {requirement}, {link}"

    def add_vacancy(self, vacancy: any) -> None:
        """Метод добавляет объект вакансии в список вакансий,
        принимая данные в виде словаря с описанием вакансии, объекта вакнсии, списка словарей,
        либо списка объектов вакансий."""
        if isinstance(vacancy, dict):
            new_vacancy = Vacancy(**vacancy)
            self.vacs_list.append(new_vacancy)
        elif isinstance(vacancy, Vacancy):
            self.vacs_list.append(vacancy)
        elif isinstance(vacancy, list) or isinstance(vacancy, tuple):
            for item in vacancy:
                if isinstance(item, dict):
                    new_vacancy = Vacancy(**item)
                    self.vacs_list.append(new_vacancy)
                elif isinstance(item, Vacancy):
                    self.vacs_list.append(item)

    def del_vacanсy(self, number: int) -> None:
        """Метод удаляет из списка объект вакансии по номеру (индексу)."""
        self.vacs_list.pop(number - 1)

    def export_vacanсy_list(self):
        """Метод возвращает список объектов вакансий."""
        return self.vacs_list

    def import_vacancy_list(self, new_list):
        """Метод принимает новый список объектов вакансий и заменяет им старый."""
        self.vacs_list = new_list

    def top_vacs(self, n):
        result_info = ""
        if n < len(self.vacs_list):
            for i in range(n):
                result_info += f"Номер - {i + 1} {str(self.vacs_list[i])}\n"
        else:
            for i in range(len(self.vacs_list)):
                result_info += f"Номер - {i + 1} {str(self.vacs_list[i])}\n"
        return result_info
