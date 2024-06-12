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
        "elementCount": {"type": "integer"},
        "maximumEditingTime": {"type": "string"},
        "body": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "depId": {"type": "integer"},
                    "id": {"type": "integer"},
                    "serviceDepCode": {"type": "string"},
                    "cli_absCode": {"type": "string"},
                    "editingTime": {"type": "string"},
                    "productCode": {"type": "string"},
                    "productName": {"type": "string"},
                    "dea_absCode": {"type": "string"},
                    "depo_StatusCode": {"type": "string"},
                    "depo_Status": {"type": "string"},
                    "registrationDate": {"type": "string"},
                    "dateFrom": {"type": "string"},
                    "dateTo": {"type": "string"},
                    "dateInterestStart": {"type": "string"},
                    "depoPeriod": {"type": "string"},
                    "depoCurrency": {"type": "string"},
                    "depoAmount": {"type": "number"},
                    "depoAccountNumber": {"type": "string"},
                    "depoBalance": {"type": "number"},
                    "prolongationAmount": {"type": "number"},
                    "executedByCode": {"type": "string"},
                    "executedByName": {"type": "string"},
                    "depositPaymentSettings": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "amountType": {"type": "string"},
                                "paymentType": {"type": "string"},
                                "paymentDetails": {"type": "string"},
                                "correctdt": {"type": "string"}
                            }
                        }
                    },
                    "depositPaymentSums": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "amountType": {"type": "string"},
                                "paymentTerm": {"type": ["string", "null"]},
                                "individualPrcFl": {"type": "string"},
                                "interestRate": {"type": ["number", "null"]}
                            }
                        }
                    },
                    "depositAnalytics": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "analyticsType": {"type": "string"},
                                "analyticsName": {"type": "string"},
                                "analyticsCode": {"type": "string"}
                            }
                        }
                    },
                    "depositTrustees": {"type": "array", "items": {"type": "object"}},
                    "depositInheritors": {"type": "array", "items": {"type": "object"}},
                    "depositParameters": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "parameterName": {"type": "string"},
                                "parameterValue": {"type": ["string", "null"]}
                            }
                        }
                    }
                },
                "required": [
                    "depId", "id", "serviceDepCode", "cli_absCode", "editingTime", "productCode", "productName",
                    "dea_absCode", "depo_StatusCode", "depo_Status", "registrationDate", "dateFrom", "dateTo",
                    "dateInterestStart", "depoPeriod", "depoCurrency", "depoAmount", "depoAccountNumber",
                    "depoBalance", "prolongationAmount", "executedByCode", "executedByName", "depositPaymentSettings",
                    "depositPaymentSums", "depositAnalytics", "depositTrustees", "depositInheritors", "depositParameters"
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
    "dea_absCode": [
                "22-8-Д/NN-004608"
            ],
            "readingParameters": {
                "depositPaymentSettings": True,
                "depositPaymentSums": True,
                "depositAnalytics": True,
                "depositParameters": True,
                "depositTrustees": True,
                "depositInheritors": True
            }
    }
])

def get_service_depositRead_body(client_data):
    current_body = data.service_depositRead_body.copy()
    current_body["id"] = str(uuid.uuid4())
    current_body["body"][0].update(client_data)
    return current_body

def positive_assert_service_depositRead_body(client_data):
    service_depositRead_body = get_service_depositRead_body(client_data)
    payment_response = esb_request.service_post(service_depositRead_body)
    with allure.step("Проверка отправленного запроса"):
        allure.attach("Request", json.dumps(service_depositRead_body, ensure_ascii=False), allure.attachment_type.JSON)
    with allure.step("Проверка тела ответа"):
        allure.attach("Response", str(payment_response.text), allure.attachment_type.TEXT)
        check_response_with_schema(payment_response.json())
    with allure.step("Проверка статуса ответа"):
        assert payment_response.status_code == 200
    with allure.step("Проверка сообщения об успехе в ответе"):
        assert payment_response.json()["responseMessage"] == "Успешно"

@allure.suite("(deposit.read) Запрос информации по депозиту(ам).")
class TestClientCreateSuite:
    @allure.sub_suite("Положительные тесты с различными значениями body")
    @allure.title("Запрос инфы по депозиту физ лица")
    @pytest.mark.parametrize("client_data", [
        {
            "dea_absCode": [
                "22-8-Д/NN-004608"
            ],
            "readingParameters": {
                "depositPaymentSettings": True,
                "depositPaymentSums": True,
                "depositAnalytics": True,
                "depositParameters": True,
                "depositTrustees": True,
                "depositInheritors": True
            }
        },
    ])
    def test_create_client(self, client_data):
        positive_assert_service_depositRead_body(client_data)
