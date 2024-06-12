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
                    "principalAbsCode": {"type": "string"},
                    "dep_id": {"type": "integer"},
                    "id": {"type": "integer"},
                    "absCode": {"type": "string"},
                    "name": {"type": "string"},
                    "nord": {"type": "integer"},
                    "roleConstant": {"type": "string"},
                    "roleName": {"type": "string"},
                    "postConstant": {"type": "string"},
                    "postName": {"type": "string"},
                    "signFl": {"type": ["null", "string"]},
                    "state": {"type": "string"},
                    "documentTypeConstant": {"type": "string"},
                    "documentTypeName": {"type": "string"},
                    "documentNumber": {"type": "string"},
                    "notary": {"type": "string"},
                    "registrationPlace": {"type": "string"},
                    "dateFrom": {"type": "string"},
                    "dateTo": {"type": "string"},
                    "editingTime": {"type": "string"},
                    "editor": {"type": "string"},
                    "arcFl": {"type": "integer"},
                    "arestFl": {"type": "integer"},
                    "accounts": {
                        "type": "array",
                        "items": {"type": "object"}
                    }
                },
                "required": [
                    "principalAbsCode", "dep_id", "id", "absCode", "name", "nord", "roleConstant", "roleName",
                    "postConstant", "postName", "signFl", "state", "documentTypeConstant", "documentTypeName",
                    "documentNumber", "notary", "registrationPlace", "dateFrom", "dateTo", "editingTime", "editor",
                    "arcFl", "arestFl", "accounts"
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
        "principalAbsCode": [
            "002.034314"
        ],
        "absCode": [
            "002.034323"
        ],
        "editingTime": {
            "from": "",
            "to": ""
        }
    }
])

def get_service_authorizedPersonRead_body(client_data):
    current_body = data.service_authorizedPersonRead_body.copy()
    current_body["id"] = str(uuid.uuid4())
    current_body["body"][0].update(client_data)
    return current_body

def positive_assert_authorizedPersonRead_body(client_data):
    service_authorizedPersonRead_body = get_service_authorizedPersonRead_body(client_data)
    payment_response = esb_request.service_post(service_authorizedPersonRead_body)
    with allure.step("Проверка отправленного запроса"):
        allure.attach("Request", json.dumps(service_authorizedPersonRead_body, ensure_ascii=False), allure.attachment_type.JSON)
    with allure.step("Проверка тела ответа"):
        allure.attach("Response", str(payment_response.text), allure.attachment_type.TEXT)
        check_response_with_schema(payment_response.json())
    with allure.step("Проверка статуса ответа"):
        assert payment_response.status_code == 200
    with allure.step("Проверка сообщения об успехе в ответе"):
        assert payment_response.json()["responseMessage"] == "Успех"

@allure.suite("(authorizedPerson.read) Чтение информации по доверенным лицам")
class TestClientCreateSuite:
    @allure.sub_suite("Положительные тесты с различными значениями body")
    @allure.title("Поиск по ")
    @pytest.mark.parametrize("client_data", [
        {
            "principalAbsCode": [
                "002.034314"
            ],
            "absCode": [
                "002.034323"
            ],
            "editingTime": {
                "from": "",
                "to": ""
            }
        },
    ])
    def test_create_client(self, client_data):
        positive_assert_authorizedPersonRead_body(client_data)
