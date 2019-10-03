from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/registration1.html"
# link = "http://suninjuly.github.io/registration2.html"
browser = webdriver.Chrome()
browser.get(link)
try:
    input1 = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.first")
    input2 = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.second")
    input3 = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.third")

    input1.send_keys("1")
    input2.send_keys("1")
    input3.send_keys("1")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Поздравляем! Вы успешно зарегистировались!" == welcome_text

    browser.quit()
except:
    print('Error')
    browser.quit()
