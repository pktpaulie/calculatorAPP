from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


@given("I am on the Calculator App page")
def step_given_open_calculator_app(context):
    """
    Open the Calculator App page.

    :param context: The behave context object.
    """
    context.driver = webdriver.Chrome()
    context.driver.get("http://localhost:8000/")


@when('I enter1 "{number}" into the "{first_number}" field')
def step_when_enter_number(context, number, first_number):
    """
    Enter a number into the specified field.

    :param context: The behave context object.
    :param number: The number to enter.
    :param first_number: The name of the field to enter the number into.
    """
    input_element = context.driver.find_element(By.NAME, first_number)
    input_element.send_keys(number)


@when('I operate "{operator}" into the "{operation}" field')
def step_when_enter_operator(context, operator, operation):
    """
    Enter an operator into the specified field.

    :param context: The behave context object.
    :param operator: The operator to enter.
    :param operation: The name of the field to enter the operator into.
    """
    input_element = context.driver.find_element(By.NAME, operation)
    input_element.send_keys(operator)


@when('I enter2 "{number}" into the "{second_number}" field')
def step_when_enter_number(context, number, second_number):
    """
    Enter a number into the specified field.

    :param context: The behave context object.
    :param number: The number to enter.
    :param second_number: The name of the field to enter the number into.
    """
    input_element = context.driver.find_element(By.NAME, second_number)
    input_element.send_keys(number)


@when('I click the "{calculate_button}" button')
def step_when_click_button(context, calculate_button):
    """
    Click the specified button.

    :param context: The behave context object.
    :param calculate_button: The ID of the button to click.
    """
    button_element = context.driver.find_element(By.ID, calculate_button)
    button_element.click()


@then('I should see "{expected_result}" in the "{field}" field')
def step_then_check_result(context, expected_result, field):
    """
    Check if the expected result is displayed in the specified field.

    :param context: The behave context object.
    :param expected_result: The expected result to check.
    :param field: The name of the field to check the result in.
    """
    result_element = context.driver.find_element(By.NAME, field)
    actual_result = result_element.get_attribute("value")
    assert actual_result == expected_result


@then("I close the browser")
def step_then_close_browser(context):
    """
    Close the browser.

    :param context: The behave context object.
    """
    context.driver.quit()
