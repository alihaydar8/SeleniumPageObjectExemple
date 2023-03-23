from LoginPage import LoginPage
from CreateEmployeePage import CreateEmployeePage
from DeleteEmployeePage import DeleteEmployeePage
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope='module')
def driver():
    # Initialize and configure driver and driver
    driver = webdriver.Chrome(service=Service(
        ChromeDriverManager(version='111.0.5563.64').install()))
    driver.implicitly_wait(30)
    driver.maximize_window()

    yield driver
    # Close the driver
    driver.close()


def test_login(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login()
    login_page.checkLogin()


def test_create_employee(driver):
    create_employee_page = CreateEmployeePage(driver)
    create_employee_page.open()
    create_employee_page.create("elon1", "musk1", "elon1" "musk1", "90000001")
    create_employee_page.checkCreate()


def test_delete_employee(driver):
    create_employee_page = DeleteEmployeePage(driver)
    create_employee_page.open()
    create_employee_page.delete("elon1", "90000001")
    create_employee_page.checkDelete()


# pytest test_page_object.py --html=test_page_object.html
