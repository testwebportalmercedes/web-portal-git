import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC

class CheckingMenuLinks():            # вспомогательные методы для работы с драйвером
    def __init__(self, browser, url, timeout=15):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)



    def go_to_my_car(self):
        #time.sleep(3)
        menu_shadowRoot = self.browser.find_element(By.CSS_SELECTOR, "owc-header")
        profile_form = self.browser.execute_script("return arguments[0].shadowRoot", menu_shadowRoot)
        menu_my_car = profile_form.find_element(By.LINK_TEXT, "Мои автомобили")
        menu_my_car.click()






    def checking_go_to_my_car(self):

        my_cars_areas = self.browser.find_element(By.CSS_SELECTOR, "mmv-vehicle-stage")
        my_cars_areas_shadow = self.browser.execute_script("return arguments[0].shadowRoot", my_cars_areas)

        arrow_prevs = my_cars_areas_shadow.find_elements(By.CLASS_NAME, 'wb-type-copy-strong.page-header__title')

        for one in arrow_prevs:
            print(one.text)
            assert "Мои автомобили" == one.text, (
                "The status of the request and name has not changed")


    def go_to_back_my_data(self):
        back_my_data = self.browser.find_element(By.CLASS_NAME, "aem--logo__link")
        back_my_data.click()

    def checking_go_to_my_data(self):
        time.sleep(5)
        iframe = self.browser.find_element(By.CSS_SELECTOR, '#upmc-cont')
        self.browser.switch_to.frame(iframe)

        button = WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "wb-type-heading-l.upmc-headline"))).text
        time.sleep(2)
        print(button)

        self.browser.switch_to.default_content()




    def go_to_my_messages(self):

        menu_shadowRoot = self.browser.find_element(By.CSS_SELECTOR, "owc-header")
        my_messages = self.browser.execute_script("return arguments[0].shadowRoot", menu_shadowRoot)

        menu_my_messages = my_messages.find_element(By.LINK_TEXT, "Мои сообщения")
        menu_my_messages.click()


    def checking_go_to_my_messages(self):

        iframe = self.browser.find_element(By.ID, 'cmic-reachme-cont')
        self.browser.switch_to.frame(iframe)

        my_messages = WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "wb-type-heading-m"))).text
        time.sleep(2)
        print(my_messages)

        self.browser.switch_to.default_content()

    def go_to_back_with_my_messages(self):
        back_with_my_messages = self.browser.find_element(By.CLASS_NAME, "aem--logo__link")
        back_with_my_messages.click()


    def go_to_setting(self): # не делал

        menu_shadowRoot = self.browser.find_element(By.CSS_SELECTOR, "owc-header")
        my_messages = self.browser.execute_script("return arguments[0].shadowRoot", menu_shadowRoot)

        menu_setting = my_messages.find_element(By.LINK_TEXT, "Настройки, конфиденциальность и правовая информаци")
        menu_setting.click()


    def checking_go_to_setting(self): # не делал

        menu_shadowRoot = self.browser.find_element(By.CSS_SELECTOR, "mmu-settings-wrapper")
        my_setting = self.browser.execute_script("return arguments[0].shadowRoot", menu_shadowRoot)

        menu_setting = my_setting.find_element(By.CLASS_NAME, "headline").text
        print(menu_setting)






    def checking_configuring_incoming_messages(self):
        root1 = self.browser.find_element(By.CSS_SELECTOR, 'mmu-settings-wrapper')
        shadow_root1 = self.browser.execute_script('return arguments[0].shadowRoot', root1)

        #root2 = shadow_root1.find_element(By.CSS_SELECTOR, 'sw-router-view')
        #shadow_root2 = self.browser.execute_script('return arguments[0].shadowRoot', root2)

        menu_settings = shadow_root1.find_element(By.CLASS_NAME, "wb-type-heading-l.wb-margin-bottom-xxs.hide-title").text
        print(menu_settings)


    def go_to_back_with_my_messages(self):
        back_with_my_messages = self.browser.find_element(By.CLASS_NAME, "aem--logo__link")
        back_with_my_messages.click()