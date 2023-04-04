from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)


#vash code
    x_element = browser.find_element(By.ID, "num1")
    x = x_element.text
    
    y_element = browser.find_element(By.ID, "num2")
    y = y_element.text

    kek = str(int(x)+int(y))
    
    
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(kek)

    input4 = browser.find_element(By.CSS_SELECTOR, "button.btn")
    input4.click()

finally:
    time.sleep(4)
    browser.quit()
