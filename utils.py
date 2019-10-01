from selenium import webdriver
import math

def print_answer(remote: webdriver.Remote):
    alert = remote.switch_to.alert
    print(alert.text.split()[-1])
    alert.accept()


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
