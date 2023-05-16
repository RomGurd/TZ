import json

import pytest

from Lib.assertions import Asseretions

from Lib.base_case import BaseCase
from Lib.my_requests import MyRequests
import allure

from tests.test_getting_a_list_of_books import TestReceivingListBooks


@allure.epic("Проверка исправления книги")
class TestUpdatesBookById(BaseCase):

    with open(r"C:\Work\TZ\tests\value_for_information_updates_by_id.txt", 'r', encoding='utf-8') as f:
        value = eval(f.read())

    @allure.description("Проверка на создание и исправление книги")
    @pytest.mark.parametrize("author, isElectronicBook, name, year", value)
    def test_updates_book(self, author, isElectronicBook, name, year):
        values = {
            "author": author,
            "isElectronicBook": isElectronicBook,
            "name": name,
            "year": year
        }
        values2 = {
            "author": "Франц Кафка",
            "isElectronicBook": False,
            "name": "Письмо отцу",
            "year": 1939
        }
        response = MyRequests.post("api/books", json=values2)
        Asseretions.assert_code_status(response, 201)
        TestReceivingListBooks().test_get_list_books()
        id_from_make_book = response.json()["book"]["id"]
        response2 = MyRequests.put(f"api/books/{id_from_make_book}", json=values)
        Asseretions.assert_json_value_by_name(response2, "author", author, "Автор не претерпел изменений")
        Asseretions.assert_json_value_by_name(response2, "isElectronicBook", isElectronicBook, "Значения книги не претерпел изменений")
        Asseretions.assert_json_value_by_name(response2, "name", name, "Наименования книги не претерпела изменений")
        Asseretions.assert_json_value_by_name(response2, "year", year, "Год не претерпел изменений")
        Asseretions.assert_code_status(response2, 200)
        MyRequests.delete(f"api/books/{id_from_make_book}")
        response2 = MyRequests.get(f"api/books/{id_from_make_book}")
        assert response2.status_code == 404, "Удаления по id не состоялось"

    with open(r"C:\Work\TZ\tests\Json_for_add_new_book_invalid.txt", 'r', encoding='utf-8') as f:
        data = f.read()
        value2 = json.loads(data)

    @allure.description("Проверка на создание и исправление книги c некорректными данными")
    @pytest.mark.parametrize("values", value2)
    def test_updates_book_invalid_value(self, values):
        values2 = {
            "author": "Франц Кафка",
            "isElectronicBook": False,
            "name": "Письмо отцу",
            "year": 1939
        }
        response = MyRequests.post("api/books", json=values2)
        Asseretions.assert_code_status(response, 201)
        TestReceivingListBooks().test_get_list_books()
        id_from_make_book = response.json()["book"]["id"]
        response2 = MyRequests.put(f"api/books/{id_from_make_book}", json=values)
        Asseretions.assert_code_status(response2, 400)
        MyRequests.delete(f"api/books/{id_from_make_book}")
        response2 = MyRequests.get(f"api/books/{id_from_make_book}")
        assert response2.status_code == 404, "Удаления по id не состоялось"
