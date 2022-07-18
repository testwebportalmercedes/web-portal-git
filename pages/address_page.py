from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
import pytest
from selenium.webdriver.chrome.service import Service
import configparser
from selenium.webdriver.common.by import By
import time

class EditAdress():

    def __init__(self, browser, url, timeout=15):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)



    def scroll_to_editing_adress(self):
        iframe = self.browser.find_element(By.CSS_SELECTOR, '#upmc-cont')
        self.browser.switch_to.frame(iframe)
        move_to_editing_adress = self.browser.find_element(By.CSS_SELECTOR, "upmc-address > upmc-card > div > div > h4 > owm-svg > span > svg")
        self.browser.execute_script("arguments[0].scrollIntoView();", move_to_editing_adress)



    def go_to_editing_adress(self):
        time.sleep(2)


    # self.browser.find_element(By.CSS_SELECTOR, "h4 > owm-svg > span > svg").click()
        button = WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "upmc-address > upmc-card > div > div > h4 > owm-svg > span > svg")))
        time.sleep(2)
        button.click()


    def editing_street(self):
        self.browser.find_element(By.CSS_SELECTOR, '#upmc-STREET').clear()
        time.sleep(2)
        street = self.browser.find_element(By.CSS_SELECTOR, '#upmc-STREET')
        street.send_keys("Питерская")

    def scroll_to_house(self):
        move_to_house = self.browser.find_element(By.CSS_SELECTOR, "#upmc-HOUSE_NUMBER")
        self.browser.execute_script("arguments[0].scrollIntoView();", move_to_house)

    def editing_house(self):
        self.browser.find_element(By.CSS_SELECTOR, '#upmc-HOUSE_NUMBER').clear()
        time.sleep(2)
        street = self.browser.find_element(By.CSS_SELECTOR, '#upmc-HOUSE_NUMBER')
        street.send_keys("1к1")

    def editing_post_index(self):
        self.browser.find_element(By.CSS_SELECTOR, '#upmc-ZIP_CODE').clear()
        time.sleep(2)
        street = self.browser.find_element(By.CSS_SELECTOR, '#upmc-ZIP_CODE')
        street.send_keys("777777")

    def editing_town(self):
        self.browser.find_element(By.CSS_SELECTOR, '#upmc-CITY > div.selectize-input').click()

        street = self.browser.find_element(By.XPATH, '//*[@id="upmc-CITY"]/div[2]/div/div/div[45]/div')
        street.click()




    def subject(self):
        self.browser.find_element(By.XPATH, '//*[@id="upmc-PROVINCE"]/div[1]').click()

        street = self.browser.find_element(By.XPATH, '//*[@id="upmc-PROVINCE"]/div[2]/div/div/div[38]/div')
        street.click()


    def editing_District(self):
        self.browser.find_element(By.CSS_SELECTOR, '#upmc-ADDITIONAL_ADDRESS_LINE_1').clear()
        time.sleep(2)
        street = self.browser.find_element(By.CSS_SELECTOR, '#upmc-ADDITIONAL_ADDRESS_LINE_1')
        street.send_keys("Бородино")

    def save_button_and_click_after_edit_adress(self):
        button = self.browser.find_element(By.XPATH, "//form/div[2]/button[2]")
        self.browser.execute_script("arguments[0].click();", button)

    def scroll_to_editing_adress_after_saving_change(self):
        move_to_editing_adress = self.browser.find_element(By.XPATH, "//span[text()='Адрес']")
        self.browser.execute_script("arguments[0].scrollIntoView();", move_to_editing_adress)

    def should_be_change_adress(self):
        street = self.browser.find_element(By.XPATH, "//dl/div[2]/dd").text

        assert street == "Питерская", (
            "The street has not changed to Питерская")

        house = self.browser.find_element(By.XPATH, "//dl/div[3]/dd").text

        assert house == "1к1", (
            "The house has not changed to 1к1")


        post_inex = self.browser.find_element(By.XPATH, "//dl/div[4]/dd").text

        assert post_inex == "777777", (
            "The post_inex has not changed to 777777")

        sity = self.browser.find_element(By.XPATH, "//dl/div[5]/dd").text

        assert sity == "Артём", (
            "The sity has not changed to Артём")


        subject = self.browser.find_element(By.XPATH, "//dl/div[6]/dd").text

        assert subject == "Ленинградская область", (
            "The subject has not changed to Ленинградская область")
 


        district = self.browser.find_element(By.XPATH, "//dl/div[7]/dd").text

        assert district == "Бородино", (
            "The district has not changed to Бородино")

