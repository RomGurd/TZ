
from Lib.assertions import Asseretions

from Lib.base_case import BaseCase
from datetime import datetime
from Lib.my_requests import MyRequests
import allure

from tests.test_getting_a_list_of_books import TestReceivingListBooks


@allure.epic("Проверка удаления книги")
class TestDeletingBookById(BaseCase):
    @allure.description("Проверка на создания и удаления книги")
    def test_deleting_book(self):
        random_part = datetime.now().strftime("%m%d%Y%H%M%S")
        values = {
            "author": "Артур Конан Дойль",
            "id": random_part,
            "isElectronicBook": True,
            "name": "Приключения Шерлока Холмса",
            "year": 1927
        }
        response = MyRequests.post("api/books", json=values)
        Asseretions.assert_code_status(response, 201)
        TestReceivingListBooks().test_get_list_books()  # Здесь проходят проверки того как в каком ввиде книги внеслись в базу
        id_from_make_book = response.json()["book"]["id"]
        response2 = MyRequests.delete(f"api/books/{id_from_make_book}")
        Asseretions.assert_code_status(response2, 200)
        response3 = MyRequests.get(f"api/books/{id_from_make_book}")
        Asseretions.assert_code_status(response3, 404)




