import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

path = ChromeDriverManager().install()
driver = webdriver.Chrome(service=Service(path))
base_url = "https://passport.yandex.ru/auth/"

driver.get(base_url)
time.sleep(60)