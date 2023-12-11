import pytest
from packet_selenium.selenium_main import YaAuthorization
from dotenv import dotenv_values

incorrect_parameters = {
    "id_incorrect_login": "field:input-login:hint",
    "id_phone_code": "passp-field-phoneCode",
    "id_incorrect_password": "field:input-passwd:hint"
}

@pytest.mark.parametrize(
    "password,my_email,incorrect_parameters", [
        (dotenv_values().get("PASSWORD"),
         dotenv_values().get("email"),
         incorrect_parameters)
    ]
)
def test_ya_authorization(password, my_email, incorrect_parameters):

    person = YaAuthorization(password, my_email)
    person.open_page()
    person.select_mail()
    person.enter_login()
    person.enter_continue()
    assert person.check_enter_continue(incorrect_parameters.get("id_incorrect_login")) == "successfully", "Некорректный логин"
    assert person.check_enter_continue(incorrect_parameters.get("id_phone_code")) == "successfully", "Требуется подтверждение электронной почты"
    person.enter_password()
    person.enter_continue()
    assert person.check_enter_continue(
    incorrect_parameters.get("id_incorrect_password")) == "successfully", "Неверный пароль"
    person.browser_close()

