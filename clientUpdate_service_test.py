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
                    "Id": {"type": "integer"},
                    "absCode": {"type": "string"},
                    "docDate": {"type": "string"},
                    "editingTime": {"type": "string"},
                    "addresses": {
                        "type": "array",
                        "items": {"type": "object"}
                    }
                },
                "required": [
                    "depId", "Id", "absCode", "docDate", "editingTime", "addresses"
                ]
            }
        }
    },
    "required": [
        "version", "type", "id", "dateTime", "source", "restartAllowed",
        "responseCode", "responseMessage", "body"
    ]
}




def check_response_with_schema(response_json):
    jsonschema.validate(instance=response_json, schema=response_schema)

def decode_russian_text(text):
    return text.encode('utf-8').decode('unicode_escape')

@pytest.mark.parametrize("client_data", [
    {
        "absCode": "008.119115",
        "surname": "Мухамеджанова"
    }
])

def get_service_clientUpdate_body(client_data):
    current_body = data.service_clientUpdate_body.copy()
    current_body["id"] = str(uuid.uuid4())
    current_body["body"][0].update(client_data)
    return current_body

def positive_assert_service_clientUpdate_body(client_data):
    service_clientUpdate_body = get_service_clientUpdate_body(client_data)
    payment_response = esb_request.service_post(service_clientUpdate_body)
    with allure.step("Проверка отправленного запроса"):
        allure.attach("Request", json.dumps(service_clientUpdate_body, ensure_ascii=False), allure.attachment_type.JSON)
    with allure.step("Проверка тела ответа"):
        allure.attach("Response", str(payment_response.text), allure.attachment_type.TEXT)
        check_response_with_schema(payment_response.json())
    with allure.step("Проверка статуса ответа"):
        assert payment_response.status_code == 200
    with allure.step("Проверка сообщения об успехе в ответе"):
        assert payment_response.json()["responseMessage"] == "Информация обновлена"

@allure.suite("(client.update) Обновление карточки клиента ")
class TestClientCreateSuite:
    @allure.sub_suite("Положительные тесты с различными значениями body")
    @allure.title("Обновление фамилии в картотеке клиента")
    @pytest.mark.parametrize("client_data", [
        {
            "absCode": "008.119115",
            "surname": "Мухамеджанова"
        },
    ])
    def test_create_client(self, client_data):
        positive_assert_service_clientUpdate_body(client_data)
