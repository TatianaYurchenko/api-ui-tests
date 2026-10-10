from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.get('https://www.saucedemo.com/')

USER_NAME = (By.XPATH, "//*[@id='user-name']")
PASSWORD = (By.XPATH, "//*[@id='password']")
LOGIN = (By.XPATH, "//*[@id='login-button']")
ADD_TO_CARD_BTN = (By.XPATH, "//*[@id='add-to-cart-sauce-labs-backpack']")
CARD = (By.XPATH, "//*[@id='shopping_cart_container']/a")
ITEM = (By.XPATH, "//*[@id='item_4_title_link']/div")
ITEM_IN_CARD = (By.XPATH, "//*[@id='item_4_title_link']/div")


def test_add_item():
    driver.find_element(*USER_NAME).send_keys("standard_user")
    driver.find_element(*PASSWORD).send_keys("secret_sauce")
    driver.find_element(*LOGIN).click()
    assert driver.current_url == "https://www.saucedemo.com/inventory.html", 'url не соответствует ожидаемому'
    text_before = driver.find_element(*ITEM).text
    driver.find_element(*ADD_TO_CARD_BTN).click()
    driver.find_element(*CARD).click()
    text_after = driver.find_element(*ITEM_IN_CARD).text
    assert text_before == text_after



