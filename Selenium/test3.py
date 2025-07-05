# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import Select
# import time
#
# # Step 1: Launch the browser
# driver = webdriver.Chrome()
# driver.maximize_window()
#
# # Step 2: Open the registration page
# driver.get("https://demo.automationtesting.in/Register.html")
# time.sleep(2)
#
# # Step 3: Fill text fields
# driver.find_element(By.XPATH, "//input[@placeholder='First Name']").send_keys("Ajit")
# driver.find_element(By.XPATH, "//input[@placeholder='Last Name']").send_keys("Poojari")
# driver.find_element(By.XPATH, "//textarea[@ng-model='Adress']").send_keys("Bengaluru, Karnataka")
# driver.find_element(By.XPATH, "//input[@type='email']").send_keys("ajitpoojari03@gmail.com.")
# driver.find_element(By.XPATH, "//input[@type='tel']").send_keys("9945373090")
#
# # Step 4: Select gender
# driver.find_element(By.XPATH, "//input[@value='Male']").click()
#
# # Step 5: Select hobbies
# driver.find_element(By.ID, "checkbox1").click()  # Cricket
# driver.find_element(By.ID, "checkbox2").click()  # Movies
#
# # Step 6: Select language
# driver.find_element(By.ID, "msdd").click()
# time.sleep(2)
# driver.find_element(By.CLASS_NAME, "ui-corner-all").click()
# driver.find_element(By.XPATH, "//body").click()  # Close dropdown
#
# # Step 7: Select skills
# Select(driver.find_element(By.ID, "Skills")).select_by_visible_text("Python")
#
# # Step 8: Select country
# Select(driver.find_element(By.ID, "countries")).select_by_visible_text("India")
#
# # Step 9: Select date of birth
# Select(driver.find_element(By.ID, "yearbox")).select_by_visible_text("1996")
# Select(driver.find_element(By.XPATH, "//select[@placeholder='Month']")).select_by_visible_text("June")
# Select(driver.find_element(By.ID, "daybox")).select_by_visible_text("25")
#
# # Step 10: Enter password and confirm
# driver.find_element(By.ID, "firstpassword").send_keys("Test@123")
# driver.find_element(By.ID, "secondpassword").send_keys("Test@123")
#
# # Step 11: Click submit
# driver.find_element(By.ID, "submitbtn").click()
#
# print("Form submitted successfully!")
#
# # Close the browser
# time.sleep(3)
# driver.quit()
