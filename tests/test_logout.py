from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import burger_locators

class TestLogOut:
    def test_log_out_of_your_personal_account(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site')
        driver.find_element(*burger_locators.MAIN_PAGE_LOGIN_BUTTON).click()
        driver.find_element(*burger_locators.PASSWORD_INPUT_FIELD_LOGIN).send_keys(burger_locators.PASSWORD)
        driver.find_element(*burger_locators.EMAIL_INPUT_FIELD_LOGIN).send_keys(burger_locators.EMAIL)
        driver.find_element(*burger_locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(burger_locators.ORDER_BUTTON))
        driver.find_element(*burger_locators.PERSONAL_ACCAUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(burger_locators.EXIT_BUTTON))
        driver.find_element(*burger_locators.EXIT_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(burger_locators.LOGIN_BUTTON))
        assert driver.find_element(*burger_locators.TITLE_ENTER).text == 'Вход'
