# import pytest
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
#
# driver = None
#
#
# @pytest.fixture(scope="module")
# def init_driver():
#     global driver
#     print("---------------------setup----------------------")
#     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#     driver.implicitly_wait(10)
#     driver.delete_all_cookies()
#     driver.get("https://www.google.com")
#     yield
#     print("---------------------teardown----------------------")
#     driver.quit()
#
#
# @pytest.mark.usefixtures("init_driver")
# def test_google_title():
#     assert driver.title == "Google"
#
#
# @pytest.mark.usefixtures("init_driver")
# def test_google_url():
#     assert "google.com" in driver.current_url


# import pytest
#
# @pytest.mark.parametrize("a, b, result", [
#     (2, 3, 5),
#     (10, 5, 15),
#     (-1, 1, 0)
# ])
# def test_addition(a, b, result):
#     assert a + b == result
#
# import random
# import pytest
#
# def test_random_pass():
#     assert random.choice([True, False])


import pytest

@pytest.mark.parametrize("a, b, result", [3,2,5])
def test_addition(a, b, result):
    assert a + b == result
























