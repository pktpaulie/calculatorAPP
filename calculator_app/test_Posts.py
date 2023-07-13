import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class CalculatorAppTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()  # Change to the appropriate WebDriver for your browser
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()

    def test_calculate_addition(self):
        self.driver.get("http://localhost:8000/")  # Replace with the URL of your Django app

        first_number_input = self.driver.find_element_by_name("first_number")
        first_number_input.send_keys("5")

        operand_input = self.driver.find_element_by_name("operation")
        operand_input.send_keys("+")

        second_number_input = self.driver.find_element_by_name("second_number")
        second_number_input.send_keys("3")

        second_number_input.send_keys(Keys.RETURN)

        answer_element = self.driver.find_element_by_id("answer")
        answer = answer_element.text

        self.assertEqual(answer, "8")

    def test_calculate_subtraction(self):
        self.driver.get("http://localhost:8000/")  # Replace with the URL of your Django app

        first_number_input = self.driver.find_element_by_name("first_number")
        first_number_input.send_keys("10")

        operand_input = self.driver.find_element_by_name("operation")
        operand_input.send_keys("-")

        second_number_input = self.driver.find_element_by_name("second_number")
        second_number_input.send_keys("4")

        second_number_input.send_keys(Keys.RETURN)

        answer_element = self.driver.find_element_by_id("answer")
        answer = answer_element.text

        self.assertEqual(answer, "6")

if __name__ == "__main__":
    unittest.main()
