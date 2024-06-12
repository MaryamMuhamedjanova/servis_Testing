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
                    "dep_id": {"type": "integer"},
                    "id": {"type": "integer"},
                    "absCode": {"type": "string"},
                    "docDate": {"type": "string"}
                },
                "required": [
                    "dep_id", "id", "absCode", "docDate"
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
        "department": "125008",
        "code": "8000",
        "description": "Автомат, электропакет, новая резина",
        "ensurId": 1,
        "location": "г. Бишкек",
        "cost": 300000,
        "costCurrency": "KGS",
        "marketCost": 300000,
        "marketCostCurrency": "KGS",
        "docCount": 11,
        "registrationCountry": "KG",
        "contractRegDate": "21.08.2021",
        "contractRegNum": "456122",
        "contractRegOrg": "ГАИ",
        "counterpartyAbsCode": "008.069991",
        "assessDocInfo": "№8989",
        "assessDocDate": "05.04.2022",
        "appraisAbsCode": "",
        "vehicleRegSign": "A1277BB",
        "vehicleVIN": "996557069797",
        "vehicleMark": "BMW E34",
        "vehicleType": "Седан",
        "vehicleCategory": "B",
        "vehicleEngineNum": "M50B25TU",
        "vehicleChassisNum": "RAM456789",
        "vehicleBodyNum": "BOD456789",
        "vehiclePasspSeries": "AR",
        "vehiclePasspNum": "897327",
        "vehiclePasspDate": "02.12.05",
        "vehiclePasspIssuer": "Горгаи",
        "vehicleReleaseYear": "1993",
        "vehicleColor": "cosmosschwarz metallic",
        "vehicleEngineOutput": 192,
        "vehicleEngDisplacement": 2494,
        "vehiclePTSSeries": "AN",
        "vehiclePTSNum": "327897",
        "vehiclePTSDate": "02.12.20",
        "vehiclePTSIssuer": "Республиканская ГАИ ",
        "vehicleProdType": "2",
        "mortgageHolder": [
            {
                "mortOwnerAbsCode": "008.103879",
                "mortOwnershipCode": "1",
                "mortgageDocuments": [
                    {
                        "mortOwnershipDocType": "1",
                        "mortOwnershipDocNum": "№19999",
                        "mortOwnershipDocDate": "03.01.2022"
                    }
                ]
            }
        ]
    }
])

def get_service_mortgageCreate_body(client_data):
    current_body = data.service_mortgageCreate_body.copy()
    current_body["id"] = str(uuid.uuid4())
    current_body["body"][0].update(client_data)
    return current_body

def positive_assert_mortgageCreate_body(client_data):
    service_mortgageCreate_body = get_service_mortgageCreate_body(client_data)
    payment_response = esb_request.service_post(service_mortgageCreate_body)
    with allure.step("Проверка отправленного запроса"):
        allure.attach("Request", json.dumps(service_mortgageCreate_body, ensure_ascii=False), allure.attachment_type.JSON)
    with allure.step("Проверка тела ответа"):
        allure.attach("Response", str(payment_response.text), allure.attachment_type.TEXT)
        check_response_with_schema(payment_response.json())
    with allure.step("Проверка статуса ответа"):
        assert payment_response.status_code == 200
    with allure.step("Проверка сообщения об успехе в ответе"):
        assert payment_response.json()["responseMessage"] == "Залог создан"

@allure.suite("(mortgage.create) Сервис по созданию залога")
class TestClientCreateSuite:
    @allure.sub_suite("Положительные тесты с различными значениями body")
    @allure.title("Создание залога (Авто)")
    @pytest.mark.parametrize("client_data", [
        {
            "department": "125008",
            "code": "8000",
            "description": "Автомат, электропакет, новая резина",
            "ensurId": 1,
            "location": "г. Бишкек",
            "cost": 300000,
            "costCurrency": "KGS",
            "marketCost": 300000,
            "marketCostCurrency": "KGS",
            "docCount": 11,
            "registrationCountry": "KG",
            "contractRegDate": "21.08.2021",
            "contractRegNum": "456122",
            "contractRegOrg": "ГАИ",
            "counterpartyAbsCode": "008.069991",
            "assessDocInfo": "№8989",
            "assessDocDate": "05.04.2022",
            "appraisAbsCode": "",
            "vehicleRegSign": "A1277BB",
            "vehicleVIN": "996557069797",
            "vehicleMark": "BMW E34",
            "vehicleType": "Седан",
            "vehicleCategory": "B",
            "vehicleEngineNum": "M50B25TU",
            "vehicleChassisNum": "RAM456789",
            "vehicleBodyNum": "BOD456789",
            "vehiclePasspSeries": "AR",
            "vehiclePasspNum": "897327",
            "vehiclePasspDate": "02.12.05",
            "vehiclePasspIssuer": "Горгаи",
            "vehicleReleaseYear": "1993",
            "vehicleColor": "cosmosschwarz metallic",
            "vehicleEngineOutput": 192,
            "vehicleEngDisplacement": 2494,
            "vehiclePTSSeries": "AN",
            "vehiclePTSNum": "327897",
            "vehiclePTSDate": "02.12.20",
            "vehiclePTSIssuer": "Республиканская ГАИ ",
            "vehicleProdType": "2",
            "mortgageHolder": [
                {
                    "mortOwnerAbsCode": "008.103879",
                    "mortOwnershipCode": "1",
                    "mortgageDocuments": [
                        {
                            "mortOwnershipDocType": "1",
                            "mortOwnershipDocNum": "№19999",
                            "mortOwnershipDocDate": "03.01.2022"
                        }
                    ]
                }
            ]
        },
    ])
    def test_create_client(self, client_data):
        positive_assert_mortgageCreate_body(client_data)
