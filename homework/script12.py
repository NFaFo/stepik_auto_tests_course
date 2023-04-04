from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time


try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

#code
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    input1 = browser.find_element(By.CSS_SELECTOR, "button.btn")
    input1.click()
    browser.switch_to.window(browser.window_handles[1])
    
    
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)
    input4 = browser.find_element(By.CSS_SELECTOR, "button.btn")
    input4.click()

finally:
    time.sleep(5)
    browser.quit()
