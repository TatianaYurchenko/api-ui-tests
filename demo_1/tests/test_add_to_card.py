from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

ADD_TO_CARD_BTN = (By.XPATH, "//*[@id='add-to-cart-sauce-labs-backpack']")
CARD = (By.XPATH, "//*[@id='shopping_cart_container']/a")
ITEM = (By.XPATH, "//*[@id='item_4_title_link']/div")
ITEM_IN_CARD = (By.XPATH, "//*[@id='item_4_title_link']/div")


def test_add_item(login, wait, driver):

    assert driver.current_url == "https://www.saucedemo.com/inventory.html", 'url не соответствует ожидаемому'

    text_before = wait.until(EC.visibility_of_element_located(ITEM)).text
    add_to_card_btn = wait.until(EC.element_to_be_clickable(ADD_TO_CARD_BTN))
    add_to_card_btn.click()
    card = wait.until(EC.element_to_be_clickable(CARD))
    card.click()
    text_after = wait.until(EC.visibility_of_element_located(ITEM_IN_CARD)).text
    assert text_before == text_after


