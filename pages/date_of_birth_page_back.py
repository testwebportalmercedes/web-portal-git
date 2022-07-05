from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
import pytest
from selenium.webdriver.chrome.service import Service
import configparser
from selenium.webdriver.common.by import By
import time

class DateBirthPageBack():            # вспомогательные методы для работы с драйвером
    def __init__(self, browser, url, timeout=15):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)
        # общая настройка

    def editing_day_back(self):
        self.browser.find_element(By.XPATH, '//select[@autocomplete="bday-day"]').click()
        day = self.browser.find_element(By.XPATH, '//select[@autocomplete="bday-day"]')
        #street = self.browser.find_element(By.XPATH, '//option[@label="10"]')
        day.send_keys("12")


    def editing_month_back(self):
        self.browser.find_element(By.XPATH, '//select[@autocomplete="bday-month"]').click()
        month = self.browser.find_element(By.XPATH, '//select[@autocomplete="bday-month"]')
        #street = self.browser.find_element(By.XPATH, '//option[@label="10"]')
        month.send_keys("12")

    def editing_years_back(self):
        self.browser.find_element(By.XPATH, '//select[@autocomplete="bday-year"]').click()
        years = self.browser.find_element(By.XPATH, '//select[@autocomplete="bday-year"]')
        #street = self.browser.find_element(By.XPATH, '//option[@label="10"]')
        years.send_keys("1990")



    def should_be_change_date_of_birth_back(self):



        time.sleep(2)

        checking_date_back = self.browser.find_element(By.XPATH, '//div/upmc-birthdate/upmc-card/div/div/div/div/upmc-card-content-inactive/div/div/span').text
        print(checking_date_back)


        assert "12.12.1990" == checking_date_back, (
            "The date_of_birth has not changed back")