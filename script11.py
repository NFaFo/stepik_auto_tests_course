from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time


try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

#code
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    input1 = browser.find_element(By.CSS_SELECTOR, "button.btn")
    input1.click()

    alert = browser.switch_to.alert
    alert.accept()

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    input2 = browser.find_element(By.ID, "answer")
    input2.send_keys(y)

    input3 = browser.find_element(By.CSS_SELECTOR, "button,btn")
    input3.click()
    
finally:
    time.sleep(5)
    browser.quit()
