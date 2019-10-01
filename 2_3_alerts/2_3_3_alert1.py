from selenium import webdriver
import time
from utils import print_answer, calc
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
browser.get(link)
try:
    btn = browser.find_element_by_class_name('btn')
    btn.click()
    print_answer(browser)
    x_el = browser.find_element(By.ID, 'input_value')
    x = x_el.text
    # Ваш код, который заполняет обязательные поля
    browser.find_element_by_id("answer").send_keys(calc(x))

    # Отправляем заполненную форму
    button = browser.find_element_by_class_name("btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)
    print_answer(browser)
finally:
    browser.quit()
