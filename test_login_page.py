from selenium import webdriver
import pytest
import time
import configparser
from selenium.webdriver.chrome.service import Service

from pages.mail_page import MainPage
from pages.registration_test_page import RegisterTest
from selenium.webdriver.common.by import By

link = "https://www.mercedes-benz.ru/"

link1 = "https://mail.google.com/"


@pytest.mark.smoke
def test_user_can_edit_name(browser):
    page = MainPage(browser, link)
    page.open()
    page.cookie_acceptance()
    page.go_to_profile_wrapper()
    page.go_to_logon_with_email()
    page._do_after_click_timeout()
    page.go_to_profile_wrapper()
    page._do_after_click_timeout()
    page.go_to_my_data()
    page._do_after_click_timeout()
    page._do_after_click_timeout()
    page.go_to_editing_request_new()
    page.editing_request_from_mister_to_madam_new()
    page.editing_name_new()
    page.editing_surename_new()
    page.scroll_to_surename_and_save()
    page.editing_data_birthday_new()
    page.click_save_new()
    page.check_save_new()
    page.scroll_to_profile_wrapper()
    page._do_after_click_timeout()
    page.go_to_editing_request_new_back()
    page.editing_request_from_mister_to_madam_new_back()
    page.editing_name_new_back()
    page.editing_surename_new_back()
    page.scroll_to_surename_and_save()
    page.editing_data_birthday_new_back()
    page._do_after_click_timeout()
    page.click_save_new()
    page.check_save_new()


@pytest.mark.smoke
def test_user_can_edit_address(browser):
    page = MainPage(browser, link)
    page.open()
    page.cookie_acceptance()
    page.go_to_profile_wrapper()
    page.go_to_logon_with_email()
    page._do_after_click_timeout()
    page.go_to_profile_wrapper()
    page._do_after_click_timeout()
    page.go_to_my_data()
    page._do_after_click_timeout()
    page._do_after_click_timeout()
    page.go_to_editing_address_page()
    page.check_page_address()
    page._do_after_click_timeout()
    page.editing_post_index_new()
    page.editing_province()
    page.scroll_to_postindex()
    page.editing_city()
    page.editing_street()
    page.editing_additional_street()
    page.editing_number_home()
    page.click_save_address_new()
    page.check_save_address_new()
    page._do_after_click_timeout()
    page.scroll_to_profile_wrapper()
    page.editing_post_index_back()
    page.editing_province_back()
    page.scroll_to_postindex()
    page.editing_city_back()
    page.editing_street_back()
    page.editing_additional_street_back()
    page.editing_number_home_back()
    page._do_after_click_timeout()
    page.click_save_address_new()
    page.check_save_address_new()
    page._do_after_click_timeout()


@pytest.mark.smoke
def test_user_can_edit_date_of_birth(browser):
    page = MainPage(browser, link)
    page.open()
    page.cookie_acceptance()
    page.go_to_profile_wrapper()
    page.go_to_logon_with_email()
    page._do_after_click_timeout()
    page.go_to_profile_wrapper()
    page._do_after_click_timeout()
    page.go_to_my_data()
    page._do_after_click_timeout()
    page.scroll_to_editing_adress()
    page.go_to_editing_date_of_birth()
    page.editing_day()
    page.editing_mounths()
    page.editing_years()
    page.save_button_click()
    page.should_be_change_date_of_birth()
    page.go_to_editing_date_of_birth()
    page.editing_day_back()
    page.editing_month_back()
    page.editing_years_back()
    page.save_button_click()
    page.should_be_change_date_of_birth_back()


@pytest.mark.register
def test_user_can_register(browser):
    page = MainPage(browser, link)
    page.open()
    window_before = browser.window_handles[0]
    time.sleep(3)
    browser.get("https://www.mercedes-benz.ru/bin/daimler/public/ciam/registration.html?lang=ru_RU")
    page.enter_information_for_register()
    browser2 = webdriver.Chrome()
    page1 = MainPage(browser2, link1)
    browser2.get(link1)
    browser2.set_window_size(1280, 1280)
    time.sleep(2)
    page1.enter_email_password_google()
    time.sleep(6)
    cod = browser2.find_element(By.XPATH,
                                '//*[@id=":2c"]/span').text
    browser2.close()
    tatcod = browser.find_element(By.CSS_SELECTOR, "#tan1")
    tatcod.send_keys(cod[:6])
    page.enter_tat_cod_and_click()
    time.sleep(6)
    page.cookie_acceptance()
    page.click_no_car()
    time.sleep(5)
    page.go_to_profile_wrapper()
    time.sleep(4)
    page.go_to_my_data()
    page.move_to_delete_account_and_click_new()
    time.sleep(5)
    browser.close()
    time.sleep(5)


@pytest.mark.register_test
def test_user_can_register1(browser):
    page = MainPage(browser, link)
    page.open()
    window_before = browser.window_handles[0]
    time.sleep(3)
    browser.get("https://www.mercedes-benz.ru")
    page.cookie_acceptance()
    page.go_to_profile_wrapper()
    page.go_to_logon_with_tan()
    browser3 = webdriver.Chrome()
    page1 = MainPage(browser3, link1)
    browser3.get(link1)
    browser3.set_window_size(1280, 1280)
    time.sleep(2)
    page1.enter_email_password_google()
    time.sleep(6)
    cod = browser3.find_element(By.CSS_SELECTOR,
                                '#\:2c > span').text
    browser3.close()
    tatcod = browser.find_element(By.CSS_SELECTOR, "#tan1")
    tatcod.send_keys(cod[:6])
    page.enter_tat_cod_and_click()
    time.sleep(6)
    page.cookie_acceptance()
    page.click_no_car()
    time.sleep(5)
    page.go_to_profile_wrapper()
    time.sleep(4)
    page.go_to_profile_wrapper_after_my_data()
    page.go_to_my_mercedes_me_my_data()
    page.move_to_delete_account_and_click()
    time.sleep(5)
    browser.close()
    time.sleep(5)


@pytest.mark.menu
def test_checking_menu_links(browser):
    page = MainPage(browser, link)
    page.open()
    page.cookie_acceptance()
    page.go_to_profile_wrapper()
    page.go_to_logon_with_email()
    page._do_after_click_timeout()
    page.go_to_profile_wrapper()
    page._do_after_click_timeout()
    page.go_to_my_car()  # переход в мои автомобили +
    page.checking_go_to_my_car()  # проверка перехода в мои автомобили +
    page.go_to_profile_wrapper()  # клик по иконке меню +
    page.go_to_my_data()  # переход в мои данные +
    page.checking_go_to_my_data()  # проверка перехода в мои данные работает ++
    page.go_to_adress()  # переход в новый адресс +
    page.go_to_entry_and_security()  # новый вход и безопасность +
    page.go_to_profile_wrapper()  # клик по иконке меню+
    page.go_to_my_messages()  # переход в мои сообщения +
    page.checking_go_to_my_messages_new()  # проверка перехода в мои сообщения новая +
    page._do_after_click_timeout()
    page.go_to_profile_wrapper()  # клик по иконке меню+
    page.go_to_setting()  # Переход в мои настройки+
    page._do_after_click_timeout()
    page.checking_go_to_setting()  # Проверка перехода в мои настройки +
    page.checking_configuring_incoming_messages()  # проверка настройки входящих сообщений в моих настройках +
    page.communication_channels()  # переход в каналы связи +
    page.check_go_to_communication_channels()  # проверка перехода в каналы связи +
    page._do_after_click_timeout()
    page.units_of_measurement()  # переход в еденицы измерения+
    page.check_go_to_units_of_measurement()  # проверка перехода в еденицы измерения+
    page._do_after_click_timeout()
    page.connect_terms_of_use()  # переход в условия пользования+
    page.check_go_to_connect_terms_of_use()  # проверка перехода в условия пользования
    page.go_to_profile_wrapper()  # клик по иконке меню+
    page._do_after_click_timeout()
    page.terms_of_use()  # переход в условия пользования из меню
    page.check_go_to_connect_terms_of_use()  # проверка перехода в условия пользования из меню
    page._do_after_click_timeout()
    time.sleep(5)


if __name__ == "__main__":
    test_user_can_edit_name()

    # pytest - s test_login_page.py
    # pytest test_login_page.py

    # pytest -s -vv -m smoke test_login_page.py запуск теста проверки личных данных(смоук)

    # pytest -s -vv -m register test_login_page.py запуск теста регистрации
    # pytest -s -vv -m menu test_login_page.py запуск теста проверки меню
    # pytest -s -vv -m new test_login_page.py
