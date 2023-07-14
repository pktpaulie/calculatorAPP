from behave import *


@given("I have a calculator")
def step_given_calculator(context):
    """
    Initializes the calculator or any necessary setup.
    """
    pass


@when('I enter "{number}" as the first number')
def step_when_enter_first_number(context, number):
    """
    Enters the first number into the calculator.

    :param context: The behave context object.
    :param number: The value of the first number.
    """
    context.first_number = number


@when('I enter "{operation}" as the operation')
def step_when_enter_operation(context, operation):
    """
    Enters the operation into the calculator.

    :param context: The behave context object.
    :param operation: The value of the operation.
    """
    context.operation = operation


@when('I enter "{number}" as the second number')
def step_when_enter_second_number(context, number):
    """
    Enters the second number into the calculator.

    :param context: The behave context object.
    :param number: The value of the second number.
    """
    context.second_number = number


@then('the answer should be "{expected_answer}"')
def step_then_check_answer(context, expected_answer):
    """
    Checks if the calculated answer matches the expected answer.

    :param context: The behave context object.
    :param expected_answer: The expected answer.
    """
    actual_answer = calculate(context)
    assert actual_answer == expected_answer


def calculate(context):
    """
    Calculates the answer based on the entered numbers and operation.

    :param context: The behave context object.
    :return: The calculated answer as a string.
    """
    first_number = int(context.first_number)
    second_number = int(context.second_number)
    operation = context.operation

    if operation == "+":
        answer = first_number + second_number
    elif operation == "-":
        answer = first_number - second_number
    elif operation == "/":
        try:
            answer = first_number / second_number
        except ZeroDivisionError:
            answer = "Error: Cannot divide by zero"
    elif operation == "*":
        answer = first_number * second_number
    elif operation == "^":
        answer = first_number**second_number
    else:
        answer = "invalid operator"
    return str(answer)
