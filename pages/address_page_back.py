from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
import pytest
from selenium.webdriver.chrome.service import Service
import configparser
from selenium.webdriver.common.by import By
import time

class EditAdressBack():

    def __init__(self, browser, url, timeout=15):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def go_to_editing_adress_after_changes_and_checks(self):
        time.sleep(2)

        # self.browser.find_element(By.CSS_SELECTOR, "h4 > owm-svg > span > svg").click()
        button = WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable
            ((By.CSS_SELECTOR, "upmc-address > upmc-card > div > div > h4 > owm-svg > span > svg")))
        time.sleep(2)
        button.click()



    def editing_street_back(self):
        self.browser.find_element(By.CSS_SELECTOR, '#upmc-STREET').clear()
        time.sleep(2)
        street = self.browser.find_element(By.CSS_SELECTOR, '#upmc-STREET')
        street.send_keys("Ленинградский проспект")

    #def scroll_to_house(self):
        #move_to_house = self.browser.find_element(By.CSS_SELECTOR, "#upmc-HOUSE_NUMBER")
        #self.browser.execute_script("arguments[0].scrollIntoView();", move_to_house)

    def editing_house_back(self):
        self.browser.find_element(By.CSS_SELECTOR, '#upmc-HOUSE_NUMBER').clear()
        time.sleep(2)
        street = self.browser.find_element(By.CSS_SELECTOR, '#upmc-HOUSE_NUMBER')
        street.send_keys("39А")

    def editing_post_index_back(self):
        self.browser.find_element(By.CSS_SELECTOR, '#upmc-ZIP_CODE').clear()
        time.sleep(2)
        street = self.browser.find_element(By.CSS_SELECTOR, '#upmc-ZIP_CODE')
        street.send_keys("123456")

    def editing_town_back(self):
        self.browser.find_element(By.CSS_SELECTOR, '#upmc-CITY > div.selectize-input').click()
        editing_town = self.browser.find_element(By.XPATH, '//*[@id="upmc-CITY"]/div[1]/input')
        editing_town.send_keys("Москва")
        street = self.browser.find_element(By.XPATH, '//*[@id="upmc-CITY"]/div[2]/div/div/div[2]/div')
        street.click()

    def subject_back(self):
        self.browser.find_element(By.XPATH, '//*[@id="upmc-PROVINCE"]/div[1]').click()

        street = self.browser.find_element(By.XPATH, '//*[@id="upmc-PROVINCE"]/div[2]/div/div/div[43]/div')
        street.click()

    def editing_District_back(self):
        self.browser.find_element(By.CSS_SELECTOR, '#upmc-ADDITIONAL_ADDRESS_LINE_1').clear()
        time.sleep(2)
        street = self.browser.find_element(By.CSS_SELECTOR, '#upmc-ADDITIONAL_ADDRESS_LINE_1')
        street.send_keys("Москва")

    #def save_button_and_click_after_edit_adress(self):
        #button = self.browser.find_element(By.XPATH, "//form/div[2]/button[2]")
        #self.browser.execute_script("arguments[0].click();", button)

    #def scroll_to_editing_adress_after_saving_change(self):
        #move_to_editing_adress = self.browser.find_element(By.XPATH, "//span[text()='Адрес']")
        #self.browser.execute_script("arguments[0].scrollIntoView();", move_to_editing_adress)

    def should_be_change_adress_back(self):
        street = self.browser.find_element(By.XPATH, "//dl/div[2]/dd").text

        assert street == "Ленинградский проспект", (
            "The street has not changed back to Ленинградский проспект")

        house = self.browser.find_element(By.XPATH, "//dl/div[3]/dd").text

        assert house == "39А", (
            "The house has not changed back to 39А")

        post_index = self.browser.find_element(By.XPATH, "//dl/div[4]/dd").text

        assert post_index == "123456", (
            "The post_index has not changed back to 123456")

        sity = self.browser.find_element(By.XPATH, "//dl/div[5]/dd").text

        assert sity == "Москва", (
            "The sity has not changed back to Москва")

        subject = self.browser.find_element(By.XPATH, "//dl/div[6]/dd").text

        assert subject == "Москва", (
            "The subject has not changed back to Москва")

        district = self.browser.find_element(By.XPATH, "//dl/div[7]/dd").text

        assert district == "Москва", (
            "The district has not changed back to Москва")

