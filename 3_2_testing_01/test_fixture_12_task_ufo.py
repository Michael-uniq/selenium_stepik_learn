import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


@pytest.fixture(scope='module')
def browser():
    print("\nstart browser for test..")
    dr = webdriver.Chrome()
    yield dr
    print("\nquit browser..")
    dr.quit()


def answer():
    return str(math.log(int(time.time())))

urls = [
    'https://stepik.org/lesson/236895/step/1',
    'https://stepik.org/lesson/236896/step/1',
    'https://stepik.org/lesson/236897/step/1',
    'https://stepik.org/lesson/236898/step/1',
    'https://stepik.org/lesson/236899/step/1',
    'https://stepik.org/lesson/236903/step/1',
    'https://stepik.org/lesson/236904/step/1',
    'https://stepik.org/lesson/236905/step/1',
]


@pytest.mark.parametrize("urls", urls)
def test_correct_or_message(browser: webdriver.Chrome, urls):
    browser.get(urls)
    browser.implicitly_wait(10)
    browser.find_element(By.CLASS_NAME, "textarea").send_keys(answer())
    browser.find_element(By.CLASS_NAME, "submit-submission").click()
    feedback = browser.find_element(By.CLASS_NAME, "smart-hints__hint").text
    assert feedback == 'Correct!', f'Feedback is not "Correct!", real={feedback}'
