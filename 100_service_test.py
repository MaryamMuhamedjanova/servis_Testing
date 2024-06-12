import allure
import pytest
import json
import data
import esb_request

#проверка карточки клиента
def get_100_body(clientCode):
    current_body = data.service_100_body.copy()
    current_body["body"][0]["clientCode"] = clientCode
#    print(current_body)
    return current_body

def positive_assert_clientCode(clientCode):
    service_100_body = get_100_body(clientCode)
    payment_response = esb_request.service_post(service_100_body)
    # Добавляем запрос как шаг в отчет Allure
    with allure.step("Проверка отправленного запроса"):
        allure.attach("Request", str(service_100_body), allure.attachment_type.JSON)
    # Добавляем ответ сервиса в отчет Allure
    with allure.step("Проверка тела ответа"):
        allure.attach("Response", str(payment_response.text), allure.attachment_type.TEXT)
    # Преобразуем ответ сервиса в объект Python
    response_data = json.loads(payment_response.text)
    # Ожидаемые поля в ответе
    expected_fields = {
        "id", "version", "type", "source", "responseCode", "responseMessage", "dateTime", "body"
    }
    # Поля для каждого счета клиента
    account_fields = {
        "accountNum", "currency", "isActive", "statDscr", "balance",
        "blockedAmount", "availAmount", "opened", "statDscrId",
        "statDscrNord", "dateLast", "department", "closeDate",
        "chaCode", "processing", "cardFl", "blockedStatus",
        "defaultFL", "depAccFl", "creAccFl", "ordId"
    }
    # Проверка наличия ожидаемых полей в ответе
    missing_fields = expected_fields - set(response_data.keys())
    assert not missing_fields, f"Отсутствуют поля в ответе: {missing_fields}"
    # Проверка наличия всех счетов клиента и их полей
    assert isinstance(response_data["body"], list)
    for account in response_data["body"][0].get("accounts", []):
        missing_account_fields = account_fields - set(account.keys())
        assert not missing_account_fields, f"Отсутствуют поля в карточке клиента: {missing_account_fields}"
        extra_account_fields = set(account.keys()) - account_fields
        assert not extra_account_fields, f"Обнаружены лишние поля в карточке клиента: {extra_account_fields}"
    # Проверка наличия лишних полей в "body"
    extra_body_fields = set(response_data["body"][0].keys()) - {"accounts"}
    assert not extra_body_fields, f"Обнаружены лишние поля в 'body': {extra_body_fields}"
    # Проверка наличия лишних полей в ответе
    extra_fields = set(response_data.keys()) - expected_fields
    assert not extra_fields, f"Обнаружены лишние поля в ответе: {extra_fields}"
    # Проверка статуса ответа
    with allure.step("Проверка статуса ответа"):
        assert payment_response.status_code == 200
    # Проверка сообщения об успехе в ответе
    with allure.step("Проверка сообщения об успехе в ответе"):
        assert response_data["responseMessage"] == "Response succesfully recived"

def negative_assert_clientCode(clientCode):
    service_100_body = get_100_body(clientCode)
    response = esb_request.service_post(service_100_body)
    with allure.step("Проверка сообщения об ошибке и кода ответа"):
        assert response.json()["responseCode"] != '0'

@allure.suite("(100 сервис) Получение списка счетов клиента")
class TestSuite:

    @allure.sub_suite("Позитивные тест-кейсы")
    @pytest.mark.parametrize("clientCode", ["008.119115"], ids=["008.119115"])
    @allure.title("Поиск по корректному коду клиента: ")
    @allure.description("Этот тест проверяет успешный запрос по коду клиента")
    def test_get_list_account_10_letter_in_clientCode_get_success_response(self,clientCode):
        positive_assert_clientCode(clientCode)

#    @allure.sub_suite("Негативные тест-кейсы")
#   def test_get_list_account_has_special_symbol_in_clientCode_get_error_response(self):
#        negative_assert_clientCode("008.119115%")