import uuid
import allure
import pytest
import json
import jsonschema
import data
import esb_request

response_schema ={
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
                    "absCode": {"type": "string"},
                    "editingTime": {"type": "string"},
                    "jurFl": {"type": "string"},
                    "pboyulFl": {"type": "string"},
                    "arcFl": {"type": "integer"},
                    "department": {"type": "string"},
                    "departmentName": {"type": "string"},
                    "serviceGroup": {"type": "string"},
                    "trfPlnCategory": {"type": "string"},
                    "registrationDate": {"type": "string"},
                    "surName": {"type": "string"},
                    "name": {"type": "string"},
                    "fatherName": {"type": "string"},
                    "fullName": {"type": "string"},
                    "latSurName": {"type": "string"},
                    "latName": {"type": "string"},
                    "latFatherName": {"type": "string"},
                    "latFullName": {"type": "string"},
                    "cardStatus": {"type": "string"},
                    "cardStatusCode": {"type": "string"},
                    "pastName": {"type": "string"},
                    "birthDate": {"type": "string"},
                    "deceaseDate": {"type": "string"},
                    "sex": {"type": "string"},
                    "title": {"type": "string"},
                    "residFl": {"type": "integer"},
                    "registrationCountryId": {"type": ["integer", "null"]},
                    "registrationCountryCode": {"type": "string"},
                    "registrationCountryName": {"type": "string"},
                    "citizenshipId": {"type": "integer"},
                    "citizenshipCode": {"type": "string"},
                    "citizenshipName": {"type": "string"},
                    "econBranchId": {"type": "integer"},
                    "econBranchCode": {"type": "string"},
                    "econBranchName": {"type": "string"},
                    "sectorId": {"type": "string"},
                    "sectorName": {"type": "string"},
                    "privateForm": {"type": ["null", "string"]},
                    "privateFormName": {"type": ["null", "string"]},
                    "operationForm": {"type": "string"},
                    "operationFormName": {"type": "string"},
                    "taxCode": {"type": "string"},
                    "taxAgencyCode": {"type": "string"},
                    "taxAgencyName": {"type": "string"},
                    "okpo": {"type": "string"},
                    "shortName": {"type": "string"},
                    "swiftName": {"type": "string"},
                    "executedBy": {"type": "string"},
                    "closeDate": {"type": "string"},
                    "regInitDate": {"type": "string"},
                    "managerAbsCode": {"type": "string"}
                },
                "required": [
                    "depId",
                    "id",
                    "absCode",
                    "editingTime",
                    "jurFl",
                    "pboyulFl",
                    "arcFl",
                    "department",
                    "departmentName",
                    "serviceGroup",
                    "trfPlnCategory",
                    "registrationDate",
                    "surName",
                    "name",
                    "fatherName",
                    "fullName",
                    "latSurName",
                    "latName",
                    "latFatherName",
                    "latFullName",
                    "cardStatus",
                    "cardStatusCode",
                    "pastName",
                    "birthDate",
                    "deceaseDate",
                    "sex",
                    "title",
                    "residFl",
                    "registrationCountryId",
                    "registrationCountryCode",
                    "registrationCountryName",
                    "citizenshipId",
                    "citizenshipCode",
                    "citizenshipName",
                    "econBranchId",
                    "econBranchCode",
                    "econBranchName",
                    "sectorId",
                    "sectorName",
                    "privateForm",
                    "privateFormName",
                    "operationForm",
                    "operationFormName",
                    "taxCode",
                    "taxAgencyCode",
                    "taxAgencyName",
                    "okpo",
                    "shortName",
                    "swiftName",
                    "executedBy",
                    "closeDate",
                    "regInitDate",
                    "managerAbsCode"
                ]
            }
        }
    },
    "required": [
        "version",
        "type",
        "id",
        "dateTime",
        "source",
        "restartAllowed",
        "responseCode",
        "responseMessage",
        "elementCount",
        "maximumEditingTime",
        "body"
    ]
}

def check_response_with_schema(response_json):
    jsonschema.validate(instance=response_json, schema=response_schema)

def decode_russian_text(text):
    return text.encode('utf-8').decode('unicode_escape')

@pytest.mark.parametrize("client_data", [
    {
        "absCode": [
            "008.119115"
        ],
        "roles": [
            "CLI",
            "AUT"
        ],
        "editingTime": {
            "from": "",
            "to": ""
        },
        "notEditedByAbsCodes": [
            "CRM2"
        ],
        "readingParameters": {
            "archiveFl": 0,
            "jurFl": 0,
            "pboYulFl": 0
        }
    }
])

def get_service_clientRead_body(client_data):
    current_body = data.service_clientRead_body.copy()
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

@allure.suite("(client.read) Запрос информации по клиенту(ам)")
class TestClientCreateSuite:
    @allure.sub_suite("Положительные тесты с различными значениями body")
    @allure.title("Поиск по коду клиента физ лица")
    @pytest.mark.parametrize("client_data", [
        {
            "absCode": [
                "008.119115"
            ],
            "roles": [
                "CLI",
                "AUT"
            ],
            "editingTime": {
                "from": "",
                "to": ""
            },
            "notEditedByAbsCodes": [
                "CRM2"
            ],
            "readingParameters": {
                "archiveFl": 0,
                "jurFl": 0,
                "pboYulFl": 0
            }
        },
    ])
    def test_create_client(self, client_data):
        positive_assert_clientRead_body(client_data)
