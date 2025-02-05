from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def validateCart():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("https://www.ebay.com")

    # search for book
    search_box = driver.find_element(By.XPATH, '//*[@id="gh-ac"]')
    search_box.click()
    search_box.send_keys("book")
    search_button = driver.find_element(By.XPATH, '//*[@id="gh-search-btn"]/span')
    search_button.click()

    # click on the very 1st link - Dynamically handled
    driver.find_element(By.XPATH, '//*[@class="srp-results srp-list clearfix"]/li[1]/div/div[2]/a').click()
    window_handles = driver.window_handles
    driver.switch_to.window(window_handles[1])

    # add to cart
    time.sleep(5)
    addtocart = driver.find_element(By.XPATH, '//*[@id="atcBtn_btn_1"]')
    addtocart.click()
    cartget = driver.find_element(By.XPATH, '//*[@class="gh-cart__icon"]')
    textvalue = cartget.text
    assert int(textvalue) == 1, "cart value is updated"
    print(f"cart value is {textvalue}")


validateCart()
