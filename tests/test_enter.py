from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import burger_locators


class TestEnter:
    def test_enter_button_log_in_your_account(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site')
        driver.find_element(*burger_locators.MAIN_PAGE_LOGIN_BUTTON).click()
        driver.find_element(*burger_locators.PASSWORD_INPUT_FIELD_LOGIN).send_keys(burger_locators.PASSWORD)
        driver.find_element(*burger_locators.EMAIL_INPUT_FIELD_LOGIN).send_keys(burger_locators.EMAIL)
        driver.find_element(*burger_locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(burger_locators.ORDER_BUTTON))
        order_button = driver.find_element(*burger_locators.ORDER_BUTTON)
        assert order_button.is_displayed()

    def test_enter_log_in_personal_account_in_your_account(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site')
        driver.find_element(*burger_locators.PERSONAL_ACCAUNT_BUTTON).click()
        driver.find_element(*burger_locators.PASSWORD_INPUT_FIELD_LOGIN).send_keys(burger_locators.PASSWORD)
        driver.find_element(*burger_locators.EMAIL_INPUT_FIELD_LOGIN).send_keys(burger_locators.EMAIL)
        driver.find_element(*burger_locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(burger_locators.ORDER_BUTTON))
        order_button = driver.find_element(*burger_locators.ORDER_BUTTON)
        assert order_button.is_displayed()

    def test_enter_button_log_in_registration_page(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/register')
        driver.find_element(*burger_locators.BUTTON_LOGIN_IN_REG).click()
        driver.find_element(*burger_locators.PASSWORD_INPUT_FIELD_LOGIN).send_keys(burger_locators.PASSWORD)
        driver.find_element(*burger_locators.EMAIL_INPUT_FIELD_LOGIN).send_keys(burger_locators.EMAIL)
        driver.find_element(*burger_locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 15).until(expected_conditions.visibility_of_element_located(burger_locators.ORDER_BUTTON))
        order_button = driver.find_element(*burger_locators.ORDER_BUTTON)
        assert order_button.is_displayed()

    def test_enter_button_log_in_password_recovery_page(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/forgot-password')
        driver.find_element(*burger_locators.LOGIN_BUTTON_FOR_RECOVERY).click()
        driver.find_element(*burger_locators.PASSWORD_INPUT_FIELD_LOGIN).send_keys(burger_locators.PASSWORD)
        driver.find_element(*burger_locators.EMAIL_INPUT_FIELD_LOGIN).send_keys(burger_locators.EMAIL)
        driver.find_element(*burger_locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 15).until(expected_conditions.visibility_of_element_located(burger_locators.ORDER_BUTTON))
        order_button = driver.find_element(*burger_locators.ORDER_BUTTON)
        assert order_button.is_displayed()



