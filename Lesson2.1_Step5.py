from selenium import webdriver
from selenium.webdriver.common.by import By
import math
from selenium.webdriver.chrome.options import Options
import time
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "https://suninjuly.github.io/math.html"
o = Options()
o.add_experimental_option("detach", True)
browser = webdriver.Chrome(options=o)
browser.get(link)
x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
x = x_element.text
y = calc(x)
answer = browser.find_element(By.CSS_SELECTOR, "#answer")
answer.send_keys(y)
checkbox = browser.find_element(By.CSS_SELECTOR,"#robotCheckbox")
checkbox.click()
radio_button = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
radio_button.click()
submit_button = browser.find_element(By.CSS_SELECTOR, "button")
submit_button.click()
time.sleep(10)
browser.quit()
