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
                    "constval": {"type": "string"},
                    "constcode": {"type": "string"},
                    "shortname": {"type": "string"},
                    "longname": {"type": "string"},
                    "arcfl": {"type": "string"},
                    "prim": {"type": "string"},
                    "txt_add": {"type": "string"}
                },
                "required": ["constval", "constcode", "shortname", "longname", "arcfl", "prim", "txt_add"]
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
        "directoryCode": "G_CLIAUTHPRS_PLACE"
    },
])

def get_service_directoriesUniversal_body(client_data):
    current_body = data.service_directoriesUniversal_body.copy()
    current_body["id"] = str(uuid.uuid4())
    current_body["body"][0].update(client_data)
    return current_body

def positive_assert_directoriesUniversal_body(client_data):
    service_directoriesUniversal_body = get_service_directoriesUniversal_body(client_data)
    payment_response = esb_request.service_post(service_directoriesUniversal_body)
    with allure.step("Проверка отправленного запроса"):
        allure.attach("Request", json.dumps(service_directoriesUniversal_body, ensure_ascii=False), allure.attachment_type.JSON)
    with allure.step("Проверка тела ответа"):
        allure.attach("Response", str(payment_response.text), allure.attachment_type.TEXT)
        check_response_with_schema(payment_response.json())
    with allure.step("Проверка статуса ответа"):
        assert payment_response.status_code == 200
    with allure.step("Проверка сообщения об успехе в ответе"):
        assert payment_response.json()["responseMessage"] == "Успешно"

@allure.suite("(directories.universal) Универсальный справочник по уполномоченным лицам")
class TestClientCreateSuite:
    @allure.sub_suite("Положительные тесты с различными значениями кода справочника")
    @allure.title("Для справочника <Должности>")
    @pytest.mark.parametrize("client_data", [
        {
            "directoryCode": "G_CLIAUTHPRS_PLACE"
        }
    ])
    def test_G_CLIAUTHPRS_PLACE(self, client_data):
        positive_assert_directoriesUniversal_body(client_data)

    @allure.sub_suite("Положительные тесты с различными значениями кода справочника")
    @allure.title("Для справочника <Роли>")
    @pytest.mark.parametrize("client_data", [
        {
            "directoryCode": "G_CLIPRS_NSIGN"
        }
    ])
    def test_G_CLIPRS_NSIGN(self, client_data):
        positive_assert_directoriesUniversal_body(client_data)

    @allure.sub_suite("Положительные тесты с различными значениями кода справочника")
    @allure.title("Для справочника <Семейное положение>")
    @pytest.mark.parametrize("client_data", [
        {
            "directoryCode": "G_CLI_FAM"
        }
    ])
    def test_G_CLI_FAM(self, client_data):
        positive_assert_directoriesUniversal_body(client_data)

    @allure.sub_suite("Положительные тесты с различными значениями кода справочника")
    @allure.title("Для справочника <Тип адреса>")
    @pytest.mark.parametrize("client_data", [
        {
            "directoryCode": "G_CLIADR_TYPE"
        }
    ])
    def test_G_CLIADR_TYPE(self, client_data):
        positive_assert_directoriesUniversal_body(client_data)

    @allure.sub_suite("Положительные тесты с различными значениями кода справочника")
    @allure.title("Для справочника <Тип клиентов для плана счетов>")
    @pytest.mark.parametrize("client_data", [
        {
            "directoryCode": "G_CLITYPE_ACC"
        }
    ])
    def test_G_CLITYPE_ACC(self, client_data):
        positive_assert_directoriesUniversal_body(client_data)

    @allure.sub_suite("Положительные тесты с различными значениями кода справочника")
    @allure.title("Для справочника <Тип телефона клиента>")
    @pytest.mark.parametrize("client_data", [
        {
            "directoryCode": "G_CLIPHONE_TYP"
        }
    ])
    def test_G_CLIPHONE_TYP(self, client_data):
        positive_assert_directoriesUniversal_body(client_data)

    @allure.sub_suite("Положительные тесты с различными значениями кода справочника")
    @allure.title("Для справочника <Тип собственности по адресу>")
    @pytest.mark.parametrize("client_data", [
        {
            "directoryCode": "G_CLIADR_OWNR"
        }
    ])
    def test_G_CLIADR_OWNR(self, client_data):
        positive_assert_directoriesUniversal_body(client_data)

    @allure.sub_suite("Положительные тесты с различными значениями кода справочника")
    @allure.title("Для справочника <Виды обращения к клиенту>")
    @pytest.mark.parametrize("client_data", [
        {
            "directoryCode": "G_CLITITLE_TYP"
        }
    ])
    def test_G_CLITITLE_TYP(self, client_data):
        positive_assert_directoriesUniversal_body(client_data)

    @allure.sub_suite("Положительные тесты с различными значениями кода справочника")
    @allure.title("Для справочника <Тип родственной связи>")
    @pytest.mark.parametrize("client_data", [
        {
            "directoryCode": "G_CLI_FAMILY"
        }
    ])
    def test_G_CLI_FAMILY(self, client_data):
        positive_assert_directoriesUniversal_body(client_data)

    @allure.sub_suite("Положительные тесты с различными значениями кода справочника")
    @allure.title("Для справочника <Подтип подписи клиента>")
    @pytest.mark.parametrize("client_data", [
        {
            "directoryCode": "DMN$36"
        }
    ])
    def testDMN36(self, client_data):
        positive_assert_directoriesUniversal_body(client_data)

    @allure.sub_suite("Положительные тесты с различными значениями кода справочника")
    @allure.title("Для справочника <Подтип подписи клиента> (может включать в себя несколько подтипов подписи)")
    @pytest.mark.parametrize("client_data", [
        {
            "directoryCode": "DMN$35"
        }
    ])
    def testDMN35(self, client_data):
        positive_assert_directoriesUniversal_body(client_data)

    @allure.sub_suite("Положительные тесты с различными значениями кода справочника")
    @allure.title("Для справочника <Канал поступления клиента>")
    @pytest.mark.parametrize("client_data", [
        {
            "directoryCode": "DMN$34"
        }
    ])
    def testDMN34(self, client_data):
        positive_assert_directoriesUniversal_body(client_data)

    @allure.sub_suite("Положительные тесты с различными значениями кода справочника")
    @allure.title("Для справочника Направление/отрасль НБКР>")
    @pytest.mark.parametrize("client_data", [
        {
            "directoryCode": "Z069_INDUSTRY_HBKR"
        }
    ])
    def testZ069_INDUSTRY_HBKR(self, client_data):
        positive_assert_directoriesUniversal_body(client_data)

    @allure.sub_suite("Положительные тесты с различными значениями кода справочника")
    @allure.title("Для справочника <Право собственности>")
    @pytest.mark.parametrize("client_data", [
        {
            "directoryCode": "L_PROP_RIGHT_TYPE"
        }
    ])
    def testL_PROP_RIGHT_TYPE(self, client_data):
        positive_assert_directoriesUniversal_body(client_data)

    @allure.sub_suite("Положительные тесты с различными значениями кода справочника")
    @allure.title("Для справочника <Документы права собственности>")
    @pytest.mark.parametrize("client_data", [
        {
            "directoryCode": "L_PROP_RIGHT_DOC"
        }
    ])
    def testL_PROP_RIGHT_DOC(self, client_data):
        positive_assert_directoriesUniversal_body(client_data)

    @allure.sub_suite("Положительные тесты с различными значениями кода справочника")
    @allure.title("Для справочника <Категория транспортного средства>")
    @pytest.mark.parametrize("client_data", [
        {
            "directoryCode": "M_AUTOCAT"
        }
    ])
    def testM_AUTOCAT(self, client_data):
        positive_assert_directoriesUniversal_body(client_data)

    @allure.sub_suite("Положительные тесты с различными значениями кода справочника")
    @allure.title("Для справочника <Производство транспортного средства>")
    @pytest.mark.parametrize("client_data", [
        {
            "directoryCode": "L_AUTOMADEIN"
        }
    ])
    def testL_AUTOMADEIN(self, client_data):
        positive_assert_directoriesUniversal_body(client_data)