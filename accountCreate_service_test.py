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
                    "docId": {"type": "string"},
                    "colvirProcessId": {"type": "string"},
                    "number": {"type": "string"},
                    "department": {"type": "string"},
                    "ledgerAccount": {"type": "string"},
                    "currency": {"type": "string"},
                    "serviceGroup": {"type": "string"},
                    "clientCode": {"type": "string"},
                    "name": {"type": "string"},
                    "shortName": {"type": "string"}
                },
                "required": ["depId", "docId", "colvirProcessId", "number", "department", "ledgerAccount", "currency", "serviceGroup", "clientCode", "name", "shortName"]
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
        "department": "125008",
        "ledgerAccount": "20201",
        "serviceGroup": "125008.000",
        "client": "008.119115",
        "name": "Мухамеджданова Марьям Ахмаджановна",
        "currency": "KGS"
    },
    # Другие наборы данных можно добавить здесь
])

# Функция для формирования тела запроса
def get_service_accountCreate_body(client_data):
    current_body = data.service_accountCreate_body.copy()
    current_body["id"] = str(uuid.uuid4())
    current_body["body"][0].update(client_data)
    return current_body

def positive_assert_accountCreate_body(client_data):
    service_accountCreate_body = get_service_accountCreate_body(client_data)
    payment_response = esb_request.service_post(service_accountCreate_body)
    with allure.step("Проверка отправленного запроса"):
        allure.attach("Request", json.dumps(service_accountCreate_body, ensure_ascii=False), allure.attachment_type.JSON)
    with allure.step("Проверка тела ответа"):
        allure.attach("Response", str(payment_response.text), allure.attachment_type.TEXT)
        check_response_with_schema(payment_response.json())
    with allure.step("Проверка статуса ответа"):
        assert payment_response.status_code == 200

    with allure.step("Проверка сообщения об успехе в ответе"):
        assert payment_response.json()["responseMessage"] == "Счёт успешно создан"

@allure.suite("(account.create) Создание счета клиента")
class TestClientCreateSuite:
    @allure.sub_suite("Положительные тесты с различными значениями body")
    @allure.title("Создание счета клиента (Физ лицо, KGS)")
    @pytest.mark.parametrize("client_data", [
        {
            "department": "125008",
            "ledgerAccount": "20201",
            "serviceGroup": "125008.000",
            "client": "008.119115",
            "name": "Мухамеджанова Марьям Ахмаджановна",
            "currency": "KGS"
        },
    ])
    def test_create_client(self, client_data):
        positive_assert_accountCreate_body(client_data)

    @allure.sub_suite("Положительные тесты с различными значениями body")
    @allure.title("Создание счета клиента (Физ лицо, USD)")
    @pytest.mark.parametrize("client_data", [
        {
            "department": "125008",
            "ledgerAccount": "20201",
            "serviceGroup": "125008.000",
            "client": "008.119115",
            "name": "Мухамеджанова Марьям Ахмаджановна",
            "currency": "USD"
        },
    ])
    def test_create_client2(self, client_data):
        positive_assert_accountCreate_body(client_data)

