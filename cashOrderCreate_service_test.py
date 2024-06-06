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
                    "docNum": {"type": "string"},
                    "sumProp": {"type": "string"},
                    "docDate": {"type": "string"}
                },
                "required": ["depId", "docId", "colvirProcessId", "docNum", "sumProp", "docDate"]
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
            "incomFl": 1,
            "accountDebit": {
                "department": "125008"
            },
            "accountCredit": {
                "department": "125008",
                "number": "1250820004787445",
                "currency": "KGS"
            },
            "amount": 19.00,
            "currency": "KGS",
            "bnkOper": "B1010",
            "docNum": "09-035832",
            "docDate": "31.05.2024",
            "operDate": "31.05.2024",
            "knp": {
                "gkpo": "55303005",
                "pb": "",
                "vpb": ""
            },
            "description": "Пополнение счета",
            "payer": "Рысбеков Серик Токторбайевич",
            "identityDocument": "Паспорт гражданина КР (ID-карта) ID 1551801 МКК 211031 17.01.2020",
            "additionalInfo": [
                {
                    "code": "Z069_ADDRESS",
                    "value": "КЫРГЫЗСТАН, ИССЫК- КУЛСЬКАЯ обл, ИССЫК КУЛЬКИЙ р-н, БАЛЫКЧИ г, ЛЕОНОВА ул, дом 15"
                },
                {
                    "code": "Z069_BIRTHDATE",
                    "value": "25.05.1984"
                },
                {
                    "code": "Z069_BIRTHPLACE",
                    "value": ""
                },
                {
                    "code": "Z069_CITIZENSHIP",
                    "value": "Кыргызстан"
                },
                {
                    "code": "Z069_CONTACTS",
                    "value": "0772 677789"
                },
                {
                    "code": "Z069_INN",
                    "value": "22505198400193"
                },
                {
                    "code": "Z069_MARITAL",
                    "value": "Женат/Замужем"
                },
                {
                    "code": "Z069_NATIONALITY",
                    "value": "казах"
                },
                {
                    "code": "Z069_RESIDFL",
                    "value": "1"
                },
                {
                    "code": "Z069_VISA_REG",
                    "value": ""
                }
            ],
            "signatures": {
                "head": ""
            },
            "cashPlanSymbols": [
                {
                    "symbol": "13",
                    "amount": 19.00
                }
            ]
    },
    # Другие наборы данных можно добавить здесь
])

# Функция для формирования тела запроса
def get_service_cashOrderCreate_body(client_data):
    current_body = data.service_cashOrderCreate_body.copy()
    current_body["id"] = str(uuid.uuid4())
    current_body["body"][0].update(client_data)
    return current_body

def positive_assert_cashOrderCreate_body(client_data):
    service_cashOrderCreate_body = get_service_cashOrderCreate_body(client_data)
    payment_response = esb_request.service_post(service_cashOrderCreate_body)
    with allure.step("Проверка отправленного запроса"):
        allure.attach("Request", json.dumps(service_cashOrderCreate_body, ensure_ascii=False), allure.attachment_type.JSON)
    with allure.step("Проверка тела ответа"):
        allure.attach("Response", str(payment_response.text), allure.attachment_type.TEXT)
        check_response_with_schema(payment_response.json())
    with allure.step("Проверка статуса ответа"):
        assert payment_response.status_code == 200

    with allure.step("Проверка сообщения об успехе в ответе"):
        assert payment_response.json()["responseMessage"] == "Документ успешно создан"

@allure.suite("(cashOrder.create) Создание кассового документа")
class TestClientCreateSuite:
    @allure.sub_suite("Положительные тесты с различными значениями body")
    @allure.title("Приход через кассу")
    @pytest.mark.parametrize("client_data", [
        {
            "incomFl": 1,
            "accountDebit": {
                "department": "125008"
            },
            "accountCredit": {
                "department": "125008",
                "number": "1250820004787445",
                "currency": "KGS"
            },
            "amount": 19.00,
            "currency": "KGS",
            "bnkOper": "B1010",
            "docNum": "09-035832",
            "docDate": "31.05.2024",
            "operDate": "31.05.2024",
            "knp": {
                "gkpo": "55303005",
                "pb": "",
                "vpb": ""
            },
            "description": "Пополнение счета",
            "payer": "Рысбеков Серик Токторбайевич",
            "identityDocument": "Паспорт гражданина КР (ID-карта) ID 1551801 МКК 211031 17.01.2020",
            "additionalInfo": [
                {
                    "code": "Z069_ADDRESS",
                    "value": "КЫРГЫЗСТАН, ИССЫК- КУЛСЬКАЯ обл, ИССЫК КУЛЬКИЙ р-н, БАЛЫКЧИ г, ЛЕОНОВА ул, дом 15"
                },
                {
                    "code": "Z069_BIRTHDATE",
                    "value": "25.05.1984"
                },
                {
                    "code": "Z069_BIRTHPLACE",
                    "value": ""
                },
                {
                    "code": "Z069_CITIZENSHIP",
                    "value": "Кыргызстан"
                },
                {
                    "code": "Z069_CONTACTS",
                    "value": "0772 677789"
                },
                {
                    "code": "Z069_INN",
                    "value": "22505198400193"
                },
                {
                    "code": "Z069_MARITAL",
                    "value": "Женат/Замужем"
                },
                {
                    "code": "Z069_NATIONALITY",
                    "value": "казах"
                },
                {
                    "code": "Z069_RESIDFL",
                    "value": "1"
                },
                {
                    "code": "Z069_VISA_REG",
                    "value": ""
                }
            ],
            "signatures": {
                "head": ""
            },
            "cashPlanSymbols": [
                {
                    "symbol": "13",
                    "amount": 19.00
                }
            ]
        },
    ])
    def test_create_client(self, client_data):
        positive_assert_cashOrderCreate_body(client_data)
