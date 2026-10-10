from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.get('https://www.saucedemo.com/')

USER_NAME = (By.XPATH, "//*[@id='user-name']")
PASSWORD = (By.XPATH, "//*[@id='password']")
LOGIN = (By.XPATH, "//*[@id='login-button']")


def test_auth_positive():
    driver.find_element(*USER_NAME).send_keys("standard_user")
    driver.find_element(*PASSWORD).send_keys("secret_sauce")
    driver.find_element(*LOGIN).click()
    assert driver.current_url == "https://www.saucedemo.com/inventory.html", 'url не соответствует ожидаемому'
    time.sleep(1)
    driver.quit()


