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

    driver.find_element(By.ID, 'forgot_password').click()
    assert driver.find_element(By.TAG_NAME, 'h1').text == "Восстановление пароля"
