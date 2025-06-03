import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(autouse=True)
def driver():
    driver = webdriver.Chrome()
    # Переходим на страницу авторизации
    driver.get('https://b2c.passport.rt.ru')

    yield driver

    driver.quit()

def test_authorization_to_email_valid(driver):
    """Tests login by email and password with valid data."""
    # Долгая загрузка страницы, ожидаем ее загрузки
    driver.implicitly_wait(5)
    # Вводим валидный лоигн и пароль
    driver.find_element(By.ID, 'username').send_keys('boristester@yandex.ru')
    driver.find_element(By.ID, 'password').send_keys('6W2-ssC-3z2-c8V')
    driver.find_element(By.ID, 'kc-login').click()
    driver.implicitly_wait(10)
    # Проверяем прошла ли авторизация и открылась страница имеено введенного аккаунта
    assert driver.find_element(By.TAG_NAME, 'h2').text == "Тестеров Борис"


def test_authorization_to_email_password_not_valid(driver):
    """Tests login by email and password with incorrect password"""
    # Долгая загрузка страницы, ожидаем ее загрузки
    driver.implicitly_wait(5)
    # Вводим валидный лоигн и пароль
    driver.find_element(By.ID, 'username').send_keys('boristester@yandex.ru')
    driver.find_element(By.ID, 'password').send_keys('6W2-ssC-3z2-c8Vq')
    driver.find_element(By.ID, 'kc-login').click()
    #driver.implicitly_wait(10)
    # Проверяем прошла ли авторизация и открылась страница имеено введенного аккаунта
    assert driver.find_element(By.ID, 'form-error-message').text == "Неверный логин или пароль"

def test_authorization_to_email_login_not_valid(driver):
    """Tests login by email and password with incorrect login"""
    # Долгая загрузка страницы, ожидаем ее загрузки
    driver.implicitly_wait(5)
    # Вводим валидный лоигн и пароль
    driver.find_element(By.ID, 'username').send_keys('boristester@yndex.ru')
    driver.find_element(By.ID, 'password').send_keys('6W2-ssC-3z2-c8Vq')
    driver.find_element(By.ID, 'kc-login').click()
    #driver.implicitly_wait(10)
    # Проверяем прошла ли авторизация и открылась страница имеено введенного аккаунта
    assert driver.find_element(By.ID, 'form-error-message').text == "Неверный логин или пароль"

def test_open_page_registration(driver):
    """Tests whether the registration page opens"""
    driver.implicitly_wait(5)
    driver.find_element(By.ID, 'kc-register').click()
    assert driver.find_element(By.TAG_NAME, 'h1').text == "Регистрация"

def test_registration_without_region(driver):
    """Tests registration with the fields entered except for the Region field."""
    driver.implicitly_wait(5)
    driver.find_element(By.ID, 'kc-register').click()
    assert driver.find_element(By.TAG_NAME, 'h1').text == "Регистрация"
    driver.find_element(By.NAME, 'firstName').send_keys('Федор')
    driver.find_element(By.NAME, 'lastName').send_keys('Двинятин')
    driver.find_element(By.ID, 'address').send_keys('bo@ya.ru')
    driver.find_element(By.ID, 'password').send_keys('Aa12345678')
    driver.find_element(By.ID, 'password-confirm').send_keys('Aa12345678')
    driver.find_element(By.NAME, 'register').click()
    assert driver.find_element(By.XPATH, '//span[contains(text(), "Укажите регион")]')

def test_password_recovery_page(driver):
    """Tests the presence of a password recovery page"""
    driver.implicitly_wait(5)
    driver.find_element(By.ID, 'forgot_password').click()
    assert driver.find_element(By.TAG_NAME, 'h1').text == "Восстановление пароля"

def test_registration_name_one_simbol(driver):
    """Tests the "Name" input field when one character is entered."""
    driver.implicitly_wait(5)
    driver.find_element(By.ID, 'kc-register').click()
    assert driver.find_element(By.TAG_NAME, 'h1').text == "Регистрация"
    driver.find_element(By.NAME, 'firstName').send_keys('Ф')
    driver.find_element(By.NAME, 'lastName').send_keys('Двинятин')
    driver.find_element(By.ID, 'address').send_keys('bo@ya.ru')
    driver.find_element(By.ID, 'password').send_keys('Aa12345678')
    driver.find_element(By.ID, 'password-confirm').send_keys('Aa12345678')
    driver.find_element(By.NAME, 'register').click()
    assert driver.find_element(By.XPATH, '//span[contains(text(), "Необходимо заполнить поле кириллицей. От 2 до 30 символов.")]')

def test_registration_name_31_simbol(driver):
    """Tests the "Name" input field with 31 characters entered out of 30 allowed."""
    driver.implicitly_wait(5)
    driver.find_element(By.ID, 'kc-register').click()
    assert driver.find_element(By.TAG_NAME, 'h1').text == "Регистрация"
    driver.find_element(By.NAME, 'firstName').send_keys('Форачшствдчтвоаствнегаовтыврвти')
    driver.find_element(By.NAME, 'lastName').send_keys('Двинятин')
    driver.find_element(By.ID, 'address').send_keys('bo@ya.ru')
    driver.find_element(By.ID, 'password').send_keys('Aa12345678')
    driver.find_element(By.ID, 'password-confirm').send_keys('Aa12345678')
    driver.find_element(By.NAME, 'register').click()
    assert driver.find_element(By.XPATH, '//span[contains(text(), "Необходимо заполнить поле кириллицей. От 2 до 30 символов.")]')

def test_registration_last_name_one_simbol(driver):
    """Tests the "Last Name" input field when one character is entered."""
    driver.implicitly_wait(5)
    driver.find_element(By.ID, 'kc-register').click()
    assert driver.find_element(By.TAG_NAME, 'h1').text == "Регистрация"
    driver.find_element(By.NAME, 'firstName').send_keys('Федор')
    driver.find_element(By.NAME, 'lastName').send_keys('Д')
    driver.find_element(By.ID, 'address').send_keys('bo@ya.ru')
    driver.find_element(By.ID, 'password').send_keys('Aa12345678')
    driver.find_element(By.ID, 'password-confirm').send_keys('Aa12345678')
    driver.find_element(By.NAME, 'register').click()
    assert driver.find_element(By.XPATH, '//span[contains(text(), "Необходимо заполнить поле кириллицей. От 2 до 30 символов.")]')

def test_registration_last_name_31_simbol(driver):
    """Tests the "Last Name" input field with 31 characters entered, out of 30 allowed."""
    driver.implicitly_wait(5)
    driver.find_element(By.ID, 'kc-register').click()
    assert driver.find_element(By.TAG_NAME, 'h1').text == "Регистрация"
    driver.find_element(By.NAME, 'firstName').send_keys('Федор')
    driver.find_element(By.NAME, 'lastName').send_keys('Дйцкертсланвоставрсыоастрансзтв')
    driver.find_element(By.ID, 'address').send_keys('bo@ya.ru')
    driver.find_element(By.ID, 'password').send_keys('Aa12345678')
    driver.find_element(By.ID, 'password-confirm').send_keys('Aa12345678')
    driver.find_element(By.NAME, 'register').click()
    assert driver.find_element(By.XPATH, '//span[contains(text(), "Необходимо заполнить поле кириллицей. От 2 до 30 символов.")]')

def test_registration_not_valid_email(driver):
    """Tests an incorrectly entered email."""
    driver.implicitly_wait(5)
    driver.find_element(By.ID, 'kc-register').click()
    assert driver.find_element(By.TAG_NAME, 'h1').text == "Регистрация"
    driver.find_element(By.NAME, 'firstName').send_keys('Федор')
    driver.find_element(By.NAME, 'lastName').send_keys('Двинятин')
    driver.find_element(By.ID, 'address').send_keys('bo')
    driver.find_element(By.ID, 'password').send_keys('Aa12345678')
    driver.find_element(By.ID, 'password-confirm').send_keys('Aa12345678')
    driver.find_element(By.NAME, 'register').click()
    assert driver.find_element(By.XPATH, '//span[contains(text(), "Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru")]')

def test_registration_short_password(driver):
    """Tests whether the entered password is of insufficient length."""
    driver.implicitly_wait(5)
    driver.find_element(By.ID, 'kc-register').click()
    assert driver.find_element(By.TAG_NAME, 'h1').text == "Регистрация"
    driver.find_element(By.NAME, 'firstName').send_keys('Федор')
    driver.find_element(By.NAME, 'lastName').send_keys('Двинятин')
    driver.find_element(By.ID, 'address').send_keys('bo')
    driver.find_element(By.ID, 'password').send_keys('Aa123')
    driver.find_element(By.ID, 'password-confirm').send_keys('Aa123')
    driver.find_element(By.NAME, 'register').click()
    assert driver.find_element(By.XPATH, '//span[contains(text(), "Длина пароля должна быть не менее 8 символов")]')

def test_registration_not_confirm_password(driver):
    """Tests whether the password confirmation check works."""
    driver.implicitly_wait(5)
    driver.find_element(By.ID, 'kc-register').click()
    assert driver.find_element(By.TAG_NAME, 'h1').text == "Регистрация"
    driver.find_element(By.NAME, 'firstName').send_keys('Федор')
    driver.find_element(By.NAME, 'lastName').send_keys('Двинятин')
    driver.find_element(By.ID, 'address').send_keys('bo')
    driver.find_element(By.ID, 'password').send_keys('Aa1232345')
    driver.find_element(By.ID, 'password-confirm').send_keys('Aa1232')
    driver.find_element(By.NAME, 'register').click()
    assert driver.find_element(By.XPATH, '//span[contains(text(), "Пароли не совпадают")]')

def test_registration_name_not_cyrillic(driver):
    """Checks the validation of the "Name" field when Latin characters are entered."""
    driver.implicitly_wait(5)
    driver.find_element(By.ID, 'kc-register').click()
    assert driver.find_element(By.TAG_NAME, 'h1').text == "Регистрация"
    driver.find_element(By.NAME, 'firstName').send_keys('Fedor')
    driver.find_element(By.NAME, 'lastName').send_keys('Двинятин')
    driver.find_element(By.ID, 'address').send_keys('bo@ya.ru')
    driver.find_element(By.ID, 'password').send_keys('Aa12345678')
    driver.find_element(By.ID, 'password-confirm').send_keys('Aa12345678')
    driver.find_element(By.NAME, 'register').click()
    assert driver.find_element(By.XPATH, '//span[contains(text(), "Необходимо заполнить поле кириллицей. От 2 до 30 символов.")]')

def test_registration_last_name_not_cyrillic(driver):
    """Checks the validation of the "Last Name" field when Latin characters are entered."""
    driver.implicitly_wait(5)
    driver.find_element(By.ID, 'kc-register').click()
    assert driver.find_element(By.TAG_NAME, 'h1').text == "Регистрация"
    driver.find_element(By.NAME, 'firstName').send_keys('Федор')
    driver.find_element(By.NAME, 'lastName').send_keys('Dvinyatin')
    driver.find_element(By.ID, 'address').send_keys('bo@ya.ru')
    driver.find_element(By.ID, 'password').send_keys('Aa12345678')
    driver.find_element(By.ID, 'password-confirm').send_keys('Aa12345678')
    driver.find_element(By.NAME, 'register').click()
    assert driver.find_element(By.XPATH, '//span[contains(text(), "Необходимо заполнить поле кириллицей. От 2 до 30 символов.")]')

def test_registration_name_spec_sympols(driver):
    """Tests registration with the fields entered except for the Region field."""
    driver.implicitly_wait(5)
    driver.find_element(By.ID, 'kc-register').click()
    assert driver.find_element(By.TAG_NAME, 'h1').text == "Регистрация"
    driver.find_element(By.NAME, 'firstName').send_keys('!@#$%^^&&*')
    driver.find_element(By.NAME, 'lastName').send_keys('Двинятин')
    driver.find_element(By.ID, 'address').send_keys('bo@ya.ru')
    driver.find_element(By.ID, 'password').send_keys('Aa12345678')
    driver.find_element(By.ID, 'password-confirm').send_keys('Aa12345678')
    driver.find_element(By.NAME, 'register').click()
    assert driver.find_element(By.XPATH, '//span[contains(text(), "Необходимо заполнить поле кириллицей. От 2 до 30 символов.")]')

def test_registration_last_name_spec_symbol(driver):
    """Tests registration with the fields entered except for the Region field."""
    driver.implicitly_wait(5)
    driver.find_element(By.ID, 'kc-register').click()
    assert driver.find_element(By.TAG_NAME, 'h1').text == "Регистрация"
    driver.find_element(By.NAME, 'firstName').send_keys('Федор')
    driver.find_element(By.NAME, 'lastName').send_keys('!@#$%^&*')
    driver.find_element(By.ID, 'address').send_keys('bo@ya.ru')
    driver.find_element(By.ID, 'password').send_keys('Aa12345678')
    driver.find_element(By.ID, 'password-confirm').send_keys('Aa12345678')
    driver.find_element(By.NAME, 'register').click()
    assert driver.find_element(By.XPATH, '//span[contains(text(), "Необходимо заполнить поле кириллицей. От 2 до 30 символов.")]')

def test_registration_valid_phone_format(driver):
    """Checks if the entered phone number is correct."""
    driver.implicitly_wait(5)
    driver.find_element(By.ID, 'kc-register').click()
    assert driver.find_element(By.TAG_NAME, 'h1').text == "Регистрация"
    driver.find_element(By.NAME, 'firstName').send_keys('Федор')
    driver.find_element(By.NAME, 'lastName').send_keys('Двинятин')
    driver.find_element(By.ID, 'address').send_keys('89872')
    driver.find_element(By.ID, 'password').send_keys('Aa12345678')
    driver.find_element(By.ID, 'password-confirm').send_keys('Aa12345678')
    driver.find_element(By.NAME, 'register').click()
    assert driver.find_element(By.XPATH, '//span[contains(text(), "Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru")]')

def test_registration_empty_name(driver):
    """Checks validation when the "Name" field is empty"""
    driver.implicitly_wait(5)
    driver.find_element(By.ID, 'kc-register').click()
    assert driver.find_element(By.TAG_NAME, 'h1').text == "Регистрация"
    driver.find_element(By.NAME, 'firstName').send_keys('')
    driver.find_element(By.NAME, 'lastName').send_keys('Двинятин')
    driver.find_element(By.ID, 'address').send_keys('bo@ya.ru')
    driver.find_element(By.ID, 'password').send_keys('Aa12345678')
    driver.find_element(By.ID, 'password-confirm').send_keys('Aa12345678')
    driver.find_element(By.NAME, 'register').click()
    assert driver.find_element(By.XPATH, '//span[contains(text(), "Необходимо заполнить поле кириллицей. От 2 до 30 символов.")]')

def test_registration_empty_last_name(driver):
    """Checks validation when the "Last Name" field is empty."""
    driver.implicitly_wait(5)
    driver.find_element(By.ID, 'kc-register').click()
    assert driver.find_element(By.TAG_NAME, 'h1').text == "Регистрация"
    driver.find_element(By.NAME, 'firstName').send_keys('Федор')
    driver.find_element(By.NAME, 'lastName').send_keys('')
    driver.find_element(By.ID, 'address').send_keys('bo@ya.ru')
    driver.find_element(By.ID, 'password').send_keys('Aa12345678')
    driver.find_element(By.ID, 'password-confirm').send_keys('Aa12345678')
    driver.find_element(By.NAME, 'register').click()
    assert driver.find_element(By.XPATH, '//span[contains(text(), "Необходимо заполнить поле кириллицей. От 2 до 30 символов.")]')

def test_registration_empty_email(driver):
    """Checks validation when the "Email or mobile phone" field is empty."""
    driver.implicitly_wait(5)
    driver.find_element(By.ID, 'kc-register').click()
    assert driver.find_element(By.TAG_NAME, 'h1').text == "Регистрация"
    driver.find_element(By.NAME, 'firstName').send_keys('Федор')
    driver.find_element(By.NAME, 'lastName').send_keys('Двинятин')
    driver.find_element(By.ID, 'address').send_keys('')
    driver.find_element(By.ID, 'password').send_keys('Aa12345678')
    driver.find_element(By.ID, 'password-confirm').send_keys('Aa12345678')
    driver.find_element(By.NAME, 'register').click()
    assert driver.find_element(By.XPATH, '//span[contains(text(), "Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru")]')
