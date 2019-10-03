from selenium import webdriver
import time
from utils import print_answer, calc


link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)
try:
    x_element = browser.find_element_by_id('treasure')
    x = x_element.get_attribute('valuex')
    y = calc(x)
    # Ваш код, который заполняет обязательные поля
    element = browser.find_element_by_id("answer")

    element.send_keys(y)

    option1 = browser.find_element_by_css_selector("input#robotcheckbox")
    option1.click()
    option2 = browser.find_element_by_css_selector("#robotsrule")
    option2.click()

    # Отправляем заполненную форму
    button = browser.find_element_by_class_name("btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)
    print_answer(browser)

finally:
    browser.quit()
