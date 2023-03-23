import pytest
from selenium.webdriver.common.by import By

URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
ORANGE_HRM_USERNAME = "Admin"
ORANGE_HRM_PASSWORD = "admin123"
ORANGE_HRM_USERNAME_locator = "username"
ORANGE_HRM_PASSWORD_locator = "password"


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = URL
        self.ORANGE_HRM_USERNAME = ORANGE_HRM_USERNAME
        self.ORANGE_HRM_PASSWORD = ORANGE_HRM_PASSWORD
        self.ORANGE_HRM_USERNAME_locator = ORANGE_HRM_USERNAME_locator
        self.ORANGE_HRM_PASSWORD_locator = ORANGE_HRM_PASSWORD_locator

    def open(self):
        self.driver.get(self.url)

    def login(self):
        username_input = self.driver.find_element(
            By.NAME, ORANGE_HRM_USERNAME_locator)

        username_input.send_keys(self.ORANGE_HRM_USERNAME)
        password_input = self.driver.find_element(
            By.NAME, ORANGE_HRM_PASSWORD_locator)
        submit_button = self.driver.find_element(
            By.CSS_SELECTOR, ".oxd-button")
        password_input.send_keys(self.ORANGE_HRM_PASSWORD)
        submit_button.click()

    def checkLogin(self):
        assert self.driver.find_element(By.LINK_TEXT, "Admin"), "ERROR LOGIN"
