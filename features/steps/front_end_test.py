from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


@given('I am on the Calculator App page')
def step_given_open_calculator_app(context):
    context.driver = webdriver.Chrome()  
    
    context.driver.get("http://localhost:8000/")
      

@when('I enter1 "{number}" into the "{first_number}" field')
def step_when_enter_number(context, number, first_number):
    input_element = context.driver.find_element(By.NAME, first_number)
    input_element.send_keys(number)

@when('I operate "{operator}" into the "{operation}" field')
def step_when_enter_number(context, operator, operation):
    input_element = context.driver.find_element(By.NAME, operation)
    input_element.send_keys(operator)

@when('I enter2 "{number}" into the "{second_number}" field')
def step_when_enter_number(context, number, second_number):
    input_element = context.driver.find_element(By.NAME, second_number)
    input_element.send_keys(number)

@when('I click the "{calculate_button}" button')
def step_when_click_button(context, calculate_button):
    button_element = context.driver.find_element(By.ID, calculate_button)
    button_element.click()

@then('I should see "{expected_result}" in the "{field}" field')
def step_then_check_result(context, expected_result, field):
    result_element = context.driver.find_element(By.NAME, field)
    actual_result = result_element.get_attribute("value")
    assert actual_result == expected_result

@then('I close the browser')
def step_then_close_browser(context):
    context.driver.quit()
