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
        "version": {"type": "string", "const": "1.0"},
        "type": {"type": "string", "const": "007"},
        "id": {"type": "string", "format": "uuid"},
        "dateTime": {"type": "string", "format": "date-time"},
        "source": {"type": "string"},
        "restartAllowed": {"type": "integer"},
        "responseCode": {"type": "string"},
        "responseMessage": {"type": "string"},
        "body": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "responseCode": {"type": "string"},
                    "responseMessage": {"type": "string"},
                    "accountDebit": {
                        "type": "object",
                        "properties": {
                            "department": {"type": "string"},
                            "number": {"type": ["string", "null"]}
                        },
                        "required": ["department", "number"]
                    },
                    "docNum": {"type": "string"},
                    "sumProp": {"type": "string"},
                    "depId": {"type": "string"},
                    "docId": {"type": "string"},
                    "docDate": {"type": "string", "format": "date-time"}
                },
                "required": ["responseCode", "responseMessage", "accountDebit", "docNum",
                             "sumProp", "depId", "docId", "docDate"]
            }
        }
    },
    "required": ["version", "type", "id", "dateTime", "source", "restartAllowed",
                 "responseCode", "responseMessage", "body"]
}



# Функция для проверки ответа с использованием JSON Schema
def check_response_with_schema(response_json):
    jsonschema.validate(instance=response_json, schema=response_schema)

# Остальной код остается таким же, но использует новую функцию check_response_with_schema
# Функция для формирования тела запроса
# Функция для проверки полей в объекте accountDebit
def check_accountDebit_fields(accountDebit):
    expected_fields = [
        "department", "number", "currency", "name", "inn", "cardFl", "processing"
    ]
    for field in expected_fields:
        assert field in accountDebit, f"Поле '{field}' отсутствует в accountDebit"

def decode_russian_text(text):
    return text.encode('utf-8').decode('unicode_escape')


# Позитивный тест

# Функция для формирования тела запроса с учетом accountDebit и accountCredit
def service_007_body1(accountDebit, accountCredit):
    current_body = data.service_007_body.copy()
    current_body["body"][0]["accountDebit"] = accountDebit
    current_body["body"][0]["accountCredit"] = accountCredit
    return current_body

def positive_assert_amount_with_accountDebit_and_accountCredit(accountDebit, accountCredit):
    service_007_body = service_007_body1(accountDebit, accountCredit)
    payment_response = esb_request.service_post(service_007_body)
    # Добавляем запрос как шаг в отчет Allure
    with allure.step("Проверка отправленного запроса"):
        # Декодируем русский текст для accountDebit
        decoded_accountDebit = {key: decode_russian_text(value) if isinstance(value, str) else value for key, value in
                                accountDebit.items()}
        # Декодируем русский текст для accountCredit
        decoded_accountCredit = {key: decode_russian_text(value) if isinstance(value, str) else value for key, value in
                                 accountCredit.items()}
        # Преобразуем словари в JSON с декодированными данными
        decoded_body = {
            "body": [{
                "accountDebit": decoded_accountDebit,
                "accountCredit": decoded_accountCredit,
                **service_007_body["body"][0]
            }]
        }
        allure.attach("Request", json.dumps(decoded_body, ensure_ascii=False), allure.attachment_type.JSON)

        #allure.attach("Request", json.dumps(service_001_body1(accountDebit, accountCredit)), allure.attachment_type.JSON)
    # Проверяем ответ
    with allure.step("Проверка тела ответа"):
        allure.attach("Response", str(payment_response.text), allure.attachment_type.TEXT)
        # Проверка ответа с использованием JSON Schema
        check_response_with_schema(payment_response.json())
        # Проверка наличия полей в ответе для accountDebit
       # check_accountDebit_fields(accountDebit)
        # Проверка наличия полей в ответе для accountCredit
        #check_accountCredit_fields(accountCredit)
    # Проверка статуса ответа
    with allure.step("Проверка статуса ответа"):
        assert payment_response.status_code == 200
    # Проверка сообщения об успехе в ответе
    with allure.step("Проверка сообщения об успехе в ответе"):
        assert payment_response.json()["responseMessage"] == "Документ успешно создан"


# Класс с тестами
@allure.suite("Взнос наличных на банковский счет (007 сервис)")
class TestAmountSuite:
    # Параметризованный тест
    @allure.sub_suite("Тесты с различными значениями для счета кредита(accountCredit)")
    @allure.title("Взнос наличных на банковский счет (KGS)")
    @pytest.mark.parametrize("accountDebit, accountCredit", [
        (
                {
                    "department": "125001"
                },
                {
                    "department": "125001",
                    "number": "1250110000041083",
                    "currency": "KGS"
                }
        )
    ])

    def test_specific_accountDebit_and_accountCredit(self, accountDebit, accountCredit):
        positive_assert_amount_with_accountDebit_and_accountCredit(accountDebit, accountCredit)



