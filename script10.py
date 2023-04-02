from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    

#code
    input1 = browser.find_element(By.NAME,"firstname")
    input1.send_keys('kek')

    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys("XYU")

    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys("xyesas@mail.ru")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    input4 = browser.find_element(By.ID, "file")
    input4.send_keys(file_path)
    
    input5 = browser.find_element(By.CSS_SELECTOR, "button.btn")
    input5.click()
    
finally:
    time.sleep(5)
    browser.quit()
