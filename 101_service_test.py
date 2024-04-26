import allure
import pytest
import json
import data
import esb_request

#проверка карточки клиента
def get_101_body(customerId):
    current_body = data.service_101_body.copy()
    current_body["body"][0]["customerId"] = customerId
#    print(current_body)
    return current_body

def positive_assert_customerId(customerId):
    service_101_body = get_101_body(customerId)
    payment_response = esb_request.service_post(service_101_body)
    #assert payment_response.status_code == 200

    # Добавляем запрос как шаг в отчет Allure
    with allure.step("Проверка отправленного запроса"):
        allure.attach("Request", str(service_101_body), allure.attachment_type.JSON)

    #    # Добавляем ответ сервиса в отчет Allure
#    allure.attach("Response", str(payment_response.text), allure.attachment_type.TEXT)

        # Преобразуем ответ сервиса в объект Python
        response_data = json.loads(payment_response.text)

        # Проверяем наличие всех полей в ответе
        assert "id" in response_data
        assert "version" in response_data
        assert "type" in response_data
        assert "source" in response_data
        assert "responseCode" in response_data
        assert "responseMessage" in response_data
        assert "dateTime" in response_data
        assert "body" in response_data
        assert isinstance(response_data["body"], list)
        assert isinstance(response_data["body"][0], dict)
        assert "accounts" in response_data["body"][0]

        # Добавляем шаг с проверкой тела ответа
#    with allure.step("Проверка ответа"):
#        assert "accounts" in response_data["body"][0]

        # Проверяем содержимое каждого счета в списке счетов клиента
        for account in response_data["body"][0]["accounts"]:
            assert "CardNumber" in account
            assert "cardProductCode" in account
            assert "absAccount" in account
            assert "currency" in account
            assert "balance" in account
            assert "blockedAmount" in account
            assert "availAmount" in account
            assert "status" in account
            assert "statusActual" in account
            assert "holderName" in account
            assert "issueDate" in account
            assert "expireDate" in account
            assert "cardType" in account
            assert "cardId" in account
            assert "processing" in account
            assert "cardFl" in account
            assert "overdraft" in account
            assert "department" in account
            assert "depAccFl" in account
            assert "creAccFl" in account
            assert "ordId" in account
            assert "futureTurnoverKGS" in account
    with allure.step("Проверка тела ответа"):
        allure.attach("Response", str(payment_response.text), allure.attachment_type.TEXT)
    with allure.step("Проверка статуса ответа"):
        assert payment_response.status_code == 200
    with allure.step("Проверка сообщения об успехе в ответе"):
        assert payment_response.json()["responseMessage"] == "Response succesfully recived"


def negative_assert_customerId(customerId):
    service_101_body = get_101_body(customerId)
    response = esb_request.service_post(service_101_body)
    assert response.json()["responseCode"] != '0'

@allure.suite("Получение списка счетов клиента (101 сервис)")
class TestSuite:

    @allure.sub_suite("Позитивные тест-кейсы")
    @pytest.mark.parametrize("customerId", ["008.119115"], ids=["008.119115"])
    @allure.title("поиск по корректному коду клиента: ")
    @allure.description("Этот тест проверяет успешный запрос по коду клиента")
    def test_get_list_account_10_letter_in_customerId_get_success_response(self,customerId):
        positive_assert_customerId(customerId)

#    @allure.sub_suite("Негативные тест-кейсы")
#   def test_get_list_account_has_special_symbol_in_customerId_get_error_response(self):
#        negative_assert_customerId("008.119115%")