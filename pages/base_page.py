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
url = "https://www.mercedes-benz.ru/"


class BasePage():            # вспомогательные методы для работы с драйвером
    def __init__(self, browser, url, timeout=15):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

        # общая настройка


    def open(self):
        self.browser.get(self.url)



    #def cookie_acceptance(self):
        #cookie_popup = self.browser.find_element(*CookieBannerLocators.Cookie_Banner)
        # Shadow content trick
        #cookie_form = self.browser.execute_script("return arguments[0].shadowRoot", cookie_popup)
        #accept_all = cookie_form.find_element(*CookieBannerLocators.Cookie_Accept_All)
        #accept_all.click()

    def cookie_acceptance(self):
        time.sleep(3)
        cookie_popup = self.browser.find_element(By.CSS_SELECTOR, "cmm-cookie-banner")
        # Shadow content trick
        cookie_form = self.browser.execute_script("return arguments[0].shadowRoot", cookie_popup)
        accept_all = cookie_form.find_element(By.CSS_SELECTOR, "button.wb-button--accept-all")
        accept_all.click()




    def go_to_profile_wrapper(self):
        profile_wrapper = self.browser.find_element(By.CSS_SELECTOR, "owc-header")
        profile_form = self.browser.execute_script("return arguments[0].shadowRoot", profile_wrapper)

        profile_image = profile_form.find_element(By.CSS_SELECTOR, "div.owc-header__item-profile")

        profile_image.click()
        time.sleep(1)


    def go_to_logon_with_email(self):

        login_button_wrapper = WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "iam-login-button")))
        login_button_wrapper.click()

        #login_button_wrapper = self.browser.find_element(By.CSS_SELECTOR, "iam-login-button")
        #login_button_wrapper.click()

        email_field = self.browser.find_element(By.CSS_SELECTOR, "#username")
        email_field.send_keys("mbcee.test+2@gmail.com")
        submit_button = self.browser.find_element(By.CSS_SELECTOR, "#continue")
        submit_button.click()
        time.sleep(2)
        enter_with_password_button = self.browser.find_element(By.CSS_SELECTOR, "#login-with-password")
        enter_with_password_button.click()

        input_pass_field = self.browser.find_element(By.CSS_SELECTOR, "#password")
        input_pass_field.send_keys("Ntcn1234$")
        confirm_button = self.browser.find_element(By.CSS_SELECTOR, "#confirm")
        confirm_button.click()
        time.sleep(4)

    def should_be_message_about_login(self):
        top_menu = self.browser.find_element(By.CSS_SELECTOR, "owc-header")
        top_menu_shadow = self.browser.execute_script("return arguments[0].shadowRoot", top_menu)
        welcome_text = top_menu_shadow.find_element(By.CSS_SELECTOR, "div.owc-header-mme__headline").text

        assert welcome_text in "Здравствуйте", (
            "Product name does not match the message")

    def go_to_my_data(self):
        time.sleep(3)
        personal_menu_first = self.browser.find_element(By.CSS_SELECTOR, "owc-header")
        profile_form = self.browser.execute_script("return arguments[0].shadowRoot", personal_menu_first)

        personal_menu = profile_form.find_element(By.LINK_TEXT, "Мой профиль")
        personal_menu.click()

    def go_to_my_setting(self):
        personal_menu_first = self.browser.find_element(By.CSS_SELECTOR, "owc-header")
        profile_form = self.browser.execute_script("return arguments[0].shadowRoot", personal_menu_first)

        personal_menu = profile_form.find_element(By.LINK_TEXT, "Мой профиль")
        personal_menu.click()



    def go_to_profile_wrapper_after_my_data(self):

        time.sleep(5)

        personal_menu_second = WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/header/nav/div[2]/div/div/div/ul[1]/li[2]")))
        personal_menu_second.click()

    def go_to_my_mercedes_me(self):
        personal_menu_second = self.browser.find_element(By.XPATH, "/html/body/header/nav/div[2]/nav/div[2]/div[3]/div[4]/ul/li[1]/a")
        personal_menu_second.click()

    def go_to_my_mercedes_me_my_data(self):
        personal_menu_second = self.browser.find_element(By.XPATH, "/html/body/header/nav/div[2]/nav/div[3]/div[2]/div/div[1]/div[3]/div[4]/ul/li[2]/a")
        personal_menu_second.click()



    def go_to_editing_request(self):
        time.sleep(2)


        iframe = self.browser.find_element(By.CSS_SELECTOR, '#upmc-cont')
        self.browser.switch_to.frame(iframe)

        button = WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "h4 > owm-svg > span > svg")))
        time.sleep(2)
        button.click()




    def editing_request_from_mister_to_madam(self):
        button = self.browser.find_element(By.CSS_SELECTOR, '#upmc-SALUTATION-1')

        self.browser.execute_script("arguments[0].click();", button)

    def scroll_to_name_and_surename(self):
        move_to_editing_name_and_surename = self.browser.find_element(By.XPATH, '//label[text()="Уч. звание, степень"]')

        self.browser.execute_script("arguments[0].scrollIntoView();", move_to_editing_name_and_surename)

    def editing_degree(self):
        self.browser.find_element(By.CLASS_NAME, "selectize-input").click()
        street = self.browser.find_element(By.XPATH, '//*[@id="upmc-TITLE"]/div[2]/div/div/div[4]/div')
        street.click()

    def editing_name(self):
        self.browser.find_element(By.CSS_SELECTOR, '#upmc-FIRST_NAME').clear()
        time.sleep(2)
        street = self.browser.find_element(By.CSS_SELECTOR, '#upmc-FIRST_NAME')
        street.send_keys("Дарья")

    def editing_surname(self):
        self.browser.find_element(By.CSS_SELECTOR, '#upmc-LAST_NAME_1').clear()
        time.sleep(2)
        street = self.browser.find_element(By.CSS_SELECTOR, '#upmc-LAST_NAME_1')
        street.send_keys("Тестович")


    def move_to_save_button_and_click(self):

        move_to_save_button = self.browser.find_element(By.XPATH, "//form/div[2]/button[2]")
        self.browser.execute_script("arguments[0].scrollIntoView();", move_to_save_button)
        time.sleep(2)
        button = self.browser.find_element(By.XPATH, "//form/div[2]/button[2]")
        self.browser.execute_script("arguments[0].click();", button)


    def should_be_change_name_and_surname(self):
        time.sleep(2)
        move_to_appeal = self.browser.find_element(By.CLASS_NAME, "wb-type-heading-l")
        self.browser.execute_script("arguments[0].scrollIntoView();", move_to_appeal)

        time.sleep(2)

        checking_change = self.browser.find_element(By.CLASS_NAME, "upmc-user__text").text
        print(checking_change)


        assert "Госпожа Профессор Дарья Тестович" == checking_change, (
            "The status of the request and name has not changed")


    def _do_after_click_timeout(self):

        time.sleep(2)


    def go_to_logon_with_tan(self): # Для теста ввода кода

        login_button_wrapper = WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "iam-login-button")))
        login_button_wrapper.click()

        #login_button_wrapper = self.browser.find_element(By.CSS_SELECTOR, "iam-login-button")
        #login_button_wrapper.click()

        email_field = self.browser.find_element(By.CSS_SELECTOR, "#username")
        email_field.send_keys("testwebportalmercedes@gmail.com")
        submit_button = self.browser.find_element(By.CSS_SELECTOR, "#continue")
        submit_button.click()
        time.sleep(2)


        enter_with_password_button = self.browser.find_element(By.CSS_SELECTOR, "#login-with-otp")
        enter_with_password_button.click()







