import unittest
from selenium import webdriver
import time
import pytest


class MyTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\Program Files (x86)\Chromedriver\chromedriver.exe")
        self.driver.maximize_window()

    def test_number_validation(self):
        driver = self.driver
        driver.get('https://bhalogari.com/login')
        numbers = ['0162590337', '01621808744', '+8801621808744', '016218O8744', '0!6@!*)*744']

        for number in numbers:
            driver.find_element_by_xpath('//*[@id="outlined"]').send_keys(number)
            time.sleep(1)
            driver.find_element_by_xpath('//*[@id="root"]/div/section/div/div/form/button').click()
            time.sleep(2)
            curr = driver.current_url
            if curr == 'https://bhalogari.com/login':
                print(number, ' is an invalid number')
            else:
                print(number, ' is a valid number')
            driver.get('https://bhalogari.com/login')

    def test_email_validation(self):
        driver = self.driver
        driver.get('https://bhalogari.com/login')
        emails = ['mashfiq@bhalogari.com', 'faiyaz.trd@gmail.com', 'h.nahin94@gmail.com', '016218O8744', '0!6@!*)*744']

        for email in emails:
            driver.find_element_by_xpath('//*[@id="outlined"]').send_keys(email)
            time.sleep(1)
            driver.find_element_by_xpath('//*[@id="root"]/div/section/div/div/form/button').click()
            time.sleep(2)
            curr = driver.current_url
            if curr == 'https://bhalogari.com/login':
                print(email, ' is an invalid email')
            else:
                print(email, ' is a valid email')
            driver.get('https://bhalogari.com/login')

    def test_password_validation(self):
        driver = self.driver
        driver.get('https://bhalogari.com/login')
        driver.find_element_by_xpath('//*[@id="outlined"]').send_keys('01621808744')
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="root"]/div/section/div/div/form/button').click()
        time.sleep(2)
        passwords = ['mashfiq@bhalogari.com', 'faiyaz.trd@gmail.com', 'h.nahin94@gmail.com', '016218O8744',
                  '123456']

        for password in passwords:
            driver.find_element_by_xpath('//*[@id="outlined-number"]').clear()
            driver.find_element_by_xpath('//*[@id="outlined-number"]').send_keys(password)
            time.sleep(1)
            driver.find_element_by_xpath('//*[@id="root"]/div/section/div/div/form/button').click()
            time.sleep(2)
            curr = driver.current_url
            if curr == 'https://bhalogari.com/password':
                print(password, ' is an invalid password')
            else:
                print(password, ' is a valid password')

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
