from selenium import webdriver
import time
from utils import print_answer, calc
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(link)
try:
    btn = browser.find_element_by_class_name('trollface')
    btn.click()
    new_win = browser.window_handles[1]
    browser.switch_to.window(new_win)

    x_el = browser.find_element(By.ID, 'input_value')
    x = x_el.text
    browser.find_element_by_id("answer").send_keys(calc(x))
    button = browser.find_element_by_class_name("btn")
    button.click()
    time.sleep(1)
    print_answer(browser)
finally:
    browser.quit()