import uuid
import allure
import pytest
import json
import jsonschema
import data
import esb_request

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
                    "code": {"type": "string"},
                    "name": {"type": "string"},
                    "operation": {"type": "string"},
                    "date": {"type": "string"},
                    "amount": {"type": "number"},
                    "currency": {"type": "string"},
                    "accountDebit": {
                        "type": "object",
                        "properties": {
                            "number": {"type": "string"},
                            "department": {"type": "string"}
                        },
                        "required": ["number", "department"]
                    },
                    "accountCredit": {
                        "type": "object",
                        "properties": {
                            "department": {"type": "string"}
                        },
                        "required": ["department"]
                    }
                },
                "required": ["code", "name", "operation", "date", "amount", "currency", "accountDebit", "accountCredit"]
            }
        }
    },
    "required": ["version", "type", "id", "dateTime", "source", "restartAllowed", "responseCode", "responseMessage", "body"]
}

def check_response_with_schema(response_json):
    jsonschema.validate(instance=response_json, schema=response_schema)

def decode_russian_text(text):
    return text.encode('utf-8').decode('unicode_escape')

@pytest.mark.parametrize("client_data", [
    {
        "operation": "BC1021",
        "amount": 1000000.00,
        "currency": "KGS",
        "client": "008.069991",
        "clientAccount": {
            "department": "125008",
            "number": "1250820000899159"
        },
        "accountDebit": {
            "department": "125008",
            "number": "1250820000899159"
        },
        "accountCredit": {
            "department": "125008"
        }
    },

])

def get_service_commissionCalculator_body(client_data):
    current_body = data.service_commissionCalculator_body.copy()
    current_body["id"] = str(uuid.uuid4())
    current_body["body"][0].update(client_data)
    return current_body

def positive_assert_commissionCalculator_body(client_data):
    service_commissionCalculator_body = get_service_commissionCalculator_body(client_data)
    payment_response = esb_request.service_post(service_commissionCalculator_body)
    with allure.step("Проверка отправленного запроса"):
        allure.attach("Request", json.dumps(service_commissionCalculator_body, ensure_ascii=False), allure.attachment_type.JSON)
    with allure.step("Проверка тела ответа"):
        allure.attach("Response", str(payment_response.text), allure.attachment_type.TEXT)
        check_response_with_schema(payment_response.json())
    with allure.step("Проверка статуса ответа"):
        assert payment_response.status_code == 200
    with allure.step("Проверка сообщения об успехе в ответе"):
        assert payment_response.json()["responseMessage"] == "Комиссия рассчитана"

@allure.suite("(commission.calculator) Калькулятор комиссий")
class TestClientCreateSuite:
    @allure.sub_suite("Положительные тесты с различными значениями body")
    @allure.title("Счет клиента и счет списания комиссии один и тот же")
    @pytest.mark.parametrize("client_data", [
        {
            "operation": "BC1021",
            "amount": 1000000.00,
            "currency": "KGS",
            "client": "008.069991",
            "clientAccount": {
                "department": "125008",
                "number": "1250820000899159"
            },
            "accountDebit": {
                "department": "125008",
                "number": "1250820000899159"
            },
            "accountCredit": {
                "department": "125008"
            }
        },
    ])
    def test_create_client(self, client_data):
        positive_assert_commissionCalculator_body(client_data)

    @allure.sub_suite("Положительные тесты с различными значениями body")
    @allure.title("Счет клиента и счет списания комиссии разные")
    @pytest.mark.parametrize("client_data", [
        {
            "operation": "BC1021",
            "amount": 1000000.00,
            "currency": "KGS",
            "client": "008.119115",
            "clientAccount": {
                "department": "125008",
                "number": "1250820000899159"
            },
            "accountDebit": {
                "department": "125008",
                "number": "1250820004787445"
            },
            "accountCredit": {
                "department": "125008"
            }
        },
    ])
    def test_create_client_2(self, client_data):
        positive_assert_commissionCalculator_body(client_data)
