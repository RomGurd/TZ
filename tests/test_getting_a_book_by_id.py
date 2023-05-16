from Lib.assertions import Asseretions

from Lib.base_case import BaseCase
from Lib.my_requests import MyRequests
import allure
from tests.test_getting_a_list_of_books import TestReceivingListBooks


@allure.epic("Проверка получения книги по id")
class TestGettingBookById(BaseCase):
    @allure.description("Проверка на наличия полей в запросе по id всех книг")
    def test_get_book_id(self):
        all_id = TestReceivingListBooks().test_get_list_books()
        for number in all_id:
            url = f"api/books/{number}"
            response = MyRequests.get(url)
            Asseretions.assert_code_status(response, 200)
            Asseretions.assert_json_has_keys(response, ["id", "author", "isElectronicBook", "name", "year"], "book")

    @allure.description("Проверка соответсвия формата заполненых данных в запросе по id")
    def test_books_by_id_format_data(self):
        all_id = TestReceivingListBooks().test_get_list_books()
        for number in all_id:
            url = f"api/books/{number}"
            response = MyRequests.get(url)
            print(response.json()["book"])
            Asseretions.assert_json_value_is_number(response, "id", "book")
            Asseretions.assert_json_value_is_number(response, "year", "book")
            Asseretions.assert_json_value_is_bool(response, "isElectronicBook", "book")

    @allure.description("Проверка, что значения поля id в ответе соотвествует запрашиваемому id")
    def test_books_match_id_fields(self):
        all_id = TestReceivingListBooks().test_get_list_books()
        for number in all_id:
            url = f"api/books/{number}"
            response = MyRequests.get(url)
            assert number == response.json()["book"]["id"], "Поле id в запросе книги по id, не совпадает с номером " \
                                                            "его вызова"




