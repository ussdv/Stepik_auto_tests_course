from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.chrome.options import Options

import math
import time

link = "https://suninjuly.github.io/execute_script.html"
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

#o = Options()
#o.add_experimental_option("detach", True)
browser = webdriver.Chrome() #options=o
browser.get(link)

x_element = browser.find_element(By.CSS_SELECTOR,"#input_value")
x = x_element.text
y = calc(x)

input_answer = browser.find_element(By.CSS_SELECTOR, "#answer")
input_answer.send_keys(y)
browser.execute_script("window.scrollBy(0,150);")
checkbox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
checkbox.click()
radiobutton = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
radiobutton.click()
button =  browser.find_element(By.CSS_SELECTOR, "button")
button.click()
time.sleep(5)
#browser.quit()