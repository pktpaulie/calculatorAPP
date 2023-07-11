Feature: Calculator
  Scenario: Addition
    Given I have a calculator
    When I enter "5" as the first number
    And I enter "+" as the operation
    And I enter "3" as the second number
    Then the answer should be "8"

  Scenario: Division
    Given I have a calculator
    When I enter "10" as the first number
    And I enter "/" as the operation
    And I enter "2" as the second number
    Then the answer should be "5"

  Scenario: Division by zero
    Given I have a calculator
    When I enter "5" as the first number
    And I enter "/" as the operation
    And I enter "0" as the second number
    Then the answer should be "Error: Cannot divide by zero"

  Scenario: Invalid operator
    Given I have a calculator
    When I enter "5" as the first number
    And I enter "@" as the operation
    And I enter "3" as the second number
    Then the answer should be "invalid operator"
