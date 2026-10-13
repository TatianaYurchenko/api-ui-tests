from selenium.webdriver.common.by import By

ADD_TO_CARD_BTN = (By.XPATH, "//*[@id='add-to-cart-sauce-labs-backpack']")
CARD = (By.XPATH, "//*[@id='shopping_cart_container']/a")
ITEM = (By.XPATH, "//*[@id='item_4_title_link']/div")
ITEM_IN_CARD = (By.XPATH, "//*[@id='item_4_title_link']/div")


def test_add_item(login, wait, driver):

    assert driver.current_url == "https://www.saucedemo.com/inventory.html", 'url не соответствует ожидаемому'
    text_before = driver.find_element(*ITEM).text
    driver.find_element(*ADD_TO_CARD_BTN).click()
    driver.find_element(*CARD).click()
    text_after = driver.find_element(*ITEM_IN_CARD).text
    assert text_before == text_after



