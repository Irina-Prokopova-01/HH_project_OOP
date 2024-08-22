from unittest.mock import ANY, MagicMock, patch

import pytest
from requests.exceptions import HTTPError

from src.API_HH import HH


@patch("requests.get")
def test_successfully_load_vacancies(mocked_requests_get):
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"title": "title"}
    mocked_requests_get.return_value = mock_response
    #
    # res = HH.load_vacancies(mock_response, 'менеджер')
    #
    # assert res == []
    # mocked_requests_get.assert_called_once_with(
    #     ANY, headers={}, params={}
    # )


@patch("requests.get")
def test_API_HH_error(mocked_requests_get):
    mock_response = MagicMock()
    mock_response.raise_for_status.side_effect = HTTPError("Not authenticated")
    mocked_requests_get.return_value = mock_response

    with pytest.raises(HTTPError):
        vac_1 = HH()
        vac_1.export_vac_list()


def test_add_salary_none(vacancy_1, vacancy_list_for_filter):
    with pytest.raises(TypeError):
        vacancy_1.salary(vacancy_list_for_filter)


def test_add_title_none(vacancy_1, vacancy_list_for_filter):
    with pytest.raises(TypeError):
        vacancy_1.title(vacancy_list_for_filter)


def test_add_description_none(vacancy_1, vacancy_list_for_filter):
    with pytest.raises(TypeError):
        vacancy_1.description(vacancy_list_for_filter)


def test_add_link_none(vacancy_1, vacancy_list_for_filter):
    with pytest.raises(TypeError):
        vacancy_1.link(vacancy_list_for_filter)


def test_add_area_none(vacancy_1, vacancy_list_for_filter):
    with pytest.raises(TypeError):
        vacancy_1.area(vacancy_list_for_filter)
