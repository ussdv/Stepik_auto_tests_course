from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import time




def reg_form(link):
    browser = webdriver.Chrome()
    browser.get(link)
    first_name = browser.find_element(By.CSS_SELECTOR, "div.first_block > div.form-group.first_class > input")
    first_name.send_keys("first_name")
    last_name = browser.find_element(By.CSS_SELECTOR, "div.first_block > div.form-group.second_class > input")
    last_name.send_keys("last_name")
    e_mail = browser.find_element(By.CSS_SELECTOR, "div.first_block > div.form-group.third_class > input")
    e_mail.send_keys("e_mail")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text
    time.sleep(3)
    return welcome_text

class TestReg(unittest.TestCase):
    def test_reg1(self):
        self.assertEqual(reg_form("http://suninjuly.github.io/registration1.html"),
                         "Congratulations! You have successfully registered!", "registration is failed")

    def test_reg2(self):
        self.assertEqual(reg_form("http://suninjuly.github.io/registration2.html"),
                         "Congratulations! You have successfully registered!", "registration is failed")

if __name__ == "__main__":
    unittest.main()
