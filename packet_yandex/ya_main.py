import requests
from dotenv import dotenv_values
from fake_useragent import UserAgent


class MyYandex:

    def __init__(self, ya_token):
        self.url = "https://cloud-api.yandex.net/v1/disk/resources"
        self.ya_token = ya_token

    def common_headers(self):
        user_agent = UserAgent()
        headers = {
            "Authorization": f"OAuth {self.ya_token}",
            "Content-Type": "application/json",
            "User-Agent": user_agent.random
        }
        return headers

    def common_params(self, name_folder):
        params = {
            "path": name_folder
        }
        return params

    def make_folder(self, name_folder):
        return (requests.put(self.url,
                            headers=self.common_headers(),
                            params=self.common_params(name_folder))
                .status_code)

    def check_folder(self, name_folder):
        return (requests.get(self.url,
                            headers=self.common_headers(),
                            params=self.common_params(name_folder))
                .status_code)


if __name__ == "__main__":
    name_folder = "new_folder"
    ya_token = dotenv_values().get("YANDEX_TOKEN")

    person = MyYandex(ya_token)
    print(person.make_folder(name_folder)) # 201
    print(person.check_folder(name_folder)) # 200






