from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time



try:

    link = "http://172.31.130.86:8005/"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.CSS_SELECTOR, '[class="Button_typeDefault__+lJxs"]:nth-child(2)')
    input1.click()

finally:
    time.sleep(3)
    browser.quit()
