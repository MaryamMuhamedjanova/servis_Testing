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
                    "currentOperationDate": {"type": "string"},
                    "department": {"type": "string"},
                    "cashCode": {"type": "string"},
                    "cashAddress": {"type": "string"},
                    "cashType": {"type": "string"},
                    "colvirUser": {"type": "string"},
                    "cashierFullName": {"type": "string"},
                    "cashierArchiveFl": {"type": "integer"},
                    "cashierBanFl": {"type": "integer"},
                    "cashierARM": {"type": "string"},
                    "cashState": {"type": "string"},
                    "cashInventories": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "code": {"type": "string"},
                                "name": {"type": "string"},
                                "cashFl": {"type": "string"},
                                "currency": {"type": "string"},
                                "moveType": {"type": "string"},
                                "amount": {"type": "number"}
                            },
                            "required": ["code", "name", "cashFl", "moveType", "amount"]
                        }
                    }
                },
                "required": ["currentOperationDate", "department", "cashCode", "cashAddress", "cashType", "colvirUser", "cashierFullName", "cashierArchiveFl", "cashierBanFl", "cashierARM", "cashState", "cashInventories"]
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
        "colvirUser": "",
        "department": "",
        "cashFl": "",

    },
])

# Функция для формирования тела запроса
def get_service_directoriesCashInventoryItemsRead_body(client_data):
    current_body = data.service_directoriesCashInventoryItemsRead_body.copy()
    current_body["id"] = str(uuid.uuid4())
    current_body["body"][0].update(client_data)
    return current_body

def positive_assert_directoriesCashInventoryItemsRead_body(client_data):
    service_directoriesCashInventoryItemsRead_body = get_service_directoriesCashInventoryItemsRead_body(client_data)
    payment_response = esb_request.service_post(service_directoriesCashInventoryItemsRead_body)
    with allure.step("Проверка отправленного запроса"):
        allure.attach("Request", json.dumps(service_directoriesCashInventoryItemsRead_body, ensure_ascii=False), allure.attachment_type.JSON)
    with allure.step("Проверка тела ответа"):
        allure.attach("Response", str(payment_response.text), allure.attachment_type.TEXT)
        check_response_with_schema(payment_response.json())
    with allure.step("Проверка статуса ответа"):
        assert payment_response.status_code == 200
    with allure.step("Проверка сообщения об успехе в ответе"):
        assert payment_response.json()["responseMessage"] == "Успешно"

@allure.suite("(directories.cashInventoryItems.read) Просмотр наличных средств в кассе")
class TestClientCreateSuite:
    @allure.sub_suite("Положительные тесты с различными значениями body")
    @allure.title("Список ценностей по всем кассам")
    @pytest.mark.parametrize("client_data", [{
        "colvirUser": "",
        "department": "",
        "cashFl": "",
    }
    ])
    def test_create_client(self, client_data):
        positive_assert_directoriesCashInventoryItemsRead_body(client_data)

    @allure.sub_suite("Положительные тесты с различными значениями body")
    @allure.title("Данные касс, за которыми закреплен кассир (NISAKOVA)")
    @pytest.mark.parametrize("client_data", [{
            "colvirUser": "NISAKOVA",
            "department": "",
            "cashFl": "",
    }
    ])
    def test_create_client1(self, client_data):
        positive_assert_directoriesCashInventoryItemsRead_body(client_data)

    @allure.sub_suite("Положительные тесты с различными значениями body")
    @allure.title("Данные по кассам подразделения (Бишкек)")
    @pytest.mark.parametrize("client_data", [{
            "colvirUser": "",
            "department": "125008",
            "cashFl": "",
    }
    ])
    def test_create_client2(self, client_data):
        positive_assert_directoriesCashInventoryItemsRead_body(client_data)

    @allure.sub_suite("Положительные тесты с различными значениями body")
    @allure.title("Денежные ценности в кассах")
    @pytest.mark.parametrize("client_data", [{
            "colvirUser": "",
            "department": "",
            "cashFl": "1",
    }
    ])
    def test_create_client3(self, client_data):
        positive_assert_directoriesCashInventoryItemsRead_body(client_data)

    @allure.sub_suite("Положительные тесты с различными значениями body")
    @allure.title("Неденежные ценности в кассах")
    @pytest.mark.parametrize("client_data", [{
            "colvirUser": "",
            "department": "",
            "cashFl": "0",
    }
    ])
    def test_create_client4(self, client_data):
        positive_assert_directoriesCashInventoryItemsRead_body(client_data)