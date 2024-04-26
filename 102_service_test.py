import allure
import pytest
import data
import esb_request

# проверка номера счета/карты
def get_102_body(identifier):
    current_body = data.service_102_body.copy()
    current_body["body"][0]["identifier"] = identifier
    print(current_body)
    return current_body

def positive_assert_identifier(identifier):
    service_102_body = get_102_body(identifier)
    payment_response = esb_request.service_post(service_102_body)
    with allure.step("Проверка отправленного запроса"):
        allure.attach("Request", str(service_102_body), allure.attachment_type.JSON)
    with allure.step("Проверка тела ответа"):
        allure.attach("Response", str(payment_response.text), allure.attachment_type.TEXT)

        response_json = payment_response.json()
        expected_fields = ["fromJournal", "version", "type", "id", "dateTime", "source",
                           "restartAllowed", "responseCode", "responseMessage", "body"]
        for field in expected_fields:
            assert field in response_json, f"Поле '{field}' отсутствует в ответе"
        extra_fields = set(response_json.keys()) - set(expected_fields)
        assert not extra_fields, f"Обнаружены лишние поля в ответе: {extra_fields}"

        # Проверка содержимого полей внутри "body"
        assert "body" in response_json and isinstance(response_json["body"], list), \
            "Поле 'body' отсутствует в ответе или не является списком"
        body = response_json["body"][0]  # Первый элемент списка "body"
        body_fields = ["responseCode", "responseMessage", "identifierType", "identifierStatus",
                       "account", "cards", "balance", "client"]
        for field in body_fields:
            assert field in body, f"Поле '{field}' в 'body' отсутствует в ответе"
        # Проверка содержимого полей внутри "account"
        account = body["account"]
        account_fields = ["department", "number", "currency", "psAccount", "processing",
                          "currentFl", "depositFl", "cardFl", "activeFl", "allowedDebitFl",
                          "allowedCreditFl", "deaBop", "defaultFl"]
        for field in account_fields:
            assert field in account, f"Поле '{field}' в 'account' отсутствует в ответе"
        # Проверка содержимого полей внутри "cards"
        cards = body["cards"]
        assert isinstance(cards, list), "Поле 'cards' не является списком"
        # Проверка содержимого полей внутри "balance"
        balance = body["balance"]
        balance_fields = ["balance", "avaibleAmount", "blockedAmount", "allowedDebitFl",
                          "allowedCreditFl", "minCreditAmount"]
        for field in balance_fields:
            assert field in balance, f"Поле '{field}' в 'balance' отсутствует в ответе"
        # Проверка содержимого полей внутри "client"
        client = body["client"]
        client_fields = ["code", "name", "maskedName", "inn", "pboyulFl", "jurFl", "residFl",
                         "departmentFl", "unlimitedCreditFl", "blackListFl", "birthDate",
                         "surname", "onlyName", "fatherName", "latinSurname", "latinName",
                         "latinFatherName", "country", "passportSeries", "passportNum",
                         "passportIssuer", "passportIssueDate", "address", "addressReg",
                         "nationality"]
        for field in client_fields:
            assert field in client, f"Поле '{field}' в 'client' отсутствует в ответе"


    with allure.step("Проверка статуса ответа"):
        assert payment_response.status_code == 200
    with allure.step("Проверка сообщения в ответе"):
        assert payment_response.json()["responseMessage"] == "Счёт найден"
    allure.attach("Request", str(service_102_body))  # Attach request to Allure report

def negative_assert_identifier(identifier):
    service_102_body = get_102_body(identifier)
    response = esb_request.service_post(service_102_body)
    with allure.step("Проверка сообщения об ошибке и кода ответа"):
        assert response.json()["responseCode"] != '0'
    # allure.attach("Request", str(service_102_body))  # Attach request to Allure report

@allure.suite("Получение информации по номеру счета/карты (102 сервис)")
class TestSuite:

    @allure.sub_suite("Позитивные тест-кейсы")
    @pytest.mark.parametrize("identifier", ["1250820004787445"], ids=["1250820004787445"])
    @allure.title("поиск по корректному счету физ лица: {ids}")
    @allure.description("Этот тест проверяет успешный запрос по доверенному номеру")
    def test_get_info_account_16_letter_in_identifier_get_success_response(self, identifier):
        service_102_body = get_102_body(identifier)
        allure.attach("Request", str(service_102_body))
        positive_assert_identifier(identifier)

    # def test_get_info_account_has_special_symbol_in_identifier_get_error_response():
    #     negative_assert_identifier("1250820004787445%")
    # def test_get_info_account_15_letter_in_identifier_get_success_response(self):
    #     positive_assert_identifier("125082000478744")
