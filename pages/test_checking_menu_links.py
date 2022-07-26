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
        time.sleep(1)
        arrow_prevs = my_cars_areas_shadow.find_elements(By.CLASS_NAME, 'wb-type-copy-strong.page-header__title')

        for one in arrow_prevs:
            print(one.text)
            assert "Мои автомобили" == one.text, (
                "'Мои автомобили' - Текст не совпадает")


    def go_to_back_my_data(self):
        back_my_data = self.browser.find_element(By.CLASS_NAME, "aem--logo__link")
        back_my_data.click()

    def checking_go_to_my_data(self):
        time.sleep(5)
        iframe = self.browser.find_element(By.CSS_SELECTOR, '#upmc-cont')
        self.browser.switch_to.frame(iframe)
        time.sleep(1)
        checking_go_to_my_data = WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "wb-type-heading-l.upmc-headline"))).text
        time.sleep(1)
        print(checking_go_to_my_data)

        assert checking_go_to_my_data == "Мой профиль Mercedes me", (
            "'Мой профиль Mercedes me' - Текст не совпадает")

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
        assert my_messages == "Мои сообщения", (
            "'Мои сообщения' - Текст не совпадает")

        self.browser.switch_to.default_content()

    def go_to_back_with_my_messages(self):
        back_with_my_messages = self.browser.find_element(By.CSS_SELECTOR, "body > header > nav > div.aem--headerMainNavigation__base > div > div > ul > div > a")
        back_with_my_messages.click()


    def go_to_setting(self):

        menu_shadowRoot = self.browser.find_element(By.CSS_SELECTOR, "owc-header")
        my_messages = self.browser.execute_script("return arguments[0].shadowRoot", menu_shadowRoot)
        time.sleep(1)
        menu_setting = my_messages.find_element(By.LINK_TEXT, "Настройки, конфиденциальность и правовая информаци")
        menu_setting.click()


    def checking_go_to_setting(self): # не делал

        menu_shadowRoot = self.browser.find_element(By.CSS_SELECTOR, "mmu-settings-wrapper")
        my_setting = self.browser.execute_script("return arguments[0].shadowRoot", menu_shadowRoot)
        time.sleep(1)
        menu_setting = my_setting.find_element(By.CLASS_NAME, "headline").text
        print(menu_setting)
        assert menu_setting == "Настройки, конфиденциальность и правовая информация", (
            "'Настройки, конфиденциальность и правовая информация' - Текст не совпадает")





    def checking_configuring_incoming_messages(self):
        root1 = self.browser.find_element(By.CSS_SELECTOR, 'mmu-settings-wrapper')
        shadow_root1 = self.browser.execute_script('return arguments[0].shadowRoot', root1)

        #root2 = shadow_root1.find_element(By.CSS_SELECTOR, 'sw-router-view')
        #shadow_root2 = self.browser.execute_script('return arguments[0].shadowRoot', root2)
        time.sleep(1)
        menu_settings = shadow_root1.find_element(By.CLASS_NAME, "wb-type-heading-l.wb-margin-bottom-xxs.hide-title").text
        print(menu_settings)
        assert menu_settings == "Настройки входящих сообщений", (
            "'Настройки входящих сообщений' - Текст не совпадает")

    def communication_channels(self):
        root1 = self.browser.find_element(By.CSS_SELECTOR, 'mmu-settings-wrapper')
        shadow_root1 = self.browser.execute_script('return arguments[0].shadowRoot', root1)

        units_of_measurement = shadow_root1.find_element(By.CSS_SELECTOR,
                                                         '#mmu-left-menu > wb-subnavigation-item:nth-child(2) > sw-router-link').click()

    def check_go_to_communication_channels(self):
        root1 = self.browser.find_element(By.CSS_SELECTOR, 'mmu-settings-wrapper')
        shadow_root1 = self.browser.execute_script('return arguments[0].shadowRoot', root1)
        time.sleep(3)
        communication_channelsnew = shadow_root1.find_element(By.CSS_SELECTOR, "#main-router-view > div > sw-router-view > section:nth-child(2) > div > div > div").text
        #proverka = []
        #for text in communication_channelsnew.split(" "):
            #proverka.append(text)
        print(communication_channelsnew[:29])


        assert communication_channelsnew[:29] == "Предпочтительные каналы связи",(

        "'Предпочтительные каналы связи' - ""Текст не совпадает")

    def units_of_measurement(self):
        root1 = self.browser.find_element(By.CSS_SELECTOR, 'mmu-settings-wrapper')
        shadow_root1 = self.browser.execute_script('return arguments[0].shadowRoot', root1)

        units_of_measurement = shadow_root1.find_element(By.CSS_SELECTOR,
                                                       '#mmu-left-menu > wb-subnavigation-item:nth-child(3) > sw-router-link > span')

        units_of_measurement.click()



    def check_go_to_units_of_measurement(self):
        root1 = self.browser.find_element(By.CSS_SELECTOR, 'mmu-settings-wrapper')
        shadow_root1 = self.browser.execute_script('return arguments[0].shadowRoot', root1)
        text_units_of_measurement = shadow_root1.find_element(By.CSS_SELECTOR, "#main-router-view > div > sw-router-view").text
        print(text_units_of_measurement[:17])
        assert text_units_of_measurement[:17] == "Единицы измерения", (
            "'Единицы измерения' - Текст не совпадает")

    def connect_terms_of_use(self):
        root1 = self.browser.find_element(By.CSS_SELECTOR, 'mmu-settings-wrapper')
        shadow_root1 = self.browser.execute_script('return arguments[0].shadowRoot', root1)

        #root2 = shadow_root1.find_element(By.CSS_SELECTOR, 'sw-router-link')
        #shadow_root2 = self.browser.execute_script('return arguments[0].shadowRoot', root2)

        connect_terms_of_use = shadow_root1.find_element(By.CSS_SELECTOR,'#mmu-left-menu > wb-subnavigation-item:nth-child(4) > a')
        #print("Element is visible? " + str(communication_channels.is_displayed()))
        connect_terms_of_use.click()
        #print(type (communication_channels))
        #if shadow_root1.find_element(By.CLASS_NAME,'wb-type-button-secondary.wb-link'):
            #print("Element exists")

    def check_go_to_connect_terms_of_use(self):
        root1 = self.browser.find_element(By.CSS_SELECTOR, 'mmcs-touc-wrapper')
        shadow_root1 = self.browser.execute_script('return arguments[0].shadowRoot', root1)
        time.sleep(2)

        text_connect_terms_of_use = shadow_root1.find_element(By.CLASS_NAME,
                                                              "wb-type-heading-l.wb-margin-top-xs.wb-margin-bottom-xs").text
        print(text_connect_terms_of_use)
        assert text_connect_terms_of_use == "Условия использования", (
            "'Условия использования' - Текст не совпадает")


    #def go_to_back_with_my_messages(self):
        #back_with_my_messages = self.browser.find_element(By.CLASS_NAME, "aem--logo__link")
        #print(back_with_my_messages)

    def terms_of_use(self):
        menu_shadowRoot = self.browser.find_element(By.CSS_SELECTOR, "owc-header")
        profile_form = self.browser.execute_script("return arguments[0].shadowRoot", menu_shadowRoot)
        menu_terms_of_use = profile_form.find_element(By.LINK_TEXT, "Условия пользования")
        menu_terms_of_use.click()