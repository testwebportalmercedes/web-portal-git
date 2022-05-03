from selenium.webdriver.common.by import By

class LoginPageLocators():
    Find_Header = (By.CSS_SELECTOR, "cmm-cookie-banner")
    Click_Header = (By.CSS_SELECTOR, "cmm-cookie-banner")

class CookieBannerLocators():
    Cookie_Banner = (By.CSS_SELECTOR, "owc-header")
    Cookie_Accept_All = (By.CSS_SELECTOR, "div.owc-header__item-profile")
