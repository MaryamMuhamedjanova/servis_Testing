import allure
import pytest
import data
import esb_request

# проверка номера счета/карты
def get_102_body(identifier):
    current_body = data.service_102_body.copy()
    current_body["body"][0]["identifier"] = identifier
    return current_body


def positive_assert_identifier(identifier):
    service_102_body = get_102_body(identifier)
    payment_response = esb_request.service_post(service_102_body)
    with allure.step("Проверка отправленного запроса"):
        allure.attach("Request", str(service_102_body), allure.attachment_type.JSON)
    with allure.step("Проверка тела ответа"):
        allure.attach("Response", str(payment_response.text), allure.attachment_type.TEXT)
        response_json = payment_response.json()
        # Ожидаемые поля в ответе
        expected_fields = [ "version", "type", "id", "dateTime", "source",
                           "restartAllowed", "responseCode", "responseMessage", "body"]
        # Поля, которые ожидаем в каждом элементе "body"
        body_fields = ["responseCode", "responseMessage", "identifierType", "identifierStatus",
                       "account", "cards", "balance", "client"]
        # Поля, которые ожидаем в каждом элементе "account"
        account_fields = ["department", "number", "currency", "psAccount", "processing",
                          "currentFl", "depositFl", "cardFl", "activeFl", "allowedDebitFl",
                          "allowedCreditFl", "deaBop", "defaultFl"]
        # Поля, которые ожидаем в каждом элементе "balance"
        balance_fields = ["balance", "avaibleAmount", "blockedAmount", "allowedDebitFl",
                          "allowedCreditFl", "minCreditAmount"]
        # Поля, которые ожидаем в каждом элементе "client"
        client_fields = ["code", "name", "maskedName", "inn", "pboyulFl", "jurFl", "residFl",
                         "departmentFl", "unlimitedCreditFl", "blackListFl", "birthDate",
                         "surname", "onlyName", "fatherName", "latinSurname", "latinName",
                         "latinFatherName", "country", "passportSeries", "passportNum",
                         "passportIssuer", "passportIssueDate", "address", "addressReg",
                         "nationality"]
        # Проверяем наличие ожидаемых полей в ответе
        for field in expected_fields:
            assert field in response_json, f"Поле '{field}' отсутствует в ответе"
        # Проверяем наличие лишних полей в ответе
        extra_fields = set(response_json.keys()) - set(expected_fields)
        assert not extra_fields, f"Обнаружены лишние поля в ответе: {extra_fields}"
        # Проверяем наличие "body" в ответе и его тип
        assert "body" in response_json and isinstance(response_json["body"], list), \
            "Поле 'body' отсутствует в ответе или не является списком"
        # Проверяем наличие ожидаемых полей в каждом элементе "body"
        for body_item in response_json["body"]:
            for field in body_fields:
                assert field in body_item, f"Поле '{field}' в 'body' отсутствует в ответе"
            # Проверяем наличие лишних полей в каждом элементе "body"
            extra_body_fields = set(body_item.keys()) - set(body_fields)
            assert not extra_body_fields, f"Обнаружены лишние поля в 'body': {extra_body_fields}"
            # Проверяем наличие "account" в каждом элементе "body"
            assert "account" in body_item, "Поле 'account' отсутствует в ответе"
            # Проверяем наличие ожидаемых полей в каждом элементе "account"
            for field in account_fields:
                assert field in body_item["account"], f"Поле '{field}' в 'account' отсутствует в ответе"
            # Проверяем наличие "cards" в каждом элементе "body"
            assert "cards" in body_item, "Поле 'cards' отсутствует в ответе"
            # Проверяем, что "cards" является списком
            assert isinstance(body_item["cards"], list), "Поле 'cards' не является списком"
            # Проверяем наличие "balance" в каждом элементе "body"
            assert "balance" in body_item, "Поле 'balance' отсутствует в ответе"
            # Проверяем наличие ожидаемых полей в каждом элементе "balance"
            for field in balance_fields:
                assert field in body_item["balance"], f"Поле '{field}' в 'balance' отсутствует в ответе"
            # Проверяем наличие "client" в каждом элементе "body"
            assert "client" in body_item, "Поле 'client' отсутствует в ответе"
            # Проверяем наличие ожидаемых полей в каждом элементе "client"
            for field in client_fields:
                assert field in body_item["client"], f"Поле '{field}' в 'client' отсутствует в ответе"

    # Проверка статуса ответа
    with allure.step("Проверка статуса ответа"):
        assert payment_response.status_code == 200

    # Проверка сообщения в ответе
    with allure.step("Проверка сообщения в ответе"):
        assert payment_response.json()["responseMessage"] == "Счёт найден"


def negative_assert_identifier(identifier):
    service_102_body = get_102_body(identifier)
    response = esb_request.service_post(service_102_body)
    with allure.step("Проверка сообщения об ошибке и кода ответа"):
        assert response.json()["responseCode"] != '0'
    # allure.attach("Request", str(service_102_body))  # Attach request to Allure report

@allure.suite("(102 сервис) Получение информации по номеру счета/карты")
class TestSuite:

    @allure.sub_suite("Позитивные тест-кейсы")
    @pytest.mark.parametrize("identifier", ["1250820004787445"], ids=["1250820004787445"])
    @allure.title("поиск по корректному счету физ лица:")
    @allure.description("Этот тест проверяет успешный запрос по доверенному номеру")
    def test_get_info_account_16_letter_in_identifier_get_success_response(self, identifier):
        service_102_body = get_102_body(identifier)
       # allure.attach("Request", str(service_102_body))
        positive_assert_identifier(identifier)

    # def test_get_info_account_has_special_symbol_in_identifier_get_error_response():
    #     negative_assert_identifier("1250820004787445%")
    # def test_get_info_account_15_letter_in_identifier_get_success_response(self):
    #     positive_assert_identifier("125082000478744")
