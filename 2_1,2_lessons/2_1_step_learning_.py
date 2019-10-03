from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

def print_answer(remote: webdriver.Remote):
    alert = remote.switch_to.alert
    print(alert.text.split()[-1])
    alert.accept()

link = "http://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)
try:
    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)
    # Ваш код, который заполняет обязательные поля
    element = browser.find_element_by_class_name("form-control")

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
