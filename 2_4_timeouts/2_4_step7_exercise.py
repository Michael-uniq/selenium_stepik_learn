import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils import print_answer, calc


browser = webdriver.Chrome()
get_el = browser.find_element
try:
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    # проверять в течение 12 до цены 100$
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '$100')
    )
    button = get_el(value='book')
    button.click()

    x_element = get_el(value='input_value')
    x = x_element.text
    get_el(value="answer").send_keys(calc(x))
    button = get_el(value="solve")
    button.click()

    # ждем загрузки страницы
    time.sleep(1)
    print_answer(browser)
finally:
    browser.quit()
