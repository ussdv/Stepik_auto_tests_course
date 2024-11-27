import math
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.implicitly_wait(5)
link = "http://suninjuly.github.io/explicit_wait2.html"
browser.get(link)
button = browser.find_element(By.CSS_SELECTOR,'#book')
WebDriverWait(browser,5).until(EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, '#price'), '100'))
button.click()
x = browser.find_element(By.CSS_SELECTOR,"#input_value").text
answer = calc(x)
input = browser.find_element(By.CSS_SELECTOR,'#answer')
input.send_keys(answer)
submit_button = browser.find_element(By.CSS_SELECTOR,'#solve')
submit_button.click()
time.sleep(5)
