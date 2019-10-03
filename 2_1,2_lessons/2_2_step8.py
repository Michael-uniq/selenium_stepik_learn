from selenium import webdriver
import time
import os
from utils import print_answer

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)
try:
    css = ['firstname', 'lastname', 'email']
    key = ['Name', 'Family', 'example@mail.ru']
    for i in range(3):
        browser.find_element_by_name(css[i]).send_keys(key[i])

    fp = os.path.abspath(os.path.dirname(''))
    file = os.path.join(fp, 'file.txt')

    browser.find_element_by_name('file').send_keys(file)

    # Отправляем заполненную форму
    button = browser.find_element_by_class_name("btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)
    print_answer(browser)
finally:
    browser.quit()
