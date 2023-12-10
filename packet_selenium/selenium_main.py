import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

from dotenv import dotenv_values

# passp-field-phoneCode - id при отправке кода на почту если введен не тот емайл +
# field:input-login:hint - id логина, который не подойдет +
# field:input-passwd:hint - id неверного пароля +

class YaAuthorization:

    def __init__(self, password, my_email):
        self.url = "https://passport.yandex.ru/auth/"
        self.browser = webdriver.Chrome()
        self.password = password
        self.my_email = my_email

    def open_page(self):
        self.browser.get(self.url)
        time.sleep(3)

    def select_mail(self):
        self.browser.find_element(By.CLASS_NAME, "AuthLoginInputToggle-type") \
                    .find_element(By.CSS_SELECTOR, "[data-type='login']")\
                    .click()
        time.sleep(3)

    def enter_login(self):
        self.browser.find_element(By.ID, "passp-field-login").send_keys(self.my_email)
        time.sleep(3)

    def enter_continue(self):
        self.browser.find_element(By.ID, "passp:sign-in").click()
        time.sleep(5)

    def check_enter_continue(self, by_id):
        try:
            self.browser.find_element(By.ID, by_id)
            return "error"
        except NoSuchElementException:
            return "successfully"

    def enter_password(self):
        self.browser.find_element(By.ID, "passp-field-passwd").send_keys(self.password)
        time.sleep(3)

    def browser_close(self):
        self.browser.close()

if __name__ == "__main__":
    password = dotenv_values().get("PASSWORD")
    my_email = dotenv_values().get("email")

    person = YaAuthorization(password, my_email)

    person.open_page()
    person.select_mail()
    person.enter_login()
    person.enter_continue()
    person.enter_password()
    person.enter_continue()







