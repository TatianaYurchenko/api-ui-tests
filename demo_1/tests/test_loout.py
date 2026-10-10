from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time


chrome_options = Options()
# Отключаем встроенную проверку утечки паролей
chrome_options.add_experimental_option("prefs", {
    "profile.password_manager_leak_detection": False
})

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://www.saucedemo.com/')

USER_NAME = (By.XPATH, "//*[@id='user-name']")
PASSWORD = (By.XPATH, "//*[@id='password']")
LOGIN = (By.XPATH, "//*[@id='login-button']")
BURGER_MENU = (By.XPATH, "//button[@id='react-burger-menu-btn']")
LOGOUT = (By.XPATH, "//*[@id='logout_sidebar_link']")

def test_add_item():
    driver.find_element(*USER_NAME).send_keys("standard_user")
    driver.find_element(*PASSWORD).send_keys("secret_sauce")
    driver.find_element(*LOGIN).click()
    assert driver.current_url == "https://www.saucedemo.com/inventory.html", 'url не соответствует ожидаемому'
    driver.find_element(*BURGER_MENU).click()
    time.sleep(1)
    driver.find_element(*LOGOUT).click()
    assert driver.current_url == "https://www.saucedemo.com/"

