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
                    "dep_id": {"type": "integer"},
                    "id": {"type": "integer"},
                    "absCode": {"type": "string"},
                    "docDate": {"type": "string"},
                    "efficientInterestRate": {"type": "number"}
                },
                "required": ["dep_id", "id", "absCode", "docDate", "efficientInterestRate"]
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
      "department": "125002",
      "absCode": "008.119115",
      "dclCode": "013НС_А",
      "creditCode": "02N-КД-24-54816/1-РБ",
      "creditStartDate": "15.03.2024",
      "creditRegDate": "15.03.2024",
      "creTermType": "M",
      "creTerm": 12,
      "currency": "KGS",
      "amount": 30000.00,
      "creIssueFee": 0.00,
      "prcRate": 24.00,
      "principalOverdueFee": 0.07,
      "crePurposeId": 187
    },
    # Другие наборы данных можно добавить здесь
])

# Функция для формирования тела запроса
def get_service_creditCreate_body(deposit_data):
    current_body = data.service_creditCreate_body.copy()
    current_body["id"] = str(uuid.uuid4())
    current_body["body"][0].update(deposit_data)
    return current_body

# Функция для проверки создания клиента
def positive_assert_create_client(deposit_data):
    service_creditCreate_body = get_service_creditCreate_body(deposit_data)
    payment_response = esb_request.service_post(service_creditCreate_body)

    # Добавляем запрос как шаг в отчет Allure
    with allure.step("Проверка отправленного запроса"):
        allure.attach("Request", json.dumps(service_creditCreate_body, ensure_ascii=False), allure.attachment_type.JSON)

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
        assert payment_response.json()["responseMessage"] == "Кредит создан и выдан"

# Класс с тестами
@allure.suite("(credit.create) Создание кредита")
class TestClientCreateSuite:
    # Параметризованный тест
    @allure.sub_suite("Положительные тесты с различными значениями body")
    @allure.title("Создание кредита (Физ лицо, продукт:013НС_А)")
    @pytest.mark.parametrize("deposit_data", [
        {
            "department": "125002",
            "absCode": "008.119115",
            "dclCode": "013НС_А",
            "creditCode": "02N-КД-24-54816/1-РБ",
            "creditStartDate": "15.03.2024",
            "creditRegDate": "15.03.2024",
            "creTermType": "M",
            "creTerm": 12,
            "currency": "KGS",
            "amount": 30000.00,
            "creIssueFee": 0.00,
            "prcRate": 24.00,
            "principalOverdueFee": 0.07,
            "crePurposeId": 187
        }
        # Добавьте другие тестовые данные здесь, если необходимо
    ])
    def test_create_client(self, deposit_data):
        positive_assert_create_client(deposit_data)

