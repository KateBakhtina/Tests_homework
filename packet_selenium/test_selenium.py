import pytest
from packet_selenium.selenium_main import YaAuthorization
from dotenv import dotenv_values

@pytest.mark.parametrize(
    "password,my_email", [
        (dotenv_values().get("PASSWORD"), dotenv_values().get("email")),
    ]
)
def test_ya_authorization(password, my_email):

    person = YaAuthorization(password, my_email)
    person.open_page()
    person.select_mail()
    person.enter_login()
    person.enter_continue()
    assert person.check_enter_login_one() == "successfully", "Некорректный логин"
