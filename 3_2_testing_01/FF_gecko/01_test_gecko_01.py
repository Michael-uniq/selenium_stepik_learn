import time
from selenium import webdriver

# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
with webdriver.Firefox() as driver:

    driver.get("https://stepik.org/lesson/25969/step/8")
    time.sleep(15)