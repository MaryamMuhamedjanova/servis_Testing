import uuid

import allure
import pytest
import json
import jsonschema
import data
import esb_request

# JSON Schema для описания ожидаемой структуры ответа от сервиса
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
                    "dea_dep_id": {"type": "integer"},
                    "dea_id": {"type": "integer"},
                    "dea_department": {"type": "string"},
                    "dea_absCode": {"type": "string"},
                    "acc_dep_id": {"type": "integer"},
                    "acc_id": {"type": "integer"},
                    "acc_department": {"type": "string"},
                    "acc_absCode": {"type": "string"},
                    "psCode": {"type": "string"},
                    "docDate": {"type": "string"}
                },
                "required": ["dea_dep_id", "dea_id", "dea_department", "dea_absCode", "acc_dep_id", "acc_id", "acc_department", "acc_absCode", "psCode", "docDate"]
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
@pytest.mark.parametrize("deposit_data", [
    {
        "department": "125008",
        "dclCode": "NV",
        "subDclCode": "NVCRM",
        "creTermType": "M",
        "creTerm": 36,
        "prcRate": 12.0,
        "currency": "KGS",
        "amount": 700.0,
        "date": "11.09.2023",
        "absCode": "008.119115"
    },
    # Другие наборы данных можно добавить здесь
])

# Функция для формирования тела запроса
def get_service_depositCreate_body(deposit_data):
    current_body = data.service_depositCreate_body.copy()
    current_body["id"] = str(uuid.uuid4())
    current_body["body"][0].update(deposit_data)
    return current_body

# Функция для проверки создания клиента
def positive_assert_create_client(deposit_data):
    service_depositCreate_body = get_service_depositCreate_body(deposit_data)
    payment_response = esb_request.service_post(service_depositCreate_body)

    # Добавляем запрос как шаг в отчет Allure
    with allure.step("Проверка отправленного запроса"):
        allure.attach("Request", json.dumps(service_depositCreate_body, ensure_ascii=False), allure.attachment_type.JSON)

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
        assert payment_response.json()["responseMessage"] == "Договор создан"

# Класс с тестами
@allure.suite("(deposit.create) Создание депозита")
class TestClientCreateSuite:
    # Параметризованный тест
    @allure.sub_suite("Положительные тесты с различными значениями body")
    @allure.title("Создание депозита (Физ лицо, продукт:копилка)")
    @pytest.mark.parametrize("deposit_data", [
        {
      "department": "125008",
      "dclCode": "NV",
      "subDclCode": "NVCRM",
      "creTermType": "M",
      "creTerm": 36,
      "prcRate": 12.0,
      "currency": "KGS",
      "amount": 700.0,
      "date": "11.09.2023",
      "absCode": "008.119115"

        }
        # Добавьте другие тестовые данные здесь, если необходимо
    ])
    def test_create_client(self, deposit_data):
        positive_assert_create_client(deposit_data)

