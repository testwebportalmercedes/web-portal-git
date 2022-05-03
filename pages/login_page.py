import time
from selenium.webdriver.common.by import By
from selenium import webdriver
browser = webdriver.Chrome()
browser.get("https://www.mercedes-benz.ru/")
browser.set_window_size(1080, 1080)

time.sleep(3)

cookie_popup = browser.find_element(By.CSS_SELECTOR, "cmm-cookie-banner")
# Shadow content trick
cookie_form = browser.execute_script("return arguments[0].shadowRoot", cookie_popup)
accept_all = cookie_form.find_element(By.CSS_SELECTOR, "button.wb-button--accept-all")
accept_all.click()

time.sleep(3)

profile_wrapper = browser.find_element(By.CSS_SELECTOR, "owc-header")
profile_form = browser.execute_script("return arguments[0].shadowRoot", profile_wrapper)
profile_image = profile_form.find_element(By.CSS_SELECTOR, "div.owc-header__item-profile")
profile_image.click()

time.sleep(3)

login_button_wrapper = browser.find_element(By.CSS_SELECTOR, "iam-login-button")
login_button_wrapper.click()
time.sleep(3)
email_field = browser.find_element(By.CSS_SELECTOR, "#username")
email_field.send_keys("mbcee.test+2@gmail.com")
submit_button = browser.find_element(By.CSS_SELECTOR, "#continue")
submit_button.click()
time.sleep(3)
enter_with_password_button = browser.find_element(By.CSS_SELECTOR, "#login-with-password")
enter_with_password_button.click()
time.sleep(3)
input_pass_field = browser.find_element(By.CSS_SELECTOR, "#password")
input_pass_field.send_keys("Ntcn1234$")
confirm_button = browser.find_element(By.CSS_SELECTOR, "#confirm")
confirm_button.click()