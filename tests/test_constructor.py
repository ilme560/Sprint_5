from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import burger_locators

class TestConstructor:
    def test_go_to_the_bread_section(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(*burger_locators.BREAD_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(burger_locators.BREAD_CONTENT))
        name_buns = driver.find_element(*burger_locators.BREAD_CONTENT)
        assert name_buns.is_displayed()

    def test_go_to_the_sauces_section(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(*burger_locators.SAUCES_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(burger_locators.SAUCES_CONTENT))
        name_sauces = driver.find_element(*burger_locators.SAUCES_CONTENT)
        assert name_sauces.is_displayed()

    def test_go_to_the_filings_section(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(*burger_locators.FILINGS_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(burger_locators.FILINGS_CONTENT))
        name_filings = driver.find_element(*burger_locators.FILINGS_CONTENT)
        assert name_filings.is_displayed()