from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
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


class BasePage():  # вспомогательные методы для работы с драйвером
    def __init__(self, browser, url, timeout=15):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

        # общая настройка

    def open(self):
        self.browser.get(self.url)

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

    def scroll_to_profile_wrapper(self):
        profile_wrapper = self.browser.find_element(By.CSS_SELECTOR, "owc-header")
        profile_form = self.browser.execute_script("return arguments[0].shadowRoot", profile_wrapper)
        profile_image = profile_form.find_element(By.CSS_SELECTOR, "div.owc-header__item-profile")
        self.browser.execute_script("arguments[0].scrollIntoView();", profile_image)

    def go_to_logon_with_email(self):

        login_button_wrapper = WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "iam-login-button")))
        login_button_wrapper.click()
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
            EC.element_to_be_clickable((By.XPATH, "/html/body/header")))
        personal_menu_second.click()

    def go_to_my_mercedes_me(self):
        personal_menu_second = self.browser.find_element(By.XPATH,
                                                         "/html/body/header")
        personal_menu_second.click()

    def go_to_my_mercedes_me_my_data(self):
        personal_menu_second = self.browser.find_element(By.XPATH,
                                                         "/html/body/header")
        personal_menu_second.click()

    def go_to_editing_request(self):
        time.sleep(2)
        iframe = self.browser.find_element(By.CSS_SELECTOR, '#upmc-cont')
        self.browser.switch_to.frame(iframe)
        button = WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "h4 > owm-svg > span > svg")))
        time.sleep(2)
        button.click()

    def go_to_editing_request_new(self):
        shadow_root = self.browser.find_element(By.CSS_SELECTOR, "mmu-settings-wrapper")
        shadow_root1 = self.browser.execute_script("return arguments[0].shadowRoot", shadow_root)
        request = shadow_root1.find_element(By.CSS_SELECTOR,
                                            '#main-router-view')
        request.click()

    def go_to_editing_request_new_back(self):
        shadow_root = self.browser.find_element(By.CSS_SELECTOR, "mmu-settings-wrapper")
        shadow_root1 = self.browser.execute_script("return arguments[0].shadowRoot", shadow_root)
        request = shadow_root1.find_element(By.CSS_SELECTOR,
                                            '#main-router-view > div > sw-router-view')
        request.click()

    def editing_request_from_mister_to_madam(self):
        button = self.browser.find_element(By.CSS_SELECTOR, '#upmc-SALUTATION-1')
        self.browser.execute_script("arguments[0].click();", button)

    def editing_request_from_mister_to_madam_new(self):
        shadow_root = self.browser.find_element(By.CSS_SELECTOR, "mmu-settings-wrapper")
        shadow_root1 = self.browser.execute_script("return arguments[0].shadowRoot", shadow_root)
        name = shadow_root1.find_element(By.CSS_SELECTOR,
                                         '#main-router-view > div > sw-router-view')
        name.click()

    def editing_request_from_mister_to_madam_new_back(self):
        shadow_root = self.browser.find_element(By.CSS_SELECTOR, "mmu-settings-wrapper")
        shadow_root1 = self.browser.execute_script("return arguments[0].shadowRoot", shadow_root)
        name = shadow_root1.find_element(By.CSS_SELECTOR,
                                         '#main-router-view > div > sw-router-view > section:nth-child(1)')
        name.click()

    def scroll_to_name_and_surname(self):
        move_to_editing_name_and_surname = self.browser.find_element(By.XPATH, '//label[text()="Уч. звание, степень"]')
        self.browser.execute_script("arguments[0].scrollIntoView();", move_to_editing_name_and_surname)

    def scroll_to_surname_and_save(self):
        shadow_root = self.browser.find_element(By.CSS_SELECTOR, "mmu-settings-wrapper")
        shadow_root1 = self.browser.execute_script("return arguments[0].shadowRoot", shadow_root)
        scroll_to_surname_and_sav = shadow_root1.find_element(By.CSS_SELECTOR,
                                                               '#main-router-view')
        self.browser.execute_script("arguments[0].scrollIntoView();", scroll_to_surname_and_sav)

    def editing_name_new(self):

        for i in range(5):
            shadow_root = self.browser.find_element(By.CSS_SELECTOR, "mmu-settings-wrapper")
            shadow_root1 = self.browser.execute_script("return arguments[0].shadowRoot", shadow_root)
            name = shadow_root1.find_element(By.CSS_SELECTOR,
                                             '#main-router-view > div > sw-router-view').send_keys(
                Keys.BACK_SPACE)

        shadow_root = self.browser.find_element(By.CSS_SELECTOR, "mmu-settings-wrapper")
        shadow_root1 = self.browser.execute_script("return arguments[0].shadowRoot", shadow_root)
        name = shadow_root1.find_element(By.CSS_SELECTOR,
                                         '#main-router-view > div > sw-router-view')
        name.send_keys('Игорь')

    def editing_name_new_back(self):
        for i in range(5):
            shadow_root = self.browser.find_element(By.CSS_SELECTOR, "mmu-settings-wrapper")
            shadow_root1 = self.browser.execute_script("return arguments[0].shadowRoot", shadow_root)
            name = shadow_root1.find_element(By.CSS_SELECTOR,
                                             '#main-router-view > div > sw-router-view').send_keys(
                Keys.BACK_SPACE)

        shadow_root = self.browser.find_element(By.CSS_SELECTOR, "mmu-settings-wrapper")
        shadow_root1 = self.browser.execute_script("return arguments[0].shadowRoot", shadow_root)
        name = shadow_root1.find_element(By.CSS_SELECTOR,
                                         '#main-router-view > div')
        name.send_keys('Иван')

    def editing_surname_new(self):
        for i in range(5):
            shadow_root = self.browser.find_element(By.CSS_SELECTOR, "mmu-settings-wrapper")
            shadow_root1 = self.browser.execute_script("return arguments[0].shadowRoot", shadow_root)
            name = shadow_root1.find_element(By.CSS_SELECTOR,
                                             '#main-router-view > div').send_keys(
                Keys.BACK_SPACE)

        shadow_root = self.browser.find_element(By.CSS_SELECTOR, "mmu-settings-wrapper")
        shadow_root1 = self.browser.execute_script("return arguments[0].shadowRoot", shadow_root)
        name = shadow_root1.find_element(By.CSS_SELECTOR,
                                         '#main-router-view > div > sw-router-view')
        name.send_keys('Норин')

    def editing_surname_new_back(self):

        for i in range(5):
            shadow_root = self.browser.find_element(By.CSS_SELECTOR, "mmu-settings-wrapper")
            shadow_root1 = self.browser.execute_script("return arguments[0].shadowRoot", shadow_root)
            name = shadow_root1.find_element(By.CSS_SELECTOR,
                                             '#main-router-view > div').send_keys(
                Keys.BACK_SPACE)

        shadow_root = self.browser.find_element(By.CSS_SELECTOR, "mmu-settings-wrapper")
        shadow_root1 = self.browser.execute_script("return arguments[0].shadowRoot", shadow_root)
        name = shadow_root1.find_element(By.CSS_SELECTOR,
                                         '#main-router')
        name.send_keys('Тест')

    def editing_data_birthday_new(self):

        shadow_root = self.browser.find_element(By.CSS_SELECTOR, "mmu-settings-wrapper")
        shadow_root1 = self.browser.execute_script("return arguments[0].shadowRoot", shadow_root)
        data = shadow_root1.find_element(By.CSS_SELECTOR,
                                         '#main-router-view > div')
        data.send_keys('12061995')

    def editing_data_birthday_new_back(self):

        shadow_root = self.browser.find_element(By.CSS_SELECTOR, "mmu-settings-wrapper")
        shadow_root1 = self.browser.execute_script("return arguments[0].shadowRoot", shadow_root)
        data = shadow_root1.find_element(By.CSS_SELECTOR,
                                         '#main-router-view')
        data.send_keys('05031990')

    def click_save_new(self):
        shadow_root = self.browser.find_element(By.CSS_SELECTOR, "mmu-settings-wrapper")
        shadow_root1 = self.browser.execute_script("return arguments[0].shadowRoot", shadow_root)
        shadow_root1.find_element(By.CSS_SELECTOR, '#account-info-save-btn').click()

    def check_save_new(self):
        time.sleep(4)
        shadow_root = self.browser.find_element(By.CSS_SELECTOR, "mmu-settings-wrapper")
        shadow_root1 = self.browser.execute_script("return arguments[0].shadowRoot", shadow_root)
        button = WebDriverWait(shadow_root1, timeout=10).until(lambda d: d.find_element
        (By.CSS_SELECTOR, "wb-notification-host > wb-notification > wb-notification-content")).text
        print(button)
        assert "Изменения сохранены." == button, (
            "Изменения не были сохранены.")

    def check_name_and_surname(self):
        personal_menu_first = self.browser.find_element(By.CSS_SELECTOR, "owc-header")
        profile_form = self.browser.execute_script("return arguments[0].shadowRoot", personal_menu_first)
        name = profile_form.find_element(By.CSS_SELECTOR,
                                         'header > div > nav.owc-header__top').text
        print(name)
        assert "Здравствуйте, Игорь Норин" == name, (
            "Имя не совпадает.")

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

    def go_to_logon_with_tan(self):  # Для теста ввода кода

        login_button_wrapper1 = WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "iam-login-button")))
        login_button_wrapper1.click()
        email_field1 = self.browser.find_element(By.CSS_SELECTOR, "#username")
        email_field1.send_keys("testwebportalmercedes+1@gmail.com")
        submit_button1 = self.browser.find_element(By.CSS_SELECTOR, "#continue")
        submit_button1.click()
        time.sleep(2)
        submit_button2 = self.browser.find_element(By.CLASS_NAME, "ui.fluid.basic.button")
        submit_button2.click()

    # Второе меню
    def go_to_editing_address_page(self):
        shadow_root = self.browser.find_element(By.CSS_SELECTOR, "mmu-settings-wrapper")
        shadow_root1 = self.browser.execute_script("return arguments[0].shadowRoot", shadow_root)
        shadow_root1.find_element(By.CSS_SELECTOR,
                                  '#mmu-left-menu > wb-subnavigation-item:nth-child(2) > sw-router-link').click()

    def check_page_address(self):
        shadow_root = self.browser.find_element(By.CSS_SELECTOR, "mmu-settings-wrapper")
        shadow_root1 = self.browser.execute_script("return arguments[0].shadowRoot", shadow_root)
        time.sleep(5)
        text_address = shadow_root1.find_element(By.CSS_SELECTOR, '#main-router-view > div > sw-router-view').text
        print(text_address[0:6])

        assert "Адреса" == text_address[0:6], (
            "страница не Адреса")

    def editing_post_index_new(self):
        for i in range(6):
            shadow_root = self.browser.find_element(By.CSS_SELECTOR, "mmu-settings-wrapper")
            shadow_root1 = self.browser.execute_script("return arguments[0].shadowRoot", shadow_root)
            shadow_root1.find_element(By.CSS_SELECTOR,
                                      '#address-form > div:nth-child(2) > div > wb-input-control > wb-input > input').send_keys(
                Keys.BACK_SPACE)

        shadow_root = self.browser.find_element(By.CSS_SELECTOR, "mmu-settings-wrapper")
        shadow_root1 = self.browser.execute_script("return arguments[0].shadowRoot", shadow_root)
        data = shadow_root1.find_element(By.CSS_SELECTOR,
                                         '#address-form > div:nth-child(2) > div > wb-input-control > wb-input > input')
        data.send_keys('777777')

    def editing_post_index_back(self):
        for i in range(6):
            shadow_root = self.browser.find_element(By.CSS_SELECTOR, "mmu-settings-wrapper")
            shadow_root1 = self.browser.execute_script("return arguments[0].shadowRoot", shadow_root)
            shadow_root1.find_element(By.CSS_SELECTOR,
                                      '#address-form > div:nth-child(2) > div > wb-input-control > wb-input > input').send_keys(
                Keys.BACK_SPACE)

        shadow_root = self.browser.find_element(By.CSS_SELECTOR, "mmu-settings-wrapper")
        shadow_root1 = self.browser.execute_script("return arguments[0].shadowRoot", shadow_root)
        data = shadow_root1.find_element(By.CSS_SELECTOR,
                                         '#address-form > div:nth-child(2) > div > wb-input-control > wb-input > input')
        data.send_keys('000000')

    def editing_province(self):

        shadow_root = self.browser.find_element(By.CSS_SELECTOR, "mmu-settings-wrapper")
        shadow_root1 = self.browser.execute_script("return arguments[0].shadowRoot", shadow_root)
        shadow_root1.find_element(By.CSS_SELECTOR,
                                  '#address-form > div:nth-child(3)').click()

    def editing_province_back(self):

        shadow_root = self.browser.find_element(By.CSS_SELECTOR, "mmu-settings-wrapper")
        shadow_root1 = self.browser.execute_script("return arguments[0].shadowRoot", shadow_root)
        shadow_root1.find_element(By.CSS_SELECTOR,
                                  '#address-form > div:nth-child(3) > div').click()

    def scroll_to_postindex(self):
        shadow_root = self.browser.find_element(By.CSS_SELECTOR, "mmu-settings-wrapper")
        shadow_root1 = self.browser.execute_script("return arguments[0].shadowRoot", shadow_root)

        scroll_to_postindex = shadow_root1.find_element(By.CSS_SELECTOR,
                                                        '#address-form > div:nth-child(2) > div > wb-input-control > wb-input > input')
        self.browser.execute_script("arguments[0].scrollIntoView();", scroll_to_postindex)

    def editing_city(self):
        shadow_root = self.browser.find_element(By.CSS_SELECTOR, "mmu-settings-wrapper")
        shadow_root1 = self.browser.execute_script("return arguments[0].shadowRoot", shadow_root)
        shadow_root1.find_element(By.CSS_SELECTOR,
                                  '#address-form > div:nth-child(4) > div').click()

    def editing_city_back(self):
        shadow_root = self.browser.find_element(By.CSS_SELECTOR, "mmu-settings-wrapper")
        shadow_root1 = self.browser.execute_script("return arguments[0].shadowRoot", shadow_root)
        shadow_root1.find_element(By.CSS_SELECTOR,
                                  '#address-form').click()

    def editing_street(self):

        for i in range(7):
            shadow_root = self.browser.find_element(By.CSS_SELECTOR, "mmu-settings-wrapper")
            shadow_root1 = self.browser.execute_script("return arguments[0].shadowRoot", shadow_root)
            shadow_root1.find_element(By.CSS_SELECTOR,
                                      '#address-form > div:nth-child(5) > div > wb-input-control > wb-input > input').send_keys(
                Keys.BACK_SPACE)

        shadow_root = self.browser.find_element(By.CSS_SELECTOR, "mmu-settings-wrapper")
        shadow_root1 = self.browser.execute_script("return arguments[0].shadowRoot", shadow_root)

        data = shadow_root1.find_element(By.CSS_SELECTOR,
                                         '#address-form > div:nth-child(5) > div > wb-input-control > wb-input > input')
        data.send_keys('Первая')

    def editing_street_back(self):

        for i in range(7):
            shadow_root = self.browser.find_element(By.CSS_SELECTOR, "mmu-settings-wrapper")
            shadow_root1 = self.browser.execute_script("return arguments[0].shadowRoot", shadow_root)
            shadow_root1.find_element(By.CSS_SELECTOR,
                                      '#address-form > div:nth-child(5) > div > wb-input-control > wb-input > input').send_keys(
                Keys.BACK_SPACE)

        shadow_root = self.browser.find_element(By.CSS_SELECTOR, "mmu-settings-wrapper")
        shadow_root1 = self.browser.execute_script("return arguments[0].shadowRoot", shadow_root)

        data = shadow_root1.find_element(By.CSS_SELECTOR,
                                         '#address-form > div:nth-child(5) > div > wb-input-control > wb-input > input')
        data.send_keys('Вторая')

    def editing_additional_street(self):

        for i in range(7):
            shadow_root = self.browser.find_element(By.CSS_SELECTOR, "mmu-settings-wrapper")
            shadow_root1 = self.browser.execute_script("return arguments[0].shadowRoot", shadow_root)
            shadow_root1.find_element(By.CSS_SELECTOR,
                                      '#address-form > div:nth-child(6) > div > wb-input-control > wb-input > input').send_keys(
                Keys.BACK_SPACE)

        shadow_root = self.browser.find_element(By.CSS_SELECTOR, "mmu-settings-wrapper")
        shadow_root1 = self.browser.execute_script("return arguments[0].shadowRoot", shadow_root)

        data = shadow_root1.find_element(By.CSS_SELECTOR,
                                         '#address-form > div:nth-child(6) > div > wb-input-control > wb-input > input')
        data.send_keys('Пятая')

    def editing_additional_street_back(self):

        for i in range(7):
            shadow_root = self.browser.find_element(By.CSS_SELECTOR, "mmu-settings-wrapper")
            shadow_root1 = self.browser.execute_script("return arguments[0].shadowRoot", shadow_root)
            shadow_root1.find_element(By.CSS_SELECTOR,
                                      '#address-form > div:nth-child(6) > div > wb-input-control > wb-input > input').send_keys(
                Keys.BACK_SPACE)

        shadow_root = self.browser.find_element(By.CSS_SELECTOR, "mmu-settings-wrapper")
        shadow_root1 = self.browser.execute_script("return arguments[0].shadowRoot", shadow_root)
        data = shadow_root1.find_element(By.CSS_SELECTOR,
                                         '#address-form > div:nth-child(6) > div > wb-input-control > wb-input > input')
        data.send_keys('Шестая')

    def editing_number_home(self):

        for i in range(5):
            shadow_root = self.browser.find_element(By.CSS_SELECTOR, "mmu-settings-wrapper")
            shadow_root1 = self.browser.execute_script("return arguments[0].shadowRoot", shadow_root)
            shadow_root1.find_element(By.CSS_SELECTOR,
                                      '#address-form > div:nth-child(7) > div > wb-input-control > wb-input > input').send_keys(
                Keys.BACK_SPACE)
        shadow_root = self.browser.find_element(By.CSS_SELECTOR, "mmu-settings-wrapper")
        shadow_root1 = self.browser.execute_script("return arguments[0].shadowRoot", shadow_root)
        data = shadow_root1.find_element(By.CSS_SELECTOR,
                                         '#address-form > div:nth-child(7) > div > wb-input-control > wb-input > input')
        data.send_keys('99')

    def editing_number_home_back(self):

        for i in range(5):
            shadow_root = self.browser.find_element(By.CSS_SELECTOR, "mmu-settings-wrapper")
            shadow_root1 = self.browser.execute_script("return arguments[0].shadowRoot", shadow_root)
            shadow_root1.find_element(By.CSS_SELECTOR,
                                      '#address-form > div:nth-child(7) > div > wb-input-control > wb-input > input').send_keys(
                Keys.BACK_SPACE)
        shadow_root = self.browser.find_element(By.CSS_SELECTOR, "mmu-settings-wrapper")
        shadow_root1 = self.browser.execute_script("return arguments[0].shadowRoot", shadow_root)
        data = shadow_root1.find_element(By.CSS_SELECTOR,
                                         '#address-form > div:nth-child(7) > div > wb-input-control > wb-input > input')
        data.send_keys('00')

    def click_save_address_new(self):
        shadow_root = self.browser.find_element(By.CSS_SELECTOR, "mmu-settings-wrapper")
        shadow_root1 = self.browser.execute_script("return arguments[0].shadowRoot", shadow_root)
        shadow_root1.find_element(By.CSS_SELECTOR, '#address-form > div:nth-child(8) > button').click()

    def check_save_address_new(self):
        time.sleep(4)
        shadow_root = self.browser.find_element(By.CSS_SELECTOR, "mmu-settings-wrapper")
        shadow_root1 = self.browser.execute_script("return arguments[0].shadowRoot", shadow_root)
        button = WebDriverWait(shadow_root1, timeout=10).until(lambda d: d.find_element
        (By.CSS_SELECTOR, "wb-notification-host > wb-notification > wb-notification-content")).text
        print(button)
        assert "Изменения сохранены." == button, (
            "Изменения не были сохранены.")
