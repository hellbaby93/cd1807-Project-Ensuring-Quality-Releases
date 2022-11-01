# #!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By


def config_driver():
    print('Configure Chrome Driver ...')
    options = ChromeOptions()
    options.add_argument('--headless')
    return webdriver.Chrome(options=options)

# Start the browser and login with standard_user
def test_login (username, password):
    driver = config_driver()
    driver.get('https://www.saucedemo.com/')

    driver.find_element(by=By.ID, value='user-name').send_keys(username)
    driver.find_element(by=By.ID, value='password').send_keys(password)
    driver.find_element(by=By.ID, value='login-button').click()

    print(driver.current_url)

    assert 'https://www.saucedemo.com/inventory.html' == driver.current_url

test_login('standard_user', 'secret_sauce')

