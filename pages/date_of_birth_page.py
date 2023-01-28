from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
import pytest
from selenium.webdriver.chrome.service import Service
import configparser
from selenium.webdriver.common.by import By
import time


class DataBirthPage():  # вспомогательные методы для работы с драйвером
    def __init__(self, browser, url, timeout=15):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)
        # общая настройка

    def go_to_editing_date_of_birth(self):
        time.sleep(2)
        button = WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "upmc-birthdate > upmc-card > div > div > h4 > owm-svg > span > svg")))
        time.sleep(2)
        button.click()

    def editing_day(self):
        self.browser.find_element(By.XPATH, '//select[@autocomplete="bday-day"]').click()
        street = self.browser.find_element(By.XPATH, '//select[@autocomplete="bday-day"]')
        street.send_keys("10")

    def editing_months(self):
        self.browser.find_element(By.XPATH, '//select[@autocomplete="bday-month"]').click()
        street = self.browser.find_element(By.XPATH, '//select[@autocomplete="bday-month"]')
        street.send_keys("10")

    def editing_years(self):
        self.browser.find_element(By.XPATH, '//select[@autocomplete="bday-year"]').click()
        street = self.browser.find_element(By.XPATH, '//select[@autocomplete="bday-year"]')
        street.send_keys("1999")

    def save_button_click(self):
        self.browser.find_element(By.XPATH, '//button[@data-ga-action="modify_date_of_birth"][2]').click()

    def should_be_change_date_of_birth(self):
        time.sleep(2)
        checking_date = self.browser.find_element(By.XPATH,
                                                  '//div/upmc-birthdate').text
        print(checking_date)

        assert "10.10.1999" == checking_date, (
            "The date_of_birth has not changed")
