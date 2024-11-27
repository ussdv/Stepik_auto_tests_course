from selenium import webdriver
from selenium.webdriver.common.by import By
import time
link  = "https://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)
fist_name  = browser.find_element(By.NAME,'firstname')
fist_name.send_keys('Name')
last_name = browser.find_element(By.NAME,'lastname')
last_name.send_keys("Last")
e_mail = browser.find_element(By.NAME,'email')
e_mail.send_keys('email')
browse_file = browser.find_element(By.NAME,'file')
browse_file.send_keys('d:/file.txt')
button = browser.find_element(By.CSS_SELECTOR,'button')
button.click()
time.sleep(5)
