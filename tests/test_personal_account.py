from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import burger_locators
from config import URL

class TestPersonalAccount:
    def test_log_in_your_personal_account(self, driver):
        driver.get(URL)
        driver.find_element(*burger_locators.PERSONAL_ACCAUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(burger_locators.LOGIN_BUTTON))
        order_button = driver.find_element(*burger_locators.LOGIN_BUTTON)
        assert order_button.is_displayed()

    def test_transfer_from_your_personal_account_in_constructor(self, driver):
        driver.get(URL)
        driver.find_element(*burger_locators.PERSONAL_ACCAUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(burger_locators.LOGIN_BUTTON))
        driver.find_element(*burger_locators.CONSTRUCTOR_BUTTON).click()
        assert driver.find_element(*burger_locators.TITLE_IN_THE_MAIN_PAGE).text == "Соберите бургер"

    def test_transfer_from_your_personal_account_in_stellar_burgers(self, driver):
        driver.get(URL)
        driver.find_element(*burger_locators.PERSONAL_ACCAUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(burger_locators.LOGIN_BUTTON))
        driver.find_element(*burger_locators.STELLAR_BURGERS_BUTTON).click()
        assert driver.find_element(*burger_locators.TITLE_IN_THE_MAIN_PAGE).text == "Соберите бургер"



