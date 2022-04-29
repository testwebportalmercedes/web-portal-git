from selenium import webdriver
import pytest
import time
import configparser
from selenium.webdriver.chrome.service import Service

#from pages.edit_address import EditAdress
from pages.mail_page import MainPage

from selenium.webdriver.common.by import By

link = "https://www.mercedes-benz.ru/"
link1 = "https://www.mercedes-benz.ru/bin/daimler/public/ciam/registration.html?lang=ru_RU"

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
    #page.go_to_profile_wrapper_after_my_data()
    #page.go_to_my_mercedes_me()
    #page.go_to_my_mercedes_me_my_data()
    page.go_to_editing_request()
    page.editing_request_from_mister_to_madam()
    #page.should_be_message_about_my_profil_mercedes_me() #Проверка
    page.scroll_to_name_and_surename() #скролл к имени
    page.editing_degree()
    page.editing_name()
    page.editing_surename()
    page.move_to_save_button_and_click()
    page.should_be_change_name_and_surename()

    page.go_to_editing_request_after_verification()
    page.editing_request_from_madam_to_mister_back()
    page.scroll_to_name_and_surename()
    page.editing_degree_back()
    page.editing_name_back()
    page.editing_surename_back()

    page.move_to_save_button_and_click()
    page.should_be_change_name_and_surename_back()


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
    page.go_to_my_data()
    #page.go_to_profile_wrapper_after_my_data()
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
    page._do_after_click_timeout()
    page.go_to_my_data()
    #page.go_to_profile_wrapper_after_my_data()
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
    page.editing_mounths_back()
    page.editing_years_back()
    page.save_button_click()
    page.should_be_change_date_of_birth_back()




if __name__ == "__main__":
    test_user_can_edit_name()

    # pytest - s test_login_page.py
    #pytest test_login_page.py

    #pytest -s -v -m smoke test_login_page.py

    #pytest quickstart.py

