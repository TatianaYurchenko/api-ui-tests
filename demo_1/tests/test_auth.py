from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

BURGER_MENU = (By.XPATH, "//button[@id='react-burger-menu-btn']")
LOGOUT = (By.XPATH, "//*[@id='logout_sidebar_link']")

def test_login(login, wait, driver):
    assert driver.current_url == "https://www.saucedemo.com/inventory.html", 'url не соответствует ожидаемому'

    # title = wait.until(lambda d: d.find_element(By.CLASS_NAME, "title"))
    # assert title.text == "Products"

def test_logout(login, wait, driver):
    assert driver.current_url == "https://www.saucedemo.com/inventory.html", 'url не соответствует ожидаемому'
    driver.find_element(*BURGER_MENU).click()
    logout_button = wait.until(
        EC.element_to_be_clickable(LOGOUT)
    )
    logout_button.click()
    assert driver.current_url == "https://www.saucedemo.com/"

