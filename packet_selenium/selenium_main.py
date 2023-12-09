import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import dotenv_values

class YaAuthorization:

    def __init__(self, password, my_email):
        self.url = "https://passport.yandex.ru/auth/"
        self.browser = webdriver.Chrome()
        self.password = password
        self.my_email = my_email

    def open_page(self):
        self.browser.get(self.url)
        time.sleep(3)
        return "successfully"

    def select_mail(self):
        email_click = self.browser.find_element(By.CLASS_NAME, "AuthLoginInputToggle-type") \
            .find_element(By.CSS_SELECTOR, "[data-type='login']")
        email_click.click()
        time.sleep(3)
        return "successfully"

    def enter_login(self):
        login_input = self.browser.find_element(By.ID, "passp-field-login")
        login_input.send_keys(self.my_email)
        time.sleep(3)
        return "successfully"

    def enter_continue(self):
        enter_click = self.browser.find_element(By.ID, "passp:sign-in")
        enter_click.click()
        time.sleep(5)
        return "successfully"

    def enter_password(self):
        password = self.browser.find_element(By.ID, "passp-field-passwd")
        password.send_keys(self.password)
        time.sleep(3)
        return "successfully"


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







