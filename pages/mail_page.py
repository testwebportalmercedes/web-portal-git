from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from pages.address_page import EditAdress
from pages.address_page_back import EditAdressBack
from pages.appeal_page_back import AppealPage_Back
from pages.date_of_birth_page import DataBirthPage
from pages.date_of_birth_page_back import DateBirthPageBack
from pages.registration_test_page import  RegisterTest
from pages.test_checking_menu_links import  CheckingMenuLinks
class MainPage(BasePage, EditAdress, EditAdressBack, AppealPage_Back, DataBirthPage, DateBirthPageBack, RegisterTest, CheckingMenuLinks):
    def go_to_login_page(self):
        pass

