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
                    "depId": {"type": "integer"},
                    "ordId": {"type": "integer"},
                    "absCode": {"type": "string"},
                    "owCode": {"type": "string"},
                    "elCode": {"type": "string"},
                    "pboyulFl": {"type": "integer"},
                    "surName": {"type": "string"},
                    "name": {"type": "string"},
                    "fatherName": {"type": "string"},
                    "taxCode": {"type": "string"},
                    "trustedNumber": {"type": "string"},
                    "latSurName": {"type": "string"},
                    "latName": {"type": "string"},
                    "latFatherName": {"type": "string"},
                    "birthDate": {"type": "string"},
                    "blackListFlag": {"type": "integer"},
                    "residFl": {"type": "integer"},
                    "department": {"type": "string"},
                    "fullName": {"type": "string"},
                    "nation": {"type": "string"},
                    "maritalStatus": {"type": "string"},
                    "workPostion": {"type": "string"},
                    "workOrganization": {"type": "string"},
                    "registrationCountryCode": {"type": "string"},
                    "registrationCountryName": {"type": "string"},
                    "citizenshipCode": {"type": "string"},
                    "citizenshipName": {"type": "string"},
                    "arcFl": {"type": "integer"},
                    "cardStatus": {"type": "string"},
                    "creditAvailFl": {"type": "integer"},
                    "identityDocuments": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "nord": {"type": "integer"},
                                "code": {"type": "string"},
                                "id": {"type": "integer"},
                                "name": {"type": "string"},
                                "issueDate": {"type": "string"},
                                "expireDate": {"type": "string"},
                                "series": {"type": "string"},
                                "passpNum": {"type": "string"},
                                "issuer": {"type": "string"},
                                "defaultFl": {"type": "string"},
                                "archiveFl": {"type": "string"}
                            },
                            "required": [
                                "nord", "code", "id", "name", "issueDate", "expireDate", "series", "passpNum", "issuer", "defaultFl", "archiveFl"
                            ]
                        }
                    },
                    "addresses": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "addressType": {"type": "string"},
                                "addressTypeCode": {"type": "string"},
                                "addressTypeName": {"type": "string"},
                                "ownershipType": {"type": ["string", "null"]},
                                "ownershipTypeCode": {"type": ["string", "null"]},
                                "ownershipTypeName": {"type": ["string", "null"]},
                                "addressId": {"type": "integer"},
                                "addressName": {"type": "string"},
                                "correctdt": {"type": "string"}
                            },
                            "required": [
                                "addressType", "addressTypeCode", "addressTypeName", "ownershipType", "ownershipTypeCode", "ownershipTypeName", "addressId", "addressName", "correctdt"
                            ]
                        }
                    }
                },
                "required": [
                    "depId", "ordId", "absCode", "owCode", "elCode", "pboyulFl", "surName", "name", "fatherName", "taxCode", "trustedNumber",
                    "latSurName", "latName", "latFatherName", "birthDate", "blackListFlag", "residFl", "department", "fullName", "nation",
                    "maritalStatus", "workPostion", "workOrganization", "registrationCountryCode", "registrationCountryName", "citizenshipCode",
                    "citizenshipName", "arcFl", "cardStatus", "creditAvailFl", "identityDocuments", "addresses"
                ]
            }
        }
    },
    "required": [
        "version", "type", "id", "dateTime", "source", "restartAllowed", "responseCode", "responseMessage", "body"
    ]
}


def check_response_with_schema(response_json):
    jsonschema.validate(instance=response_json, schema=response_schema)

def decode_russian_text(text):
    return text.encode('utf-8').decode('unicode_escape')

@pytest.mark.parametrize("client_data", [
    {
        "taxCode": "12006200000711",
        "pboYulFl": 0
    }
])

def get_service_clientRead_body(client_data):
    current_body = data.service_clientRead_v2_body.copy()
    current_body["id"] = str(uuid.uuid4())
    current_body["body"][0].update(client_data)
    return current_body

def positive_assert_clientRead_body(client_data):
    service_clientRead_body = get_service_clientRead_body(client_data)
    payment_response = esb_request.service_post(service_clientRead_body)
    with allure.step("Проверка отправленного запроса"):
        allure.attach("Request", json.dumps(service_clientRead_body, ensure_ascii=False), allure.attachment_type.JSON)
    with allure.step("Проверка тела ответа"):
        allure.attach("Response", str(payment_response.text), allure.attachment_type.TEXT)
        check_response_with_schema(payment_response.json())
    with allure.step("Проверка статуса ответа"):
        assert payment_response.status_code == 200
    with allure.step("Проверка сообщения об успехе в ответе"):
        assert payment_response.json()["responseMessage"] == "Успешно"

@allure.suite("(client.read) Запрос информации по клиенту(ам) VERSION2")
class TestClientCreateSuite:
    @allure.sub_suite("Положительные тесты с различными значениями body")
    @allure.title("Поиск по ИНН физ лица")
    @pytest.mark.parametrize("client_data", [
        {
            "taxCode": "12006200000711",
            "pboYulFl": 0
        },
    ])
    def test_create_client(self, client_data):
        positive_assert_clientRead_body(client_data)
