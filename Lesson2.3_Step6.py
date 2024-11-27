from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/redirect_accept.html"
browser.get(link)
button = browser.find_element(By.TAG_NAME,'button')
button.click()
name = browser.window_handles[1]
browser.switch_to.window(name)
x = browser.find_element(By.CSS_SELECTOR,"#input_value").text
answer = calc(x)
input = browser.find_element(By.CSS_SELECTOR,'#answer')
input.send_keys(answer)
submit_button = browser.find_element(By.CSS_SELECTOR,'button')
submit_button.click()
time.sleep(5)