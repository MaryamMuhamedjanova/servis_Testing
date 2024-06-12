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
        "elementCount": {"type": "integer"},
        "maximumEditingTime": {"type": "string"},
        "body": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "id": {"type": "integer"},
                    "dep_id": {"type": "integer"},
                    "ord_id": {"type": "integer"},
                    "department": {"type": "string"},
                    "number": {"type": "string"},
                    "processing": {"type": "string"},
                    "cliAbsCode": {"type": "string"},
                    "name": {"type": "string"},
                    "shortName": {"type": "string"},
                    "currency": {"type": "string"},
                    "ledgerAccount": {"type": "string"},
                    "deaBop": {"type": "string"},
                    "currentFl": {"type": "integer"},
                    "cardFl": {"type": "integer"},
                    "depositFl": {"type": "integer"},
                    "activeFl": {"type": "integer"},
                    "allowedWithdrawalFl": {"type": "integer"},
                    "allowedReplenishmentFl": {"type": "integer"},
                    "defaultFl": {"type": "integer"},
                    "capFl": {"type": "integer"},
                    "closeFl": {"type": "integer"},
                    "openDate": {"type": "string"},
                    "editingTime": {"type": "string"},
                    "bps": {
                        "type": "array",
                        "items": {"type": "string"}
                    },
                    "balance": {
                        "type": "object",
                        "properties": {
                            "balance": {"type": "number"},
                            "nationalCurrencyBalance": {"type": "number"},
                            "avaibleAmount": {"type": "number"},
                            "nationalCurrencyAvaibleAmount": {"type": "number"},
                            "hold": {"type": "number"},
                            "allowedDebitFl": {"type": "integer"},
                            "allowedCreditFl": {"type": "integer"}
                        }
                    },
                    "locks": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "id": {"type": "integer"},
                                "code": {"type": "string"},
                                "name": {"type": "string"},
                                "fromDate": {"type": "string"},
                                "toDate": {"type": "string"},
                                "note": {"type": "string"},
                                "document": {
                                    "type": "object",
                                    "properties": {
                                        "number": {"type": "string"},
                                        "organization": {"type": "string"},
                                        "date": {"type": "string"}
                                    }
                                },
                                "reference": {"type": "string"},
                                "editor": {"type": "string"},
                                "editingTime": {"type": "string"}
                            }
                        }
                    }
                },
                "required": [
                    "id", "dep_id", "ord_id", "department", "number", "processing", "cliAbsCode", "name",
                    "shortName", "currency", "ledgerAccount", "deaBop", "currentFl", "cardFl", "depositFl",
                    "activeFl", "allowedWithdrawalFl", "allowedReplenishmentFl", "defaultFl", "capFl",
                    "closeFl", "openDate", "editingTime", "bps", "balance", "locks"
                ]
            }
        }
    },
    "required": [
        "version", "type", "id", "dateTime", "source", "restartAllowed",
        "responseCode", "responseMessage", "elementCount", "maximumEditingTime", "body"
    ]
}


def check_response_with_schema(response_json):
    jsonschema.validate(instance=response_json, schema=response_schema)

def decode_russian_text(text):
    return text.encode('utf-8').decode('unicode_escape')

@pytest.mark.parametrize("client_data", [
    {
        "bps": ["1001"],
        "currency": ["KGS"],
        "closeFl": 0,
        "client": {
            "absCode": ["008.111493"]
        },
        "readingParameters": {
            "balance": True,
            "locks": True
        }
    },

])

def get_service_accountRead_body(client_data):
    current_body = data.service_accountRead_body.copy()
    current_body["id"] = str(uuid.uuid4())
    current_body["body"][0].update(client_data)
    return current_body

def positive_assert_accountRead_body(client_data):
    service_accountRead_body = get_service_accountRead_body(client_data)
    payment_response = esb_request.service_post(service_accountRead_body)
    with allure.step("Проверка отправленного запроса"):
        allure.attach("Request", json.dumps(service_accountRead_body, ensure_ascii=False), allure.attachment_type.JSON)
    with allure.step("Проверка тела ответа"):
        allure.attach("Response", str(payment_response.text), allure.attachment_type.TEXT)
        check_response_with_schema(payment_response.json())
    with allure.step("Проверка статуса ответа"):
        assert payment_response.status_code == 200
    with allure.step("Проверка сообщения об успехе в ответе"):
        assert payment_response.json()["responseMessage"] == "Успех"

@allure.suite("(account.read) Запрос информации по лицевым счетам")
class TestClientCreateSuite:
    @allure.sub_suite("Положительные тесты с различными значениями body")
    @allure.title("Получение информации по коду клиента")
    @pytest.mark.parametrize("client_data", [
        {
            "bps": ["1001"],
            "currency": ["KGS"],
            "closeFl": 0,
            "client": {
                "absCode": ["008.111493"]
            },
            "readingParameters": {
                "balance": True,
                "locks": True
            }
        },
    ])
    def test_create_client(self, client_data):
        positive_assert_accountRead_body(client_data)