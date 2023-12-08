import pytest
from dotenv import dotenv_values
from packet_yandex.ya_main import Yandex

@pytest.mark.parametrize(
    "ya_token,name_folder,expected", [
        (dotenv_values().get("YANDEX_TOKEN"), "new_folder", [200, 201])
    ]
)
def test_make_folder(ya_token, name_folder, expected):
    person = Yandex(ya_token)
    assert person.make_folder(name_folder) in expected
    assert person.check_folder(name_folder) in expected