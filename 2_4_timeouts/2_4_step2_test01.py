import time
from selenium import webdriver

browser = webdriver.Chrome()
browser.implicitly_wait(5)      # говорим WebDriver искать каждый элемент в течение 5 секунд
try:
    browser.get("http://suninjuly.github.io/wait1.html")
    button = browser.find_element_by_id("verify")
    button.click()
    message = browser.find_element_by_id("verify_message")

    time.sleep(1)
    assert "successful" in message.text
    print(message.text)

finally:
    browser.quit()