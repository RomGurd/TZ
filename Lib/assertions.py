from requests import Response
import json


class Asseretions:
    @staticmethod
    def assert_json_value_by_name(response: Response, name, expented_value, error_message):
        try:
            response_as_dict = response.json()["book"]
        except json.JSONDecodeError:
            assert False, f"Ответ не в Json формате. Ответ текста '{response.text}'"
        assert name in response_as_dict, f"Ответ Json не содержит ключ 'name'"
        assert response_as_dict[name] == expented_value, error_message

    @staticmethod
    def assert_json_has_key(response: Response, name):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"Ответ не в Json формате. Ответ текста '{response.text}'"
        assert name in response_as_dict, f"Ответ Json не содержит ключ '{name}'"

    @staticmethod
    def assert_code_status(response: Response, expected_status_code):
        assert response.status_code == expected_status_code, f"Ответ статус кода {response.status_code}, не соответсвует ожидаемому {expected_status_code}"

    @staticmethod
    def assert_json_has_not_key(response: Response, name):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"Ответ не в Json формате. Ответ текста '{response.text}'"
        assert name not in response_as_dict, f"Ответ Json содержит ключ '{name}'"

    @staticmethod
    def assert_json_has_keys(response: Response, names: list, locat):
        try:
            response_as_dict = response.json()[locat]
        except json.JSONDecodeError:
            assert False, f"Ответ не в Json формате. Ответ текста '{response.text}'"
        for name in names:
            assert name in response_as_dict, f"Ответ Json не содержит ключ '{names}'"

    @staticmethod
    def assert_json_has_keys_for_books(response: Response, names: list, locat):

        try:
            json_obj = response.json()[locat]
        except json.JSONDecodeError:
            print("JSON ответ не в формате")

        for key in names:
            if key not in json_obj[0]:
                print(f"Ключ {key} отсутствует в JSON ответе")
                exit(1)

        for book in json_obj:
            for key in names[1:]:
                if key not in book:
                    print(f"Ключ {key} отсутствует в книге {book['name']}")
                    exit(1)

    @staticmethod
    def assert_json_values_is_number(response: Response, name, locat):

        try:
            json_obj = response.json()[locat]
        except json.JSONDecodeError:
            print("JSON ответ не в формате")

        for value in json_obj:
            assert isinstance(value[name], int), f"Значение {value[name]} не является числом"

    @staticmethod
    def assert_json_values_is_bool(response: Response, name, locat):

        try:
            json_obj = response.json()[locat]
        except json.JSONDecodeError:
            print("JSON ответ не в формате")

        for value in json_obj:
            assert isinstance(value[name], bool), f"Значение {value[name]} не является Логическим типом данных"

    @staticmethod
    def assert_json_value_is_bool(response: Response, name, locat):

        try:
            json_obj = response.json()[locat]
        except json.JSONDecodeError:
            print("JSON ответ не в формате")

        assert isinstance(json_obj[name], bool), f"Значение {json_obj[name]} не является Логическим типом данных"

    @staticmethod
    def assert_json_value_is_number(response: Response, name, locat):

        try:
            json_obj = response.json()[locat]
        except json.JSONDecodeError:
            print("JSON ответ не в формате")

        assert isinstance(json_obj[name], int), f"Значение {json_obj[name]} не является числом"


