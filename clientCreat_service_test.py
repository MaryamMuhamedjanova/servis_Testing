import uuid

import allure
import pytest
import json
import jsonschema
import data
import esb_request

# JSON Schema для описания ожидаемой структуры ответа от сервиса
# Updated response schema
response_schema = {
    "type": "object",
    "properties": {
        "version": {"type": "string"},
        "type": {"type": "string"},
        "id": {"type": "string"},
        "dateTime": {"type": "string"},
        "source": {"type": "string"},
        "restartAllowed": {"type": "integer"},
        "responseCode": {"type": "string"},
        "responseMessage": {"type": "string"},
        "body": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "depId": {"type": "string"},
                    "Id": {"type": "string"},
                    "OrdId": {"type": "string"},
                    "absCode": {"type": "string"},
                    "docDate": {"type": "string"},
                    "addresses": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "value": {"type": "string"},
                                "addressId": {"type": "integer"},
                                "bpmId": {"type": ["string", "null"]},
                                "nord": {"type": "integer"}
                            },
                            "required": ["value", "addressId", "bpmId", "nord"]
                        }
                    }
                },
                "required": ["depId", "Id", "OrdId", "absCode", "docDate", "addresses"]
            }
        }
    },
    "required": ["version", "type", "id", "dateTime", "source", "restartAllowed", "responseCode", "responseMessage", "body"]
}


# Функция для проверки ответа с использованием JSON Schema
def check_response_with_schema(response_json):
    jsonschema.validate(instance=response_json, schema=response_schema)

# Остальной код остается таким же, но использует новую функцию check_response_with_schema
# Функция для формирования тела запроса
# Функция для проверки полей в объекте accountDebit

def decode_russian_text(text):
    return text.encode('utf-8').decode('unicode_escape')


# Параметризованные данные для теста
@pytest.mark.parametrize("client_data", [
    {
        "department": "125003",
        "serviceGroup": "125003.000",
        "surname": "Бебеза",
        "name": "Лора",
        "fatherName": "Юсузовна",
        "shortName": "Бебеза Л.",
        "latinSurname": "Bebeza",
        "latinName": "Lora",
        "latinFatherName": "Iusuzovna",
        "notes": "UZENBAEVA",
        "pastName": "Bebeza Lora",
        "inn": "10601198800049",
        "birthDate": "11.08.1993",
        "pboyulFl": 0,
        "jurFl": 0,
        "residFl": 1,
        "citizenship": "KG",
        "economySector": "9",
        "economyBranch": "115",
        "sex": "M",
        "title": 1,
        "trfPlnCategory": "2003"
    },
    # Другие наборы данных можно добавить здесь
])

# Функция для формирования тела запроса
def get_service_clientCreate_body(client_data):
    current_body = data.service_clientCreate_body.copy()
    current_body["id"] = str(uuid.uuid4())
    current_body["body"][0].update(client_data)
    return current_body

# Функция для проверки создания клиента
def positive_assert_create_client(client_data):
    service_clientCreate_body = get_service_clientCreate_body(client_data)
    payment_response = esb_request.service_post(service_clientCreate_body)

    # Добавляем запрос как шаг в отчет Allure
    with allure.step("Проверка отправленного запроса"):
        allure.attach("Request", json.dumps(service_clientCreate_body, ensure_ascii=False), allure.attachment_type.JSON)

    # Проверяем ответ
    with allure.step("Проверка тела ответа"):
        allure.attach("Response", str(payment_response.text), allure.attachment_type.TEXT)
        # Проверка ответа с использованием JSON Schema
        check_response_with_schema(payment_response.json())

    # Проверка статуса ответа
    with allure.step("Проверка статуса ответа"):
        assert payment_response.status_code == 200

    # Проверка сообщения об успехе в ответе
    with allure.step("Проверка сообщения об успехе в ответе"):
        assert payment_response.json()["responseMessage"] == "Клиент создан"

# Класс с тестами
@allure.suite("(client.create) Создание карточки клиента")
class TestClientCreateSuite:
    # Параметризованный тест
    @allure.sub_suite("Положительные тесты с различными значениями body")
    @allure.title("Создание карточки клиента (Физ лицо)")
    @pytest.mark.parametrize("client_data", [
        {
            "department": "125003",
            "serviceGroup": "125003.000",
            "surname": "Бебеза",
            "name": "Лора",
            "fatherName": "Юсузовна",
            "shortName": "Бебеза Л.",
            "latinSurname": "Bebeza",
            "latinName": "Lora",
            "latinFatherName": "Iusuzovna",
            "notes": "UZENBAEVA",
            "pastName": "Bebeza Lora",
            "inn": "10601198800049",
            "birthDate": "11.08.1993",
            "pboyulFl": 0,
            "jurFl": 0,
            "residFl": 1,
            "citizenship": "KG",
            "economySector": "9",
            "economyBranch": "115",
            "sex": "M",
            "title": 1,
            "trfPlnCategory": "2003"
        },
    ])
    def test_create_client(self, client_data):
        positive_assert_create_client(client_data)

