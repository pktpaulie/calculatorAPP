from behave import *


@given("I have a calculator")
def step_given_calculator(context):
    # Initialize the calculator or any necessary setup
    pass


@when('I enter "{number}" as the first number')
def step_when_enter_first_number(context, number):
    context.first_number = number


@when('I enter "{operation}" as the operation')
def step_when_enter_operation(context, operation):
    context.operation = operation


@when('I enter "{number}" as the second number')
def step_when_enter_second_number(context, number):
    context.second_number = number


@then('the answer should be "{expected_answer}"')
def step_then_check_answer(context, expected_answer):
    actual_answer = calculate(context)
    assert actual_answer == expected_answer


def calculate(context):
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
