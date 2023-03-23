import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

URL = "https://opensource-demo.orangehrmlive.com/web/index.php/pim/addEmployee"


class DeleteEmployeePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = URL

    def open(self):
        self.driver.get(self.url)

    def delete(self, firstname, employeeIdd):
        self.driver.get(
            "https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList")

        self.driver.find_element(
            By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[2]/button[1]").click()
        name_input = self.driver.find_element(
            By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/input[1]")
        employee_id_input = self.driver.find_element(
            By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/div[2]/div[1]/div[2]/input[1]")
        name_input.send_keys(firstname)
        employee_id_input.send_keys(employeeIdd)
        self.driver.find_element(
            By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[2]/button[2]").click()
        id_value = self.driver.find_element(
            By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/label[1]/span[1]/i[1]")
        assert id_value, firstname+" Not Found"
        self.driver.find_element(
            By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/label[1]/span[1]/i[1]").click()
        self.driver.find_element(
            By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]/div[1]/button[1]").click()
        self.driver.find_element(
            By.XPATH, "/html[1]/body[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[3]/button[2]").click()
        assert self.driver.find_element(
            By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[1]"), "element not deleted"

    def checkDelete(self):
        assert self.driver.find_element(
            By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[1]"), "ERROR Create Employee"
        time.sleep(2)
