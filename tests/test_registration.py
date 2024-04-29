from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import burger_locators
from helpers import get_sign_up_date
from data import user_data
from config import URL_REGISTRATION

class TestRegistration:
    def test_registration_new_user(self, driver):
        driver.get(URL_REGISTRATION)
        email_data, password_data, name_data = get_sign_up_date()
        driver.find_element(*burger_locators.NAME_INPUT_FIELD).send_keys(name_data)
        driver.find_element(*burger_locators.EMAIL_INPUT_FIELD).send_keys(email_data)
        driver.find_element(*burger_locators.PASSWORD_INPUT_FIELD).send_keys(password_data)
        driver.find_element(*burger_locators.BUTTON_LOGIN_IN_REG).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(burger_locators.LOGIN_BUTTON))
        login_button = driver.find_element(*burger_locators.LOGIN_BUTTON)
        assert login_button.is_displayed()


    def test_registration_new_user_invalid_password(self, driver):
        driver.get(URL_REGISTRATION)
        email_data, name_data, _ = get_sign_up_date()
        driver.find_element(*burger_locators.NAME_INPUT_FIELD).send_keys(name_data)
        driver.find_element(*burger_locators.EMAIL_INPUT_FIELD).send_keys(email_data)
        driver.find_element(*burger_locators.PASSWORD_INPUT_FIELD).send_keys(user_data.INVALID_PASSWORD)
        driver.find_element(*burger_locators.BUTTON_LOGIN_IN_REG).click()
        error_password = driver.find_element(*burger_locators.ERROR_PASSWORD)
        assert error_password.is_displayed()

    def test_registration_new_user_invalid_name(self, driver):
        driver.get(URL_REGISTRATION)
        email_data, password_data, _ = get_sign_up_date()
        driver.find_element(*burger_locators.NAME_INPUT_FIELD).send_keys()
        driver.find_element(*burger_locators.EMAIL_INPUT_FIELD).send_keys(email_data)
        driver.find_element(*burger_locators.PASSWORD_INPUT_FIELD).send_keys(password_data)
        driver.find_element(*burger_locators.BUTTON_LOGIN_IN_REG).click()
        error_name = driver.find_element(*burger_locators.ERROR_NAME)
        assert error_name.is_displayed()

    def test_registration_new_user_invalid_email(self, driver):
        driver.get(URL_REGISTRATION)
        name_data, password_data, _ = get_sign_up_date()
        driver.find_element(*burger_locators.NAME_INPUT_FIELD).send_keys(name_data)
        driver.find_element(*burger_locators.EMAIL_INPUT_FIELD).send_keys(user_data.INVALID_EMAIL)
        driver.find_element(*burger_locators.PASSWORD_INPUT_FIELD).send_keys(password_data)
        driver.find_element(*burger_locators.BUTTON_LOGIN_IN_REG).click()
        error_email = driver.find_element(*burger_locators.ERROR_EMAIL)
        assert error_email.is_displayed()