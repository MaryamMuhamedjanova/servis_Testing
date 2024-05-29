import uuid
import pytest
import allure
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

# Функция для проверки полей в объекте accountDebit
def check_accountDebit_fields(accountDebit):
    expected_fields = [
        "department", "number", "currency", "name", "inn", "cardFl", "processing"
    ]
    for field in expected_fields:
        assert field in accountDebit, f"Поле '{field}' отсутствует в accountDebit"

def decode_russian_text(text):
    return text.encode('utf-8').decode('unicode_escape')

# Функция для формирования тела запроса с учетом accountDebit и accountCredit
def service_001_body1(accountDebit, accountCredit, currency):
    current_body = data.service_001_body.copy()
    current_body["id"] = str(uuid.uuid4())
    current_body["body"][0]["accountDebit"] = accountDebit
    current_body["body"][0]["accountCredit"] = accountCredit
    current_body["body"][0]["currency"] = currency

    return current_body

def positive_assert_amount_with_accountDebit_and_accountCredit(accountDebit, accountCredit, currency):
    service_001_amount_body = service_001_body1(accountDebit, accountCredit, currency)
    payment_response = esb_request.service_post(service_001_amount_body)
   # Добавляем запрос как шаг в отчет Allure
    with allure.step("Проверка отправленного запроса"):
        # Декодируем русский текст для accountDebit
        decoded_accountDebit = {key: decode_russian_text(value) if isinstance(value, str) else value for key, value
                                in accountDebit.items()}
        # Декодируем русский текст для accountCredit
        decoded_accountCredit = {key: decode_russian_text(value) if isinstance(value, str) else value for key, value
                                 in accountCredit.items()}
        # Преобразуем словари в JSON с декодированными данными
        decoded_body = {
            "body": [{
                "accountDebit": decoded_accountDebit,
                "accountCredit": decoded_accountCredit,
                **service_001_amount_body["body"][0]
            }]
        }
        allure.attach("Request", json.dumps(decoded_body, ensure_ascii=False), allure.attachment_type.JSON)

    # Проверяем ответ
    with allure.step("Проверка тела ответа"):
        allure.attach("Response", str(payment_response.text), allure.attachment_type.TEXT)
        # Проверка ответа с использованием JSON Schema
        check_response_with_schema(payment_response.json())
        # Проверка наличия полей в ответе для accountDebit
    #    check_accountDebit_fields(accountDebit)
    # Проверка статуса ответа
    with allure.step("Проверка статуса ответа"):
        assert payment_response.status_code == 200
    # Проверка сообщения об успехе в ответе
    with allure.step("Проверка сообщения об успехе в ответе"):
        assert payment_response.json()["responseMessage"] == "Платеж успешно создан"
    # Проверка поля currency
    with allure.step("Проверка поля currency"):
        assert service_001_amount_body["body"][0]["currency"] == currency, "Currency mismatch in request body"

# Класс с тестами
@allure.suite("(001 сервис) Перевод между счетами клиента(-ов)")
class TestAmountSuite:
    @allure.sub_suite("Тесты с различными значениями для счета дебета(accountDebit) и счета кредита(accountCredit)")
    @allure.title("Перевод между счетами в одном подразделении (KGS->KGS)")
    @pytest.mark.parametrize("accountDebit, accountCredit, currency", [
        (
            {
                "department": "125008",
                "number": "1250820004787445",
                "currency": "KGS",
                "name": "Мухамеджанова Марьям Ахмаджановна",
                "inn": "12006200000711",
                "cardFl": 0,
                "processing": "COLVIR"
            },
            {
                "department": "125008",
                "number": "1250820006718250",
                "currency": "KGS",
                "name": "Дубов Александр Вадимович",
                "inn": "22708199600981",
                "cardFl": 0,
                "processing": "COLVIR"
            },
            "KGS"
        )
    ], ids=["1"])
    def test_specific_accountDebit_and_accountCredit(self, accountDebit, accountCredit, currency):
        positive_assert_amount_with_accountDebit_and_accountCredit(accountDebit, accountCredit, currency)

    # Параметризованный тест: Перевод между счетами в одном подразделении (KGS->USD)
    @allure.sub_suite("Тесты с различными значениями для счета дебета (accountDebit) и счета кредита (accountCredit)")
    @allure.title("Перевод между счетами в одном подразделении (KGS->USD)")
    @pytest.mark.parametrize("accountDebit, accountCredit, currency", [
        (
            {
                "department": "125008",
                "number": "1250820006718250",
                "currency": "KGS",
                "name": "Дубов Александр Вадимович",
                "inn": "22708199600981",
                "cardFl": 0,
                "processing": "COLVIR"
            },
            {
                "department": "125008",
                "number": "1250820101177557",
                "currency": "USD",
                "name": "Дубов Александр Вадимович ИП тест",
                "inn": "22708199600981",
                "cardFl": 0,
                "processing": "COLVIR"
            },
            "KGS"
        )
    ], ids=["2"])
    def test_specific_accountDebit_and_accountCredit_USD(self, accountDebit, accountCredit, currency):
        positive_assert_amount_with_accountDebit_and_accountCredit(accountDebit, accountCredit, currency)

    # Параметризованный тест: Перевод между счетами в разных подразделениях (KGS->KGS)
    @allure.sub_suite("Тесты с различными значениями для счета дебета (accountDebit) и счета кредита (accountCredit)")
    @allure.title("Перевод между счетами в разных подразделениях (KGS->KGS)")
    @pytest.mark.parametrize("accountDebit, accountCredit, currency", [
        (
            {
                "department": "125008",
                "number": "1250820006718250",
                "currency": "KGS",
                "name": "Дубов Александр Вадимович",
                "inn": "22708199600981",
                "cardFl": 0,
                "processing": "COLVIR"
            },
            {
                "department": "125002",
                "number": "1250220000188322",
                "currency": "KGS",
                "name": "Рахимов Кучкарбай Ражапбайович",
                "inn": "21709196700070",
                "cardFl": 0,
                "processing": "COLVIR"
            },
            "KGS"
        )
    ], ids=["3"])
    def test_specific_accountDebit_and_accountCredit2(self, accountDebit, accountCredit, currency):
        positive_assert_amount_with_accountDebit_and_accountCredit(accountDebit, accountCredit, currency)
