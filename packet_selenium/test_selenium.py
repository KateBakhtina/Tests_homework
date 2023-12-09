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

    assert person.open_page() == "successfully"
    assert person.select_mail() == "successfully"
    assert person.enter_login() == "successfully"
    assert person.enter_continue() == "successfully"
    assert person.enter_password() == "successfully"
    assert person.enter_continue() == "successfully"

