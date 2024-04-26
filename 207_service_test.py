import allure
import pytest
import json
import data
import esb_request


# Функция для проверки наличия полей в ответе от сервиса
def check_response_fields(response_json):
    # Проверка наличия всех основных полей в ответе
    expected_fields = [
        "id", "version", "type", "source", "responseCode", "responseMessage", "dateTime", "body"
    ]
    for field in expected_fields:
        assert field in response_json, f"Поле '{field}' отсутствует в ответе"

    # Проверка наличия поля "body" и его структуры
    assert "body" in response_json, "Поле 'body' отсутствует в ответе"
    assert isinstance(response_json["body"], list), "Поле 'body' не является списком"
    if response_json["body"]:
        assert isinstance(response_json["body"][0], dict), "Элемент 'body' не является словарем"

        # Проверка наличия поля "clients" в первом элементе "body"
        assert "clients" in response_json["body"][0], "Поле 'clients' отсутствует в первом элементе 'body'"
        assert isinstance(response_json["body"][0]["clients"], list), "Поле 'clients' не является списком"
        if response_json["body"][0]["clients"]:
            assert isinstance(response_json["body"][0]["clients"][0],
                              dict), "Элемент в списке 'clients' не является словарем"
            # Дополнительная проверка наличия необходимых полей в первом клиенте
            expected_client_fields = [
                "code", "ow_code", "el_code", "clicont", "pname1", "pname2", "pname3", "taxCode",
                "passTypeName", "passDate", "passNum", "address", "adressType", "adressDate",
                "proofNum", "plname1", "plname2", "plname3", "birthDate", "adressReg", "flagBlackList",
                "passFin", "resident", "cliType", "department", "clientIdentLevel", "passIssuer",
                "passValidDate", "fullName", "nation", "clientFactDepartment", "insiderFl",
                "insiderRelations", "maritalStatus", "position", "workplace", "citizenshipCode",
                "citizenshipName"
            ]
            for field in expected_client_fields:
                assert field in response_json["body"][0]["clients"][0], f"Поле '{field}' отсутствует в первом клиенте"

            # Проверка отсутствия лишних полей
            unexpected_client_fields = [
                field for field in response_json["body"][0]["clients"][0]
                if field not in expected_client_fields
            ]
            assert not unexpected_client_fields, f"Обнаружены лишние поля в ответе: {unexpected_client_fields}"


# Функция для проверки ответа
# проверка карточки клиента
def get_207_customerId_body(customerId):
    current_body = data.service_207_customerId_body.copy()
    current_body["body"][0]["customerId"] = customerId
    return current_body


def positive_assert_customerId(customerId):
    service_207_customerId_body = get_207_customerId_body(customerId)
    payment_response = esb_request.service_post(service_207_customerId_body)
    with allure.step("Проверка отправленного запроса"):
        allure.attach("Request", json.dumps(get_207_customerId_body(customerId)), allure.attachment_type.JSON)
    # Проверяем ответ
    # Преобразуем ответ сервиса в объект Python

    with allure.step("Проверка тела ответа"):
        allure.attach("Response", str(payment_response.text), allure.attachment_type.TEXT)
        # Проверка наличия полей в ответе
        check_response_fields(payment_response.json())

    with allure.step("Проверка статуса ответа"):
        assert payment_response.status_code == 200
    with allure.step("Проверка сообщения об успехе в ответе"):
        assert payment_response.json()["responseMessage"] == "Found"


def negative_assert_customerId(customerId):
    service_207_body = get_207_customerId_body(customerId)
    response = esb_request.service_post(service_207_body)
    # assert response.status_code == 200
    with allure.step("Проверка сообщения об ошибке и кода ответа"):
        assert response.json()["responseCode"] != '0'
        assert response.json()["responseMessage"] == "Not found"

def get_207_proofNum_body(proofNum):
    current_body = data.service_207_proofNum_body.copy()
    current_body["body"][0]["proofNum"] = proofNum
    return current_body


def positive_assert_proofNum(proofNum):
    service_207_proofNum_body = get_207_proofNum_body(proofNum)
    payment_response = esb_request.service_post(service_207_proofNum_body)
    with allure.step("Проверка отправленного запроса"):
        allure.attach("Request", json.dumps(get_207_proofNum_body(proofNum)), allure.attachment_type.JSON)
    # Проверяем ответ
    # Преобразуем ответ сервиса в объект Python
    with allure.step("Проверка тела ответа"):
        allure.attach("Response", str(payment_response.text), allure.attachment_type.TEXT)
        # Проверка наличия полей в ответе
        check_response_fields(payment_response.json())
    with allure.step("Проверка статуса ответа"):
        assert payment_response.status_code == 200
    with allure.step("Проверка сообщения об успехе в ответе"):
        assert payment_response.json()["responseMessage"] == "Found"


def negative_assert_proofNum(proofNum):
    service_207_body = get_207_proofNum_body(proofNum)
    response = esb_request.service_post(service_207_body)
    # assert response.status_code == 200
    with allure.step("Проверка сообщения об ошибке и кода ответа"):
        assert response.json()["responseCode"] != '0'
        assert response.json()["responseMessage"] == "Not found"

def get_207_inn_body(inn):
    current_body = data.service_207_inn_body.copy()
    current_body["body"][0]["inn"] = inn
    return current_body


def positive_assert_inn(inn):
    service_207_inn_body = get_207_inn_body(inn)
    payment_response = esb_request.service_post(service_207_inn_body)
    with allure.step("Проверка отправленного запроса"):
        allure.attach("Request", json.dumps(get_207_inn_body(inn)), allure.attachment_type.JSON)
    # Проверяем ответ
    # Преобразуем ответ сервиса в объект Python
    with allure.step("Проверка тела ответа"):
        allure.attach("Response", str(payment_response.text), allure.attachment_type.TEXT)
        # Проверка наличия полей в ответе
        check_response_fields(payment_response.json())
    with allure.step("Проверка статуса ответа"):
        assert payment_response.status_code == 200
    with allure.step("Проверка сообщения об успехе в ответе"):
        assert payment_response.json()["responseMessage"] == "Found"


def negative_assert_inn(inn):
    service_207_body = get_207_inn_body(inn)
    response = esb_request.service_post(service_207_body)
    # assert response.status_code == 200
    with allure.step("Проверка сообщения об ошибке и кода ответа"):
        assert response.json()["responseCode"] != '0'
        assert response.json()["responseMessage"] == "Not found"


# Первый класс с тестами по доверенному номеру
@allure.suite("Получение информации по клиенту (207 сервис)")
class TestProofNumSuite:
    @allure.sub_suite("Проверки по доверенному номеру")
    @pytest.mark.parametrize("proofNum", ["996553565311"], ids=["996553565311"])
    @allure.title("Позитивная проверка доверенного номера успешно найденного клиента")
    @allure.description("Проверка успешного поиска клиента по доверенному номеру в формате 12 символов")
    def test_get_info_client_12_letter_fiz_in_proofNum_get_success_response(self, proofNum):
        positive_assert_proofNum(proofNum)

    @allure.sub_suite("Проверки по доверенному номеру")
    @pytest.mark.parametrize("proofNum", ["0553565311"], ids=["0553565311"])
    @allure.title("Негативная проверка доверенного номера не найденного клиента")
    @allure.description("Проверка неудачного поиска клиента по доверенному номеру в формате 10 символов")
    def test_get_info_client_10_letter_fiz_in_proofNum_get_success_response(self, proofNum):
        negative_assert_proofNum(proofNum)

    @allure.sub_suite("Проверки по доверенному номеру")
    @pytest.mark.parametrize("proofNum", [""], ids=[""])
    @allure.title("Негативная проверка пустого доверенного номера")
    @allure.description("Проверка неудачного поиска клиента по пустому доверенному номеру")
    def test_get_info_client_0_letter_in_proofNum_get_error_response(self, proofNum):
        negative_assert_proofNum(proofNum)

    @allure.sub_suite("Проверки по доверенному номеру")
    @pytest.mark.parametrize("proofNum", ["996553565311%"], ids=["996553565311%"])
    @allure.title("Негативная проверка доверенного номера с символом '%'")
    @allure.description("Проверка неудачного поиска клиента по доверенному номеру с символом '%'")
    def test_get_info_client_has_special_symbol_in_proofNum_get_error_response(self, proofNum):
        negative_assert_proofNum(proofNum)

# Второй класс с тестами по коду клиента
@allure.suite("Получение информации по клиенту (207 сервис)")
class TestCustomerIdSuite:
    @allure.sub_suite("Проверки по коду клиента")
    @pytest.mark.parametrize("customerId", [""], ids=[""])
    @allure.title("Негативная проверка пустого кода клиента")
    @allure.description("Проверка неудачного поиска клиента по пустому коду клиента")
    def test_get_info_client_0_letter_in_customerId_get_error_response(self, customerId):
        negative_assert_customerId(customerId)

    @allure.sub_suite("Проверки по коду клиента")
    @pytest.mark.parametrize("customerId", ["008.119115"], ids=["Valid"])
    @allure.title("Позитивная проверка успешно найденного клиента по коду клиента")
    @allure.description("Проверка успешного поиска клиента по коду клиента в формате '008.119115'")
    def test_get_info_client_10_letter_in_customerId_get_success_response(self, customerId):
        positive_assert_customerId(customerId)

    @allure.sub_suite("Проверки по коду клиента")
    @pytest.mark.parametrize("customerId", ["008119115"], ids=["NoDot"])
    @allure.title("Негативная проверка отсутствия точки в коде клиента")
    @allure.description("Проверка неудачного поиска клиента без точки в коде клиента")
    def test_get_info_client_not_dot_in_customerId_get_error_response(self, customerId):
        negative_assert_customerId(customerId)

    @allure.sub_suite("Проверки по коду клиента")
    @pytest.mark.parametrize("customerId", ["008.11911"], ids=["Short"])
    @allure.title("Негативная проверка короткого кода клиента")
    @allure.description("Проверка неудачного поиска клиента по короткому коду клиента в формате '008.11911'")
    def test_get_info_client_9_letter_in_customerId_get_error_response(self, customerId):
        negative_assert_customerId(customerId)

    @allure.sub_suite("Проверки по коду клиента")
    @pytest.mark.parametrize("customerId", ["008.119115%"], ids=["SpecialChar"])
    @allure.title("Негативная проверка кода клиента с символом '%'")
    @allure.description("Проверка неудачного поиска клиента по коду клиента с символом '%'")
    def test_get_info_client_has_special_symbol_in_customerId_get_error_response(self, customerId):
        negative_assert_customerId(customerId)


# Третий класс с тестами по ИНН
@allure.suite("Получение информации по клиенту (207 сервис)")
class TestInnSuite:
    @allure.sub_suite("Проверки по ИНН")
    @pytest.mark.parametrize("inn", [""], ids=[""])
    @allure.title("Негативная проверка пустого ИНН")
    @allure.description("Проверка неудачного поиска клиента по пустому ИНН")
    def test_get_info_client_0_letter_in_inn_get_error_response(self, inn):
        negative_assert_inn(inn)

    @allure.sub_suite("Проверки по ИНН")
    @pytest.mark.parametrize("inn", ["12006200000711"], ids=["ValidFiz"])
    @allure.title("Позитивная проверка успешно найденного клиента по ИНН (физ.лицо)")
    @allure.description("Проверка успешного поиска клиента по ИНН физического лица в формате 14 символов")
    def test_get_info_client_14_letter_fiz_in_inn_get_success_response(self, inn):
        positive_assert_inn(inn)

    @allure.sub_suite("Проверки по ИНН")
    @pytest.mark.parametrize("inn", ["10507198401578"], ids=["ValidIP"])
    @allure.title("Позитивная проверка успешно найденного клиента по ИНН (ИП)")
    @allure.description(
        "Проверка успешного поиска клиента по ИНН индивидуального предпринимателя в формате 14 символов")
    def test_get_info_client_14_letter_IP_in_inn_get_success_response(self, inn):
        positive_assert_inn(inn)

    @allure.sub_suite("Проверки по ИНН")
    @pytest.mark.parametrize("inn", ["120062000007"], ids=["Short12"])
    @allure.title("Негативная проверка короткого ИНН")
    @allure.description("Проверка неудачного поиска клиента по короткому ИНН в формате 12 символов")
    def test_get_info_client_12_letter_in_inn_get_error_response(self, inn):
        negative_assert_inn(inn)

    @allure.sub_suite("Проверки по ИНН")
    @pytest.mark.parametrize("inn", ["1200620000071"], ids=["Short13"])
    @allure.title("Негативная проверка короткого ИНН")
    @allure.description("Проверка неудачного поиска клиента по короткому ИНН в формате 13 символов")
    def test_get_info_client_13_letter_in_inn_get_error_response(self, inn):
        negative_assert_inn(inn)

    @allure.sub_suite("Проверки по ИНН")
    @pytest.mark.parametrize("inn", ["120062000007111"], ids=["Long15"])
    @allure.title("Негативная проверка длинного ИНН")
    @allure.description("Проверка неудачного поиска клиента по длинному ИНН в формате 15 символов")
    def test_get_info_client_15_letter_in_inn_get_error_response(self, inn):
        negative_assert_inn(inn)

    @allure.sub_suite("Проверки по ИНН")
    @pytest.mark.parametrize("inn", ["12006200000711%"], ids=["SpecialChar"])
    @allure.title("Негативная проверка ИНН с символом '%'")
    @allure.description("Проверка неудачного поиска клиента по ИНН с символом '%'")
    def test_get_info_client_has_special_symbol_in_inn_get_error_response(self, inn):
        negative_assert_inn(inn)