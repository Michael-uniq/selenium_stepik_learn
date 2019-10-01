import time

from selenium import webdriver

browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)
try:
    button = browser.find_element_by_tag_name("button")
    browser.execute_script("arguments[1].scrollIntoView(true);", 'k',button)
    time.sleep(2)
    button.click()
    # assert True
finally:
    browser.close()
    browser.quit()