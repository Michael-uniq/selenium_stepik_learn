from selenium import webdriver
import time
from utils import print_answer, calc

link = "http://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)
try:
    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    # Ваш код, который заполняет обязательные поля
    browser.find_element_by_id("answer").send_keys(calc(x))
    js = "window.scrollBy(0, 100);"
    option1 = browser.find_element_by_css_selector("input#robotcheckbox")
    browser.execute_script(js)
    option1.click()
    option2 = browser.find_element_by_css_selector("#robotsrule")
    browser.execute_script(js)
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
