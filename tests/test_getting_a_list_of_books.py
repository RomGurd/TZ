from Lib.assertions import Asseretions

from Lib.base_case import BaseCase
from Lib.my_requests import MyRequests
import allure


@allure.epic("Проверка получения списка всех книг")
class TestReceivingListBooks(BaseCase):

    list_all_id = []

    @allure.description("Проверка наличия всех полей")
    def test_get_list_books(self):
        url = "api/books"
        response = MyRequests.get(url)
        Asseretions.assert_code_status(response, 200)
        Asseretions.assert_json_has_keys_for_books(response, ["id", "author", "isElectronicBook", "name", "year"], "books")
        self.__class__.list_all_id = [book["id"] for book in response.json()["books"]]

        return self.list_all_id

    @allure.description("Проверка, что список книг не пустой")
    def test_books_list_not_empty(self):
        assert len(self.list_all_id) >= 0, "Список id книг пустой"

    @allure.description("Проверка, что каждая книга имеет уникальный id")
    def test_books_id_unique(self):
        assert len(set(self.list_all_id)) == len(self.list_all_id), "Найдены дубликаты id книг"

    @allure.description("Проверка соответсвия формата заполненых данных")
    def test_books_format_data(self):
        url = "api/books"
        response = MyRequests.get(url)
        Asseretions.assert_json_values_is_number(response, "id", "books")
        Asseretions.assert_json_values_is_number(response, "year", "books")
        Asseretions.assert_json_values_is_bool(response, "isElectronicBook", "books")

