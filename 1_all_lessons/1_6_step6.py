from selenium import webdriver
from utils import print_answer


browser = webdriver.Chrome()
try:
    browser.get("http://suninjuly.github.io/huge_form.html")
    elements = browser.find_elements_by_css_selector("[type='text']")
    for element in elements:
        element.send_keys("Ans")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    print_answer(browser)
finally:
    browser.quit()