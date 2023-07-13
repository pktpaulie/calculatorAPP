import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class CalculatorAppTest(unittest.TestCase):
    def setUp(self):
        self.driver = (
            webdriver.Chrome()
        )  # Change to the appropriate WebDriver for your browser
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()

    def test_calculate_addition(self):
        self.driver.get(
            "http://localhost:8000/"
        )  # Replace with the URL of your Django app

        first_number_input = self.driver.find_element(By.NAME, "first_number")
        first_number_input.send_keys("5")

        operand_input = self.driver.find_element(By.NAME, "operation")
        operand_input.send_keys("+")

        second_number_input = self.driver.find_element(By.NAME, "second_number")
        second_number_input.send_keys("3")

        second_number_input.send_keys(Keys.RETURN)

        expected_result_element = self.driver.find_element(By.NAME, "expected_result")
        expected_result = expected_result_element.text

        assert str(expected_result) == '8'

    def test_calculate_subtraction(self):
        self.driver.get(
            "http://localhost:8000/"
        )  # Replace with the URL of your Django app

        first_number_input = self.driver.find_element(By.NAME, "first_number")
        first_number_input.send_keys("10")

        operand_input = self.driver.find_element(By.NAME, "operation")
        operand_input.send_keys("-")

        second_number_input = self.driver.find_element(By.NAME, "second_number")
        second_number_input.send_keys("4")

        second_number_input.send_keys(Keys.RETURN)

        expected_result_element = self.driver.find_element(By.NAME, "expected_result")
        expected_result = expected_result_element.text

        assert str(expected_result) == '6'


if __name__ == "__main__":
    unittest.main()
