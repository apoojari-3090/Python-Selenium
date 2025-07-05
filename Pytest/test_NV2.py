from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

def test_google():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    driver.get("http://google.com")
    assert driver.title == "Google"
    driver.quit()


def test_fb():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    driver.get("http://facebook.com")
    assert driver.title == "Facebook – log in or sign up"
    driver.quit()


def test_gm():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    driver.get("http://Gmail.com")
    assert driver.title == "Gmail"
    driver.quit()


def test_amazon():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    driver.get("http://Amazon.com")
    assert driver.title == "Amazon.com"
    driver.quit()