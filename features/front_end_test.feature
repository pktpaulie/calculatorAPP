Feature: Front end calculatorApp test
    As a user
    I want to use the Calculator App
    So that I can perform calculations

    @FrontendAddition
    Scenario: Calculate addition
        Given I am on the Calculator App page
        When I enter1 "5" into the "first_number" field
        And I operate "+" into the "operation" field
        And I enter2 "3" into the "second_number" field
        And I click the "calculate_button" button
        Then I should see "8" in the "expected_result" field

    @FrontendSubtraction
    Scenario: Calculate subtraction
        Given I am on the Calculator App page
        When I enter1 "10" into the "first_number" field
        And I operate "-" into the "operation" field
        And I enter2 "4" into the "second_number" field
        And I click the "calculate_button" button
        Then I should see "6" in the "expected_result" field
        
    @FrontendDivision
    Scenario: Calculate division
        Given I am on the Calculator App page
        When I enter1 "20" into the "first_number" field
        And I operate "/" into the "operation" field
        And I enter2 "4" into the "second_number" field
        And I click the "calculate_button" button
        Then I should see "5.0" in the "expected_result" field

    @FrontendMultiplication
    Scenario: Calculate multiplication
        Given I am on the Calculator App page
        When I enter1 "5" into the "first_number" field
        And I operate "*" into the "operation" field
        And I enter2 "4" into the "second_number" field
        And I click the "calculate_button" button
        Then I should see "20" in the "expected_result" field

    @FrontendPowerOf'n'
    Scenario: Calculate to the power of 'n'
        Given I am on the Calculator App page
        When I enter1 "10" into the "first_number" field
        And I operate "^" into the "operation" field
        And I enter2 "2" into the "second_number" field
        And I click the "calculate_button" button
        Then I should see "100" in the "expected_result" field
    
    @FrontendInvalidOperator
    Scenario: InvalidOperator
        Given I am on the Calculator App page
        When I enter1 "10" into the "first_number" field
        And I operate "&" into the "operation" field
        And I enter2 "2" into the "second_number" field
        And I click the "calculate_button" button
        Then I should see "invalid operator" in the "expected_result" field

    @FrontendDivisionByZero
    Scenario: DivisionByZero
        Given I am on the Calculator App page
        When I enter1 "10" into the "first_number" field
        And I operate "/" into the "operation" field
        And I enter2 "0" into the "second_number" field
        And I click the "calculate_button" button
        Then I should see "Error: Cannot divide by zero" in the "expected_result" field