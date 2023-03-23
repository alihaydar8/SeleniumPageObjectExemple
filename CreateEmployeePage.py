import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

URL = "https://opensource-demo.orangehrmlive.com/web/index.php/pim/addEmployee"


class CreateEmployeePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = URL

    def open(self):
        self.driver.get(self.url)

    def create(self, firstname, lastname, middlename, employeeIdd):
        self.driver.maximize_window()
        first_name_input = self.driver.find_element(By.NAME, "firstName")
        first_name_input.clear()
        first_name_input.send_keys(firstname)
        middle_name_input = self.driver.find_element(By.NAME, "middleName")
        middle_name_input.send_keys(middlename)
        last_name_input = self.driver.find_element(By.NAME, "lastName")
        last_name_input.clear()
        last_name_input.send_keys(lastname)
        employee_id_input = self.driver.find_element(
            By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/input[1]")
        employee_id_input.send_keys(Keys.CONTROL, 'a')
        employee_id_input.send_keys(employeeIdd)
        # Submit the form
        submit_button = self.driver.find_element(
            By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[2]/button[2]")
        submit_button.click()

    def checkCreate(self):
        assert self.driver.find_element(
            By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[1]"), "ERROR Create Employee"
