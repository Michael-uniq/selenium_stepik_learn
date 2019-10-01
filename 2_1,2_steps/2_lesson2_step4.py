from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select
from utils import print_answer


link = "http://suninjuly.github.io/selects1.html"
# link = "http://suninjuly.github.io/selects2.html"
browser = webdriver.Chrome()
browser.get(link)
try:
    sum = 0
    for i in ['num1', 'num2']:
        l = browser.find_element_by_id(i)
        sum += int(l.text)

    s = Select(browser.find_element_by_id('dropdown'))
    s.select_by_visible_text(str(sum))

    # Отправляем заполненную форму
    button = browser.find_element_by_class_name("btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)
    print_answer(browser)
    browser.execute_script("document.title='BMW Rules'; alert('BMW BMW BMW BMW')")
    time.sleep(5)
    alert = browser.switch_to.alert
    alert.accept()
finally:
    browser.close()
    browser.quit()
