from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Step 1: Launch the browser
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

# Step 2: Open nopCommerce demo site
driver.get("https://demo.nopcommerce.com/")
time.sleep(2)

# Step 3: Search for a product (e.g., "laptop")
search_box = driver.find_element(By.ID, "small-searchterms")
search_box.send_keys("laptop")
search_box.send_keys(Keys.RETURN)
time.sleep(3)

# Step 4: Click on the first laptop result
driver.find_element(By.XPATH, "//a[normalize-space()='Asus Laptop']").click()
time.sleep(2)

# Step 5: Click "Add to cart"
driver.find_element(By.ID, "add-to-cart-button-4").click()  # ID may change, confirm before running
time.sleep(3)

# Step 6: Confirm added to cart
driver.find_element(By.CLASS_NAME, "close").click()  # Close the green success bar
print("Product added to cart successfully!")

# Optional: Go to the cart page
driver.find_element(By.CLASS_NAME, "cart-label").click()
time.sleep(2)

# Step 7: Close browser
driver.quit()
