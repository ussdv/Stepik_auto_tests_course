from selenium import webdriver
from selenium.webdriver.common.by import By
import math
from selenium.webdriver.chrome.options import Options
import time
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"
o = Options()
o.add_experimental_option("detach", True)
browser = webdriver.Chrome(options=o)
browser.get(link)
sunduk = browser.find_element(By.CSS_SELECTOR, "#treasure")
x=sunduk.get_attribute("valuex")
y = calc(x)
answer = browser.find_element(By.CSS_SELECTOR, "#answer")
answer.send_keys(y)
checkbox = browser.find_element(By.CSS_SELECTOR,"#robotCheckbox")
checkbox.click()
radio_button = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
radio_button.click()
submit_button = browser.find_element(By.CSS_SELECTOR, "button")
submit_button.click()
time.sleep(5)
browser.quit()
