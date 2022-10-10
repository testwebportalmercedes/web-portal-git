from selenium import webdriver
import pytest
import time
import configparser
from selenium.webdriver.chrome.service import Service


from pages.mail_page import MainPage
from pages.registration_test_page import RegisterTest
from selenium.webdriver.common.by import By

link = "https://www.mercedes-benz.ru/"

link1 ="https://mail.google.com/"

@pytest.mark.smoke
def test_user_can_edit_name(browser):
    page = MainPage(browser, link)
    page.open()
    page.cookie_acceptance()
    page.go_to_profile_wrapper()
    page.go_to_logon_with_email()
    #page.should_be_message_about_login()
    page._do_after_click_timeout()
    page.go_to_profile_wrapper()
    page._do_after_click_timeout()

    page.go_to_my_data()
    #page.go_to_my_setting()  #new
    #page._do_after_click_timeout()
    #page.go_to_profile_wrapper_after_my_data() #new
    page._do_after_click_timeout()
    #page.go_to_my_mercedes_me()  #new
    #page.go_to_my_mercedes_me_my_data() #new
    page.go_to_editing_request()
    page.editing_request_from_mister_to_madam()
    page.scroll_to_name_and_surename() #скролл к имени
    page.editing_degree()
    page.editing_name()
    page.editing_surname()
    page.move_to_save_button_and_click()
    page.should_be_change_name_and_surname()

    page.go_to_editing_request_after_verification()
    page.editing_request_from_madam_to_mister_back()
    page.scroll_to_name_and_surename()
    page.editing_degree_back()
    page.editing_name_back()
    page.editing_surname_back()

    page.move_to_save_button_and_click()

    page.should_be_change_name_and_surname_back()



@pytest.mark.smoke
def test_user_can_edit_address(browser):
    page = MainPage(browser, link)
    page.open()
    page.cookie_acceptance()
    page.go_to_profile_wrapper()
    page.go_to_logon_with_email()
    #page.should_be_message_about_login()
    page._do_after_click_timeout()
    page.go_to_profile_wrapper()
    page._do_after_click_timeout()
    #page.go_to_my_setting()
    page.go_to_my_data()

    #page.go_to_profile_wrapper_after_my_data()
    page._do_after_click_timeout()
    #page.go_to_my_mercedes_me()
    #page.go_to_my_mercedes_me_my_data()
    page.scroll_to_editing_adress()

    page.go_to_editing_adress()
    page._do_after_click_timeout()
    page.editing_street()
    page.scroll_to_house()
    page.editing_house()
    page.editing_post_index()
    page.editing_town()
    page.subject()
    page.editing_District()
    page.save_button_and_click_after_edit_adress()
    page.scroll_to_editing_adress_after_saving_change()
    page.should_be_change_adress()
    page.go_to_editing_adress_after_changes_and_checks()

    page.editing_street_back()
    page.scroll_to_house()
    page.editing_house_back()
    page.editing_post_index_back()
    page.editing_town_back()
    page.subject_back()
    page.editing_District_back()
    page.save_button_and_click_after_edit_adress()
    page.scroll_to_editing_adress_after_saving_change()
    page.should_be_change_adress_back()

@pytest.mark.smoke
def test_user_can_edit_date_of_birth(browser):
    page = MainPage(browser, link)
    page.open()
    page.cookie_acceptance()
    page.go_to_profile_wrapper()
    page.go_to_logon_with_email()
    #page.should_be_message_about_login()
    page._do_after_click_timeout()
    page.go_to_profile_wrapper()
    #page.go_to_my_setting()
    page._do_after_click_timeout()
    page.go_to_my_data()
    #page.go_to_profile_wrapper_after_my_data()
    page._do_after_click_timeout()
    #page.go_to_my_mercedes_me()
    #page.go_to_my_mercedes_me_my_data()
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

    #page1.go_to_code()


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
    #page.go_to_profile_wrapper_after_my_data()
    #page.go_to_my_mercedes_me()
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

    #page1.go_to_code()


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
    #page.go_to_my_mercedes_me()
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
    page.go_to_my_car() #переход в мои автомобили +
    page.checking_go_to_my_car() #проверка перехода в мои автомобили +
    page.go_to_profile_wrapper() #клик по иконке меню +
    page.go_to_my_data()   # переход в мои данные +
    page.checking_go_to_my_data() #проверка перехода в мои данные работает +
    page.go_to_back_my_data() #переход обратно работает+
    page._do_after_click_timeout()
    page.go_to_profile_wrapper()  # клик по иконке меню+
    page.go_to_my_messages() # переход в мои сообщения +
    page.checking_go_to_my_messages() #проверка перехода в мои сообщения +
    page.go_to_back_with_my_messages() #переход обратно+
    page._do_after_click_timeout()
    page.go_to_profile_wrapper()  # клик по иконке меню+
    page.go_to_setting() #Переход в мои настройки+
    page._do_after_click_timeout()
    page.checking_go_to_setting() #Проверка перехода в мои настройки +
    page.checking_configuring_incoming_messages()  # проверка настройки входящих сообщений в моих настройках +
    page.communication_channels() # переход в каналы связи +
    page.check_go_to_communication_channels() #проверка перехода в каналы связи +
    page._do_after_click_timeout()

    page.units_of_measurement() # переход в еденицы измерения+
    page.check_go_to_units_of_measurement() #проверка перехода в еденицы измерения+
    page._do_after_click_timeout()
    page.connect_terms_of_use() # переход в условия пользования+
    page.check_go_to_connect_terms_of_use() # проверка перехода в условия пользования

    page.go_to_profile_wrapper()  # клик по иконке меню+
    page._do_after_click_timeout()
    page.terms_of_use() #переход в условия пользования из меню
    page.check_go_to_connect_terms_of_use() # проверка перехода в условия пользования из меню
    page._do_after_click_timeout()
    time.sleep(5)



















if __name__ == "__main__":
    test_user_can_edit_name()

    #pytest - s test_login_page.py
    #pytest test_login_page.py

    #pytest -s -vv -m smoke test_login_page.py запуск теста проверки личных данных(смоук)

    #pytest -s -vv -m register test_login_page.py запуск теста регистрации
    #pytest -s -vv -m menu test_login_page.py запуск теста проверки меню
    #pytest -s -vv -m new test_login_page.py
