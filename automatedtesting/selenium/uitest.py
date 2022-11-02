# #!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By


def config_driver():
    print('Configure Chrome Driver ...')
    options = ChromeOptions()
    options.add_argument('--headless')
    return webdriver.Chrome(options=options)


def test_login(username='standard_user', password='secret_sauce'):
    # Start the browser and login with standard_user
    print("Testing Logging In")
    DRIVER.get('https://www.saucedemo.com/')

    DRIVER.find_element(by=By.ID, value='user-name').send_keys(username)
    DRIVER.find_element(by=By.ID, value='password').send_keys(password)
    DRIVER.find_element(by=By.ID, value='login-button').click()

    assert 'https://www.saucedemo.com/inventory.html' == DRIVER.current_url
    print("Testing Logging In Passed")


def test_add_to_cart_button(username='standard_user', password='secret_sauce'):
    print("Testing Add to Cart Buttons")

    DRIVER.get('https://www.saucedemo.com/inventory.html')
    print("Getting add cart buttons")
    add_to_cart_btns = [item for item in DRIVER.find_elements(
        By.CSS_SELECTOR, "button") if item.accessible_name.lower() == "Add to cart".lower()]
    remove_cart_btns = [item for item in DRIVER.find_elements(
        By.CSS_SELECTOR, "button") if item.accessible_name.lower() == "Remove".lower()]
    add_to_cart_btn_count_init = len(add_to_cart_btns)
    print("Check if add to cart button count > 0 and Remove cart button count == 0")
    assert add_to_cart_btn_count_init > 0 and len(remove_cart_btns) == 0
    print("PASSED!")

    print("Clicking add to cart buttons")
    for item in add_to_cart_btns:
        item.click()

    add_to_cart_btns = [item for item in DRIVER.find_elements(
        By.CSS_SELECTOR, "button") if item.accessible_name.lower() == "Add to cart".lower()]
    remove_cart_btns = [item for item in DRIVER.find_elements(
        By.CSS_SELECTOR, "button") if item.accessible_name.lower() == "Remove".lower()]

    print("Check if add to cart button count == 0 and Remove cart button count == initial button count")
    assert len(remove_cart_btns) == add_to_cart_btn_count_init and len(
        add_to_cart_btns) == 0
    print("PASSED!")

    print("Clicking Remove buttons")
    for item in remove_cart_btns:
        item.click()

    add_to_cart_btns = [item for item in DRIVER.find_elements(
        By.CSS_SELECTOR, "button") if item.accessible_name.lower() == "Add to cart".lower()]
    remove_cart_btns = [item for item in DRIVER.find_elements(
        By.CSS_SELECTOR, "button") if item.accessible_name.lower() == "Remove".lower()]

    print("Check if add to cart button count == initial button count and Remove cart button count == 0")

    assert len(add_to_cart_btns) == add_to_cart_btn_count_init and len(
        remove_cart_btns) == 0
    print("PASSED!")


DRIVER = config_driver()
try:
    test_login()
    test_add_to_cart_button()
except Exception as err:
    print("ERROR: {}".format(err))
finally:
    DRIVER.close()
