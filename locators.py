from selenium.webdriver.common.by import By

class burger_locators:

    # Тестовые данные для регистрации пользователя с паролем меньше 6 символов:
    EMAIL = "ilme560@yandex.ru"
    PASSWORD = "123456"
    INVALID_PASSWORD = "12345"
    INVALID_EMAIL = 'ilmeyandex.ru'

    # поле ввода Емейл на странице регистрации
    EMAIL_INPUT_FIELD = By.XPATH, './/fieldset[2]/div/div/input[@name = "name"]'

    # поле ввода Пароля на странице регистрации
    PASSWORD_INPUT_FIELD = By.XPATH, './/fieldset[3]/div/div/input[@name  = "Пароль"]'

    # поле ввода Имени на странице регистрации
    NAME_INPUT_FIELD = By.XPATH, './/fieldset[1]/div/div/input[@name = "name"]'

    # кнопка Войти на странице регистрации
    BUTTON_LOGIN_IN_REG = By.XPATH, './/a[@href="/login"]'

    # кнопка Личный кабинет в шапке
    PERSONAL_ACCAUNT_BUTTON = By.XPATH, './/a[@href = "/account"]'

    # кнопка зарегистрироваться на странице регистрации
    REGISTER_BUTTON = By.XPATH, './/button[text() = "Зарегистрироваться"]'

    # кнопка Войти в аккаунт на главной странице
    MAIN_PAGE_LOGIN_BUTTON = By.XPATH, './/button[text() = "Войти в аккаунт"]'

    # поле ввода email на странице авторизации
    EMAIL_INPUT_FIELD_LOGIN = By.XPATH, './/input[@name = "name"]'

    # поле ввода пароля на странице авторизации
    PASSWORD_INPUT_FIELD_LOGIN = By.XPATH, './/input[@name  = "Пароль"]'

    # кнопка Войти на странице авторизации
    LOGIN_BUTTON = By.XPATH, './/button[text() = "Войти"]'

    # тултип при некорректных данных введенного пароля на странице регистрации
    ERROR_PASSWORD = By.XPATH, './/p[text() = "Некорректный пароль"]'

    # тултип при некорректных данных введенного имени на странице регистрации
    ERROR_NAME = By.XPATH, './/p[text() = "Некорректное имя"]'

    # тултип при некорректных данных введенного email на странице регистрации
    ERROR_EMAIL = By.XPATH, './/p[text() = "Некорректный email"]'

    # имя в личном кабинете
    PROFILE_NAME = By.XPATH, ('.//input[@class ="text input__textfield text_type_main-default '
                              'input__textfield-disabled"]')

    # кнопка восстановления пароля
    RECOVER_PASSWORD_BUTTON = By.XPATH, './/a[@href="/forgot-password"]'

    # поле ввода для email на странице восстановления пароля
    RECOVERY_EMAIL = By.XPATH, './/input[@name = "name"]'

    # кнопка восстановить на странице восстановления пароля
    RECOVERY_BUTTON = By.XPATH, './/button[ text() = "Восстановить"]'

    # кнопка Войти на странице восстановления пароля
    LOGIN_BUTTON_FOR_RECOVERY = By.XPATH, './/a[@href="/login"]'

    # кнопка Выйти на странице профиля
    EXIT_BUTTON = By.XPATH, ".//button[text() = 'Выход']"

    # кнопка на логотип Stellar Burgers
    STELLAR_BURGERS_BUTTON = By.XPATH, './/a[@href="/"]'

    # кнопка конструктор в шапке
    CONSTRUCTOR_BUTTON = By.XPATH, './/p[text() = "Конструктор"]'

    # кнопка Булки
    BREAD_BUTTON = By.XPATH, './/span[text() = "Булки"]'

    # наименование раздела Булки
    BREAD_CONTENT = By.XPATH, './/h2[text() = "Булки"]'

    # кнопка Соусы
    SAUCES_BUTTON = By.XPATH, './/span[text() = "Соусы"]'

    # наименование раздела Соусы
    SAUCES_CONTENT = By.XPATH, './/h2[text() = "Соусы"]'

    # кнопка Начинки
    FILINGS_BUTTON = By.XPATH, './/span[text() = "Начинки"]'

    # наименование раздела Начинки
    FILINGS_CONTENT = By.XPATH, './/h2[text() = "Начинки"]'

    # кнопка Оформить заказ
    ORDER_BUTTON = By.XPATH, './/button[text() = "Оформить заказ"]'

    # Заголовок главной страницы "Собери бургер"
    TITLE_IN_THE_MAIN_PAGE = By.XPATH, '//h1[contains(@class, "text text_type_main-large")]'

    # кнопка Выход в Личном кабинете
    EXIT_BUTTON = By.XPATH, ".//button[text() = 'Выход']"

    # Заголовок странице авторизации
    TITLE_ENTER = By.TAG_NAME, 'h2'








