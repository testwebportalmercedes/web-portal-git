from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
import pytest
from selenium.webdriver.chrome.service import Service
import configparser
from selenium.webdriver.common.by import By
import time
from pages.selectors import CookieBannerLocators
from pages.selectors import LoginPageLocators
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


# url = "https://www.mercedes-benz.ru/"


class AppealPage_Back():  # вспомогательные методы для работы с драйвером
    def __init__(self, browser, url, timeout=15):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)
        # общая настройка

    def go_to_editing_request_after_verification(self):
        button = WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "h4 > owm-svg > span > svg")))
        button.click()

    def editing_request_from_madam_to_mister_back(self):
        button = self.browser.find_element(By.CSS_SELECTOR, '#upmc-SALUTATION-0')
        self.browser.execute_script("arguments[0].click();", button)

    def editing_degree_back(self):
        self.browser.find_element(By.CLASS_NAME, "selectize-input").click()
        street = self.browser.find_element(By.XPATH, '//*[@id="upmc-TITLE"]/div[2]/div/div/div[3]/div')
        street.click()

    def editing_name_back(self):
        self.browser.find_element(By.CSS_SELECTOR, '#upmc-FIRST_NAME').clear()
        time.sleep(2)
        name = self.browser.find_element(By.CSS_SELECTOR, '#upmc-FIRST_NAME')
        name.send_keys("Иван")

    def editing_surname_back(self):
        self.browser.find_element(By.CSS_SELECTOR, '#upmc-LAST_NAME_1').clear()
        time.sleep(2)
        surname = self.browser.find_element(By.CSS_SELECTOR, '#upmc-LAST_NAME_1')
        surname.send_keys("Тестов")

    def move_to_save_button_and_click(self):
        move_to_save_button = self.browser.find_element(By.XPATH, "//form/div[2]/button[2]")
        self.browser.execute_script("arguments[0].scrollIntoView();", move_to_save_button)
        time.sleep(2)
        button = self.browser.find_element(By.XPATH, "//form/div[2]/button[2]")
        self.browser.execute_script("arguments[0].click();", button)

    def should_be_change_name_and_surname_back(self):
        time.sleep(1)
        move_to_appeal = self.browser.find_element(By.CLASS_NAME, "wb-type-heading-l")
        self.browser.execute_script("arguments[0].scrollIntoView();", move_to_appeal)
        time.sleep(2)
        checking_change_back = self.browser.find_element(By.CLASS_NAME, "upmc-user__text").text
        print(checking_change_back)

        assert "Господин Доктор наук Иван Тестов" == checking_change_back, (
            "The status of the request and name has not changed back")
