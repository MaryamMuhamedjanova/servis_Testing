import allure
import pytest
import json
import data
import esb_request

#проверка карточки клиента
def get_205_body(customerId):
    current_body = data.service_205_body.copy()
    current_body["body"][0]["customerId"] = customerId
#    print(current_body)
    return current_body


def positive_assert_customerId(customerId):
    service_205_body = get_205_body(customerId)
    payment_response = esb_request.service_post(service_205_body)

    # Добавляем запрос как шаг в отчет Allure
    with allure.step("Проверка отправленного запроса"):
        allure.attach("Request", str(service_205_body), allure.attachment_type.JSON)

# Добавляем ответ сервиса в отчет Allure
    with allure.step("Проверка тела ответа"):
        allure.attach("Response", str(payment_response.text), allure.attachment_type.TEXT)

        # Преобразуем ответ сервиса в объект Python
        response_data = json.loads(payment_response.text)

        # Ожидаемые поля в ответе
        expected_fields = {
            "id", "version", "type", "source", "responseCode", "responseMessage", "dateTime", "body"
        }

        # Поля для каждой карточки клиента
        account_fields = {
            "creditId", "depId", "code", "customerId", "contractNum", "beginDate", "title",
            "deaAmount", "currency", "percent", "effectivePercent", "endDate", "currentBalance",
            "accRuedPercent", "percentToPay", "overDueAmount", "totalDue", "amountToPay",
            "paymentMethod", "productType", "colvirProcessId", "customerId2", "iban2", "currency2",
            "alias", "status", "status2", "balance", "blockedBalance", "bankBranch", "productCode",
            "opened", "closed", "lastMove", "customerTaxCode", "deaRestAmount", "prdName",
            "prdNameDM", "regDate", "prdDateForGrafik"
        }

        # Проверка наличия ожидаемых полей в ответе
        missing_fields = expected_fields - set(response_data.keys())
        assert not missing_fields, f"Отсутствуют поля в ответе: {missing_fields}"

        # Проверка наличия всех карточек клиента и их полей
        assert isinstance(response_data["body"], list)
        for acc in response_data["body"][0].get("acc", []):
            missing_account_fields = account_fields - set(acc.keys())
            assert not missing_account_fields, f"Отсутствуют поля в карточке клиента: {missing_account_fields}"
            extra_account_fields = set(acc.keys()) - account_fields
            assert not extra_account_fields, f"Обнаружены лишние поля в карточке клиента: {extra_account_fields}"

        # Проверка наличия лишних полей в "body"
        extra_body_fields = set(response_data["body"][0].keys()) - {"acc"}
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


def negative_assert_customerId(customerId):
    service_205_body = get_205_body(customerId)
    response = esb_request.service_post(service_205_body)
    assert response.json()["responseCode"] != '0'

@allure.suite("Получение списка кредитов (205 сервис)")
class TestSuite:
    @allure.sub_suite("Позитивные тест-кейсы")
    @pytest.mark.parametrize("customerId", ["008.128090"], ids=["008.128090"])
    @allure.title("Поиск по корректному коду клиента: ")
    @allure.description("Этот тест проверяет успешный запрос по коду клиента")
    def test_get_list_account_10_letter_in_customerId_get_success_response(self,customerId):
        positive_assert_customerId(customerId)

#    @allure.sub_suite("Негативные тест-кейсы")
#   def test_get_list_account_has_special_symbol_in_customerId_get_error_response(self):
#        negative_assert_customerId("008.119115%")