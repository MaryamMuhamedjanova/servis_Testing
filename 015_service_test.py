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
                    "responseCode": {"type": "string"},
                    "responseMessage": {"type": "string"},
                    "docNum": {"type": "string"},
                    "debitAmount": {"type": "number"},
                    "debitCurrency": {"type": "string"},
                    "creditAmount": {"type": "number"},
                    "creditCurrency": {"type": "string"},
                    "depId": {"type": "string"},
                    "docId": {"type": "string"},
                    "docDate": {"type": "string"},
                    "operDate": {"type": "string"}
                },
                "required": ["responseCode", "responseMessage", "docNum", "debitAmount",
                             "debitCurrency", "creditAmount", "creditCurrency", "depId",
                             "docId", "docDate", "operDate"]
            }
        }
    },
    "required": ["version", "type", "id", "dateTime", "source", "restartAllowed",
                 "responseCode", "responseMessage", "body"]
}

def check_response_with_schema(response_json):
    jsonschema.validate(instance=response_json, schema=response_schema)

def check_accountDebit_fields(accountDebit):
    expected_fields = [
        "department", "number", "currency", "name", "inn", "cardFl", "processing"
    ]
    for field in expected_fields:
        assert field in accountDebit, f"Поле '{field}' отсутствует в accountDebit"

def decode_russian_text(text):
    return text.encode('utf-8').decode('unicode_escape')

def get_015_body(accountDebit, accountCredit, currency):
    current_body = data.service_015_body.copy()
    current_body["id"] = str(uuid.uuid4())
    current_body["body"][0]["accountDebit"] = accountDebit
    current_body["body"][0]["accountCredit"] = accountCredit
    current_body["body"][0]["currency"] = currency
    return current_body

def positive_assert_amount_with_accountDebit_and_accountCredit(accountDebit, accountCredit,currency):
    service_015_body = get_015_body(accountDebit, accountCredit,currency)
    payment_response = esb_request.service_post(service_015_body)
    with allure.step("Проверка отправленного запроса"):
        decoded_accountDebit = {key: decode_russian_text(value) if isinstance(value, str) else value for key, value in
                                accountDebit.items()}
        decoded_accountCredit = {key: decode_russian_text(value) if isinstance(value, str) else value for key, value in
                                 accountCredit.items()}
        decoded_body = {
            "body": [{
                "accountDebit": decoded_accountDebit,
                "accountCredit": decoded_accountCredit,
                **service_015_body["body"][0]
            }]
        }
        allure.attach("Request", json.dumps(decoded_body, ensure_ascii=False), allure.attachment_type.JSON)

        #allure.attach("Request", json.dumps(service_001_body1(accountDebit, accountCredit)), allure.attachment_type.JSON)
    # Проверяем ответ
    with allure.step("Проверка тела ответа"):
        allure.attach("Response", str(payment_response.text), allure.attachment_type.TEXT)
        # Проверка ответа с использованием JSON Schema
        check_response_with_schema(payment_response.json())
        # Проверка наличия полей в ответе для accountDebit
        check_accountDebit_fields(accountDebit)
        # Проверка наличия полей в ответе для accountCredit
        #check_accountCredit_fields(accountCredit)
    # Проверка статуса ответа
    with allure.step("Проверка статуса ответа"):
        assert payment_response.status_code == 200
    # Проверка сообщения об успехе в ответе
    with allure.step("Проверка сообщения об успехе в ответе"):
        assert payment_response.json()["responseMessage"] == "Платеж успешно создан"


# Класс с тестами
@allure.suite("(015 сервис) Перевод с карты на карту")
class TestAmountSuite:
    # Параметризованный тест
    @allure.sub_suite("Тесты с различными значениями для счета дебета(accountDebit) и счета кредита(accountCredit)")
    @allure.title("Перевод с карты на карту в одном подразделении (KGS->KGS)")
    @pytest.mark.parametrize("accountDebit, accountCredit, currency", [
        (
                {
                    "department": "125008",
                    "number": "1250820004775119",
                    "currency": "KGS",
                    "name": "Мухамеджанова Марьям Ахмаджано",
                    "inn": "12006200000711",
                    "cardFl": 1,
                    "processing": "OW4"
                },
                {
                    "department": "125008",
                    "number": "1250820006886382",
                    "currency": "KGS",
                    "name": "Мухамеджанова Марьям Ахмаджано",
                    "inn": "12006200000711",
                    "cardFl": 1,
                    "processing": "OW4"
                },
            "KGS"
        )
    ])

    def test_specific_accountDebit_and_accountCredit(self, accountDebit, accountCredit,currency):
        positive_assert_amount_with_accountDebit_and_accountCredit(accountDebit, accountCredit,currency)

    # @allure.sub_suite("Тесты с различными значениями для счета дебета(accountDebit) и счета кредита(accountCredit)")
    # @allure.title("Перевод с карты на карту в одном подразделении (KGS->USD)")
    # @pytest.mark.parametrize("accountDebit, accountCredit", [
    #     (
    #             {
    #                 "department": "125008",
    #                 "number": "1250820004775119",
    #                 "currency": "KGS",
    #                 "name": "Мухамеджанова Марьям Ахмаджано",
    #                 "inn": "12006200000711",
    #                 "cardFl": 1,
    #                 "processing": "OW4"
    #             },
    #             {
    #
    #             }
    #     )
    # ])
    #
    # def test_specific_accountDebit_and_accountCredit_USD(self, accountDebit, accountCredit):
    #     positive_assert_amount_with_accountDebit_and_accountCredit(accountDebit, accountCredit)
    #
    # @allure.sub_suite("Тесты с различными значениями для счета дебета(accountDebit) и счета кредита(accountCredit)")
    # @allure.title("Перевод с карты клиента одного подразделения на счет того же клиента в другом подразделении (KGS->KGS)")
    # @pytest.mark.parametrize("accountDebit, accountCredit", [
    #     (
    #             {
    #                 "department": "125008",
    #                 "number": "1250820004775119",
    #                 "currency": "KGS",
    #                 "name": "Мухамеджанова Марьям Ахмаджано",
    #                 "inn": "12006200000711",
    #                 "cardFl": 1,
    #                 "processing": "OW4"
    #             },
    #             {
    #
    #             }
    #     )
    # ])
    # def test_specific_accountDebit_and_accountCredit2(self, accountDebit, accountCredit):
    #     positive_assert_amount_with_accountDebit_and_accountCredit(accountDebit, accountCredit)
    #
    # @allure.sub_suite("Тесты с различными значениями для счета дебета(accountDebit) и счета кредита(accountCredit)")
    # @allure.title("Перевод с карты клиента одного подразделения на счет того же клиента в другом подразделении (KGS->USD)")
    # @pytest.mark.parametrize("accountDebit, accountCredit", [
    #     (
    #             {
    #                 "department": "125008",
    #                 "number": "1250820004775119",
    #                 "currency": "KGS",
    #                 "name": "Мухамеджанова Марьям Ахмаджано",
    #                 "inn": "12006200000711",
    #                 "cardFl": 1,
    #                 "processing": "OW4"
    #             },
    #             {
    #
    #             }
    #     )
    # ])
    # def test_specific_accountDebit_and_accountCredit3(self, accountDebit, accountCredit):
    #     positive_assert_amount_with_accountDebit_and_accountCredit(accountDebit, accountCredit)
    #
    # @allure.sub_suite("Тесты с различными значениями для счета дебета(accountDebit) и счета кредита(accountCredit)")
    # @allure.title("Перевод с карты клиента одного подразделения на счет клиента в другом подразделении (KGS->KGS)")
    # @pytest.mark.parametrize("accountDebit, accountCredit", [
    #     (
    #             {
    #                 "department": "125008",
    #                 "number": "1250820004775119",
    #                 "currency": "KGS",
    #                 "name": "Мухамеджанова Марьям Ахмаджано",
    #                 "inn": "12006200000711",
    #                 "cardFl": 1,
    #                 "processing": "OW4"
    #             },
    #             {
    #
    #             }
    #     )
    # ])
    # def test_specific_accountDebit_and_accountCredit4(self, accountDebit, accountCredit):
    #     positive_assert_amount_with_accountDebit_and_accountCredit(accountDebit, accountCredit)
    #
    # @allure.sub_suite("Тесты с различными значениями для счета дебета(accountDebit) и счета кредита(accountCredit)")
    # @allure.title("Перевод с карты клиента одного подразделения на счет клиента в другом подразделении (KGS->USD)")
    # @pytest.mark.parametrize("accountDebit, accountCredit", [
    #     (
    #             {
    #                 "department": "125008",
    #                 "number": "1250820008709881",
    #                 "currency": "KGS",
    #                 "name": "Дубов А.В. ИП тест Элкарт",
    #                 "inn": "22708199600981",
    #                 "cardFl": 1,
    #                 "processing": "IPC"
    #             },
    #             {
    #
    #             }
    #     )
    # ])
    # def test_specific_accountDebit_and_accountCredit5(self, accountDebit, accountCredit):
    #     positive_assert_amount_with_accountDebit_and_accountCredit(accountDebit, accountCredit)
    #
