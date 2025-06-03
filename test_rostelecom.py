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
    # Долгая загрузка страницы, ожидаем ее загрузки
    driver.implicitly_wait(10)
    # Вводим валидный лоигн и пароль
    driver.find_element(By.ID, 'username').send_keys('boristester@yandex.ru')
    driver.find_element(By.ID, 'password').send_keys('6W2-ssC-3z2-c8V')
    driver.find_element(By.ID, 'kc-login').click()
    driver.implicitly_wait(10)
    # Проверяем прошла ли авторизация и открылась страница имеено введенного аккаунта
    assert driver.find_element(By.TAG_NAME, 'h2').text == "Тестеров Борис"


def test_authorization_to_email_password_not_valid(driver):
    # Долгая загрузка страницы, ожидаем ее загрузки
    driver.implicitly_wait(10)
    # Вводим валидный лоигн и пароль
    driver.find_element(By.ID, 'username').send_keys('boristester@yandex.ru')
    driver.find_element(By.ID, 'password').send_keys('6W2-ssC-3z2-c8Vq')
    driver.find_element(By.ID, 'kc-login').click()
    #driver.implicitly_wait(10)
    # Проверяем прошла ли авторизация и открылась страница имеено введенного аккаунта
    assert driver.find_element(By.ID, 'form-error-message').text == "Неверный логин или пароль"

def test_authorization_to_email_login_not_valid(driver):
    # Долгая загрузка страницы, ожидаем ее загрузки
    driver.implicitly_wait(10)
    # Вводим валидный лоигн и пароль
    driver.find_element(By.ID, 'username').send_keys('boristester@yndex.ru')
    driver.find_element(By.ID, 'password').send_keys('6W2-ssC-3z2-c8Vq')
    driver.find_element(By.ID, 'kc-login').click()
    #driver.implicitly_wait(10)
    # Проверяем прошла ли авторизация и открылась страница имеено введенного аккаунта
    assert driver.find_element(By.ID, 'form-error-message').text == "Неверный логин или пароль"