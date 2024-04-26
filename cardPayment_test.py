import json
import pytest
import esb_request
import data
import allure


def check_payment_response_fields(response_json):
    expected_fields = ["ResponseCode", "ResponseMessage", "TransIdent"]
    for field in response_json:
        assert field in expected_fields, f"Обнаружено лишнее поле '{field}' в ответе"
    for field in expected_fields:
        assert field in response_json, f"Поле '{field}' отсутствует в ответе"


def get_cardPayment_body(accNumber):
    current_body = data.cardPayment_body.copy()
    current_body["accNumber"] = accNumber
    return current_body


def positive_assert_accNumber(accNumber):
    cardPayment_body = get_cardPayment_body(accNumber)
    payment_response = esb_request.service_post_cardPayment(cardPayment_body)
    with allure.step("Проверка отправленного запроса"):
        allure.attach("Request", json.dumps(get_cardPayment_body(accNumber)), allure.attachment_type.JSON)
    check_payment_response_fields(payment_response.json())
    with allure.step("Проверка тела ответа"):
        allure.attach("Response", str(payment_response.text), allure.attachment_type.TEXT)
    with allure.step("Проверка статуса ответа"):
        assert payment_response.status_code == 200
    with allure.step("Проверка сообщения об успехе в ответе"):
        assert payment_response.json()["ResponseMessage"] == "Successfully completed"


def negative_assert_accNumber(accNumber):
    cardPayment_body = get_cardPayment_body(accNumber)
    response = esb_request.service_post_cardPayment(cardPayment_body)
    with allure.step("Проверка сообщения об ошибке и кода ответа"):
        assert response.status_code == 200
        assert response.json()["ResponseCode"] != '0'


# processing
def get_cardPayment_body_processing(processing):
    current_body = data.cardPayment_body.copy()
    current_body["processing"] = processing
    return current_body


def positive_assert_processing(processing):
    cardPayment_body = get_cardPayment_body_processing(processing)
    payment_response = esb_request.service_post_cardPayment(cardPayment_body)
    with allure.step("Проверка отправленного запроса"):
        allure.attach("Request", json.dumps(get_cardPayment_body_processing(processing)), allure.attachment_type.JSON)
    check_payment_response_fields(payment_response.json())
    with allure.step("Проверка тела ответа"):
        allure.attach("Response", str(payment_response.text), allure.attachment_type.TEXT)
    with allure.step("Проверка статуса ответа"):
        assert payment_response.status_code == 200
    with allure.step("Проверка сообщения об успехе в ответе"):
        assert payment_response.json()["ResponseMessage"] == "Successfully completed"


def negative_assert_processing(processing):
    cardPayment_body = get_cardPayment_body_processing(processing)
    response = esb_request.service_post_cardPayment(cardPayment_body)
    with allure.step("Проверка сообщения об ошибке и кода ответа"):
        assert response.status_code == 200
        assert response.json()["ResponseCode"] != '0'


@allure.suite("Пополнение карт (cardPaymentService)")
class TestAccNumberPayment:

    @allure.sub_suite("Тесты по номеру счета")
    @allure.title("Тест негативного ввода номера счета")
    @allure.description("Проверка обработки запросов с негативным вводом номера счета")
    @pytest.mark.parametrize("accNumber", ["", "125082000688638", "12508200068863822"])
    def test_negative_accNumber(self, accNumber):
        negative_assert_accNumber(accNumber)

    @allure.sub_suite("Тесты по номеру счета")
    @allure.title("Тест позитивного ввода номера счета")
    @allure.description("Проверка обработки запросов с позитивным вводом номера счета")
    @pytest.mark.parametrize("accNumber", ["1250820006886382"])
    def test_positive_accNumber(self, accNumber):
        positive_assert_accNumber(accNumber)


@allure.suite("Пополнение карт (cardPaymentService)")
class TestProcessingPayment:

    @allure.sub_suite("Тесты по процессингу")
    @allure.title("Тест негативного ввода процессинга")
    @allure.description("Проверка обработки запросов с негативным вводом процессинга")
    @pytest.mark.parametrize("processing", ["OW", "123", "OW123", "", "OW@", "OW 123", "OW44"])
    def test_negative_processing(self, processing):
        negative_assert_processing(processing)

    @allure.sub_suite("Тесты по процессингу")
    @allure.title("Тест позитивного ввода процессинга")
    @allure.description("Проверка обработки запросов с позитивным вводом процессинга")
    @pytest.mark.parametrize("processing", ["OW4"])
    def test_positive_processing(self, processing):
        positive_assert_processing(processing)
