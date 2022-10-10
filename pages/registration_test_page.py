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



class RegisterTest():            # вспомогательные методы для работы с драйвером
    def __init__(self, browser, url, timeout=15):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)


    def enter_information_for_register(self):
        time.sleep(1)
        email_register = self.browser.find_element(By.CSS_SELECTOR, "#username")
        email_register.send_keys("testwebportalmercedes+3@gmail.com")

        name_register = self.browser.find_element(By.CSS_SELECTOR, "#firstname")
        name_register.send_keys("Тест")

        surename_register = self.browser.find_element(By.CSS_SELECTOR, "#lastname")
        surename_register.send_keys("Тестович")

        move_to_surename_register = self.browser.find_element(By.CSS_SELECTOR, '#lastname')

        self.browser.execute_script("arguments[0].scrollIntoView();", move_to_surename_register)

        self.browser.find_element(By.ID, "56-button").click()
        self.browser.find_element(By.ID, "56-option-de").click()

        self.browser.find_element(By.ID, "59-button").click()
        self.browser.find_element(By.ID, "59-option-RU").click()

        password_register = self.browser.find_element(By.CSS_SELECTOR, "#password")
        password_register.send_keys("1234Ntcn$$")

        self.browser.find_element(By.ID, "legaltext0").click()
        self.browser.find_element(By.ID, "legaltext1").click()

        self.browser.find_element(By.ID, "continue").click()

    def enter_email_password_google(self):
        email_register = self.browser.find_element(By.CSS_SELECTOR, "#identifierId")
        email_register.send_keys("testwebportalmercedes@gmail.com")

        self.browser.find_element(By.XPATH, '//*[@id="identifierNext"]/div/button/span').click()
        self.browser.implicitly_wait(60)
        password_register = self.browser.find_element(By.XPATH, '//input[@autocomplete="current-password"]')
        password_register.send_keys("1234Ntcn$")
        time.sleep(2)
        self.browser.find_element(By.XPATH, '//*[@id="passwordNext"]/div/button/span').click()




    def enter_tat_cod_and_click(self):
        self.browser.find_element(By.XPATH, '//*[@id="confirm"]').click()

    def click_no_car(self):
        self.browser.find_element(By.CSS_SELECTOR, '#aem--userWithoutCarBtnLightbox').click()

    def move_to_delete_account_and_click_new(self):
        time.sleep(4)
        cookie_popup_1 = self.browser.find_element(By.CSS_SELECTOR, "mmu-settings-wrapper")
        # Shadow content trick
        cookie_form = self.browser.execute_script("return arguments[0].shadowRoot", cookie_popup_1)
        time.sleep(5)
        move_to_del_button = cookie_form.find_element(By.CLASS_NAME, 'wb-margin-bottom-xxs.wb-type-copy-tertiary')
        self.browser.execute_script("arguments[0].scrollIntoView();", move_to_del_button)
        time.sleep(4)

        delit = self.browser.find_element(By.CSS_SELECTOR, "mmu-settings-wrapper")
        delit_button = self.browser.execute_script("return arguments[0].shadowRoot", delit)
        button = delit_button.find_element(By.CLASS_NAME, 'wb-link.wb-link--standalone.delete-link')
        button.click()

        time.sleep(2)

        password = self.browser.find_element(By.CSS_SELECTOR, '#password')
        password .send_keys("1234Ntcn$$")
        self.browser.find_element(By.CSS_SELECTOR, '#saveChange').click()


    def move_to_delete_account_and_click(self):

        iframe = self.browser.find_element(By.CSS_SELECTOR, '#upmc-cont')
        self.browser.switch_to.frame(iframe)

        move_to_del_button = self.browser.find_element(By.XPATH, '//span[text()="Удалить учетную запись"]')
        self.browser.execute_script("arguments[0].scrollIntoView();", move_to_del_button)
        time.sleep(2)
        button = self.browser.find_element(By.CSS_SELECTOR, "body > div.upmc > upmc > upmc-connect > div > div > upmc-app > div > div:nth-child(3) > div > div:nth-child(2) > div > upmc-delete-account > upmc-card > div > div > div > div > upmc-card-content-inactive > a > span")
        self.browser.execute_script("arguments[0].click();", button)
        time.sleep(2)

        password = self.browser.find_element(By.CSS_SELECTOR, '#password')
        password .send_keys("1234Ntcn$$")
        self.browser.find_element(By.CSS_SELECTOR, '#saveChange').click()

    def test_for_test(self):

        time.sleep(1)
        cookie_popup = self.browser.find_element(By.CSS_SELECTOR, "cmm-cookie-banner")

        cookie_form = self.browser.execute_script("return arguments[0].shadowRoot", cookie_popup)
        accept_all = cookie_form.find_element(By.CSS_SELECTOR, "button.wb-button--accept-all")
        accept_all.click()


        profile_wrapper = self.browser.find_element(By.CSS_SELECTOR, "owc-header")
        profile_form = self.browser.execute_script("return arguments[0].shadowRoot", profile_wrapper)

        profile_image = profile_form.find_element(By.CSS_SELECTOR, "div.owc-header__item-profile")

        profile_image.click()
        time.sleep(1)



        login_button_wrapper = WebDriverWait(self.browser, 5).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "iam-login-button")))
        login_button_wrapper.click()



        email_field = self.browser.find_element(By.CSS_SELECTOR, "#username")
        email_field.send_keys("testwebportalmercedes@gmail+3.com")
        submit_button = self.browser.find_element(By.CSS_SELECTOR, "#continue")
        submit_button.click()
        time.sleep(2)
        enter_with_password_button = self.browser.find_element(By.CSS_SELECTOR, "#login-with-password")
        enter_with_password_button.click()

        input_pass_field = self.browser.find_element(By.CSS_SELECTOR, "#password")
        input_pass_field.send_keys("1234Ntcn$$")
        confirm_button = self.browser.find_element(By.CSS_SELECTOR, "#confirm")
        confirm_button.click()
        time.sleep(7)

        personal_menu_second = WebDriverWait(self.browser, 5).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/header/nav/div[2]/div/div/div/ul[1]/li[2]")))
        personal_menu_second.click()

    def test_for_test1(self):

        time.sleep(2)

        iframe = self.browser.find_element(By.CSS_SELECTOR, '#upmc-cont')
        self.browser.switch_to.frame(iframe)

        move_to_del_button = self.browser.find_element(By.XPATH, '//span[text()="Удалить учетную запись"]')
        self.browser.execute_script("arguments[0].scrollIntoView();", move_to_del_button)
        time.sleep(2)
        button = self.browser.find_element(By.CSS_SELECTOR,
                                           "body > div.upmc > upmc > upmc-connect > div > div > upmc-app > div > div:nth-child(3) > div > div:nth-child(2) > div > upmc-delete-account > upmc-card > div > div > div > div > upmc-card-content-inactive > a > span")
        self.browser.execute_script("arguments[0].click();", button)
        time.sleep(2)

        password = self.browser.find_element(By.CSS_SELECTOR, '#password')
        password .send_keys("1234Ntcn$$")
        self.browser.find_element(By.CSS_SELECTOR, '#saveChange').click()