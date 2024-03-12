import math
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
link = "https://suninjuly.github.io/execute_script.html"
browser.get(link)


def calc(x: str):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    elem1 = browser.find_element(By.ID, 'input_value').text
    answer = browser.find_element(By.CLASS_NAME, "form-control")
    answer.send_keys(calc(elem1))
    print('1')
    sleep(5)
    input_check = browser.find_element(By.CSS_SELECTOR, '[for="robotCheckbox"]')
    input_check.click()
    print('2')
    sleep(5)
    check1 = browser.find_element(By.CLASS_NAME, 'form-check-label')
    check1.click()
    print('3')
    sleep(5)
    # button = browser.find_element(By.TAG_NAME, "button")
    # browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    # button.click()
    # print('4')
finally:
    webdriver.Chrome().quit()
