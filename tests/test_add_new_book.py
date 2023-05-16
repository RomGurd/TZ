import json
import pytest
import allure

from Lib.assertions import Asseretions

from Lib.base_case import BaseCase
from Lib.my_requests import MyRequests
from tests.test_getting_a_list_of_books import TestReceivingListBooks


@allure.epic("Проверка на внесения в API новой книги")
class TestAddNewBook(BaseCase):

    with open(r"C:\Work\TZ\tests\Json_for_add_new_book.txt", 'r', encoding='utf-8') as f:
        data = f.read()
        value = json.loads(data)

    @allure.description("Проверка на внесения в API новой книги")
    @pytest.mark.parametrize("values", value)
    def test_add_new_book(self, values):
        url = "api/books"
        response = MyRequests.post(url, json=values)
        Asseretions.assert_code_status(response, 201)
        TestReceivingListBooks().test_get_list_books()  # Здесь проходят проверки того как в каком ввиде кнги внеслись в базу
        print(response.json()["book"])

        id_list = [] # Здесь происходит удаления всех добавленниыйх книг по id
        id_list.append(response.json()["book"]["id"])
        for id in id_list:
            MyRequests.delete(f"api/books/{id}")
            response2 = MyRequests.get(f"api/books/{id}")
            assert response2.status_code == 404, "Удаления по id не состоялось"

    with open(r"C:\Work\TZ\tests\Json_for_add_new_book_stress.txt", 'r', encoding='utf-8') as f:
        data = f.read()
        value2 = json.loads(data)

    @allure.description("Стресс тест на внесение большого кол-во книг одним разом")
    @pytest.mark.parametrize("value", value2)
    def test_add_new_book_stress(self, value):
        response = MyRequests.post("api/books", json=value)
        Asseretions.assert_code_status(response, 201)

        id_list = []
        id_list.append(response.json()["book"]["id"])
        for id in id_list:
            MyRequests.delete(f"api/books/{id}")
            response2 = MyRequests.get(f"api/books/{id}")
            assert response2.status_code == 404, "Удаления по id не состоялось"

    with open(r"C:\Work\TZ\tests\Json_for_add_new_book_invalid.txt", 'r', encoding='utf-8') as f:
        data = f.read()
        value3 = json.loads(data)

    @allure.description("Проверка на внесение данных без поля 'name'")
    @pytest.mark.parametrize("value", value3)
    def test_add_new_book_invalid(self, value):
        response = MyRequests.post("api/books", json=value)
        Asseretions.assert_code_status(response, 400)







