from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import time

link = "http://suninjuly.github.io/selects1.html"
o = Options()
o.add_experimental_option("detach", True)
browser = webdriver.Chrome(options=o)
browser.get(link)
num1 = browser.find_element(By.CSS_SELECTOR,"#num1")
num1_value = int(num1.text)
num2 = browser.find_element(By.CSS_SELECTOR,"#num2")
num2_value = int(num2.text)
sum1 = num1_value+num2_value
select = Select(browser.find_element(By.CSS_SELECTOR,"#dropdown" ))
select.select_by_visible_text(str(sum1))
submit_button = browser.find_element(By.CSS_SELECTOR,"button")
submit_button.click()
time.sleep(5)