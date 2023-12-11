import pytest
from dotenv import dotenv_values
from packet_yandex.ya_main import MyYandex

@pytest.mark.parametrize(
    "ya_token,name_folder,expected", [
        (dotenv_values().get("YANDEX_TOKEN"), "new_folder", [200, 201])
    ]
)
def test_my_yandex(ya_token, name_folder, expected):
    person = MyYandex(ya_token)
    assert person.make_folder(name_folder) in expected, "Папка уже существует"
    assert person.check_folder(name_folder) in expected, "Такой папки не существует"