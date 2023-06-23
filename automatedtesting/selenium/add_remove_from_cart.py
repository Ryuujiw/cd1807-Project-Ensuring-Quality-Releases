# #!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
import datetime


def timestamp():
    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return (ts + '\t')

# Start the browser and login with standard_user
def login(user, password):
    print(timestamp() + 'Starting the browser...')
    options = ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument("--headless") 
    options.add_argument("--remote-debugging-port=9222")

    driver = webdriver.Chrome(options=options)
    print(timestamp() + 'Browser has started. Logging in...')
    driver.get('https://www.saucedemo.com/')
    # login
    driver.find_element(By.CSS_SELECTOR, "input[id='user-name']").send_keys(user)
    driver.find_element(By.CSS_SELECTOR, "input[id='password']").send_keys(password)
    driver.find_element(By.ID, "login-button").click()
    product_label = driver.find_element(By.CSS_SELECTOR, "div[class='product_label']").text
    assert "Products" in product_label
    print(timestamp() + 'Login with username {:s} and password {:s} successfully.'.format(user, password))
    return driver

def add_cart(driver, n_items):
    for i in range(n_items):
        element = "a[id='item_" + str(i) + "_title_link']"  # Get the product URL
        driver.find_element(By.CSS_SELECTOR, element).click()  # Click the found URL
        driver.find_element(By.CSS_SELECTOR, "button.btn_primary.btn_inventory").click()  # Add product to the cart
        product = driver.find_element(By.CSS_SELECTOR, "div[class='inventory_details_name']").text  # Get the product name
        print(timestamp() + product + " added to shopping cart.")  # Show what product has been added
        driver.find_element(By.CSS_SELECTOR, "button.inventory_details_back_button").click()  # Go Back
    print(timestamp() + '{:d} items were added to shopping cart.'.format(n_items))

def remove_cart(driver, n_items):
    for i in range(n_items):
        element = "a[id='item_" + str(i) + "_title_link']"
        driver.find_element(By.CSS_SELECTOR, element).click()
        driver.find_element(By.CSS_SELECTOR, "button.btn_secondary.btn_inventory").click()
        product = driver.find_element(By.CSS_SELECTOR, "div[class='inventory_details_name']").text
        print(timestamp() + product + " removed from shopping cart.")  # Display message saying which product was added
        driver.find_element(By.CSS_SELECTOR, "button.inventory_details_back_button").click()
    print(timestamp() + '{:d} items are all removed from shopping cart.'.format(n_items))


if __name__ == "__main__":
    N_ITEMS = 6
    TEST_USERNAME = 'standard_user'
    TEST_PASSWORD = 'secret_sauce'
    driver = login(TEST_USERNAME, TEST_PASSWORD)
    add_cart(driver, N_ITEMS)
    remove_cart(driver, N_ITEMS)
    print(timestamp() + 'UI tests are all completed')
