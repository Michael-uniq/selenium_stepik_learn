import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def answer():
    return str(math.log(int(time.time())))

urls = [
    '236895',
    '236896',
    '236897',
    '236898',
    '236899',
    '236903',
    '236904',
    '236905',
]


@pytest.mark.parametrize("urls", urls)
def test_correct_or_message(browser: webdriver.Chrome, urls):
    browser.get(f'https://stepik.org/lesson/{urls}/step/1')
    browser.implicitly_wait(10)
    browser.find_element(By.CLASS_NAME, "textarea").send_keys(answer())
    browser.find_element(By.CLASS_NAME, "submit-submission").click()
    feedback = browser.find_element(By.CLASS_NAME, "smart-hints__hint").text
    assert feedback == 'Correct!', f'Feedback is not "Correct!", real={feedback}'