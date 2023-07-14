import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class CalculatorAppTest(unittest.TestCase):
    def setUp(self):
        """
        Set up the test case by initializing the WebDriver and implicitly waiting for elements to be found.
        """
        self.driver = webdriver.Chrome()  
        self.driver.implicitly_wait(10)

    def tearDown(self):
        """
        Clean up the test case by quitting the WebDriver.
        """
        self.driver.quit()

    def test_calculate_addition(self):
        """
        Test the addition calculation functionality of the calculator app.

        1. Open the calculator app.
        2. Enter the first number, operation, and second number.
        3. Press the Enter key to perform the calculation.
        4. Get the expected result from the input field.
        5. Assert that the expected result matches the actual result.
        """
        self.driver.get("http://localhost:8000/")  
        first_number_input = self.driver.find_element(By.NAME, "first_number")
        first_number_input.send_keys("5")

        operand_input = self.driver.find_element(By.NAME, "operation")
        operand_input.send_keys("+")

        second_number_input = self.driver.find_element(By.NAME, "second_number")
        second_number_input.send_keys("3")

        second_number_input.send_keys(Keys.RETURN)

        expected_result_element = self.driver.find_element(By.NAME, "expected_result")
        expected_result = expected_result_element.get_attribute("value")

        self.assertEqual(expected_result, '8')

    def test_calculate_subtraction(self):
        """
        Test the subtraction calculation functionality of the calculator app.

        1. Open the calculator app.
        2. Enter the first number, operation, and second number.
        3. Press the Enter key to perform the calculation.
        4. Get the expected result from the input field.
        5. Assert that the expected result matches the actual result.
        """
        self.driver.get("http://localhost:8000/")  

        first_number_input = self.driver.find_element(By.NAME, "first_number")
        first_number_input.send_keys("10")

        operand_input = self.driver.find_element(By.NAME, "operation")
        operand_input.send_keys("-")

        second_number_input = self.driver.find_element(By.NAME, "second_number")
        second_number_input.send_keys("4")

        second_number_input.send_keys(Keys.RETURN)

        expected_result_element = self.driver.find_element(By.NAME, "expected_result")
        expected_result = expected_result_element.get_attribute("value")

        self.assertEqual(expected_result, '6')


if __name__ == "__main__":
    unittest.main()
