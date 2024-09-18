# import json
# from unittest.mock import Mock, mock_open, patch
#
# # import pandas as pd
# import pytest

from src.vacancies_file import VacancyFile


def test_vacancy_file_init(file_name):
    """Тестирование инициализации."""
    assert VacancyFile(file_name).filename == "test_file_name.json"


def test_vacancy_file_import_export(vacancy_list_for_filter):
    """Тестирование импорта и экспорта списка вакансий."""
    test = VacancyFile()
    test.import_vacancy_list(vacancy_list_for_filter)
    assert test.export_vacancy_list() == vacancy_list_for_filter


#
# @patch("test_vacancies_file")
# def test_read_file_json(path):
#     path.return_value = pd.DataFrame()
#     assert read_file("foo") == []
#
#
# def test_read_file_uncorrect_path():
#     test = VacancyFile("../data/vacancies.json")
#     test.read_file()
#     assert test.write_file() == "../data/vacancies.json"
#
