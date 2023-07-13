Feature: Calculator logic test

  @Addition
  Scenario: Addition

    When I enter "5" as the first number
    And I enter "+" as the operation
    And I enter "3" as the second number
    Then the answer should be "8"

  @Division
  Scenario: Division
    
    When I enter "10" as the first number
    And I enter "/" as the operation
    And I enter "2" as the second number
    Then the answer should be "5.0"

  @DivisionByZero
  Scenario: Division by zero
    
    When I enter "5" as the first number
    And I enter "/" as the operation
    And I enter "0" as the second number
    Then the answer should be "Error: Cannot divide by zero"

  @InvalidOperator
  Scenario: Invalid operator
    
    When I enter "5" as the first number
    And I enter "@" as the operation
    And I enter "3" as the second number
    Then the answer should be "invalid operator"

  @Subtraction
  Scenario: Subtraction
    
    When I enter "10" as the first number
    And I enter "-" as the operation
    And I enter "2" as the second number
    Then the answer should be "8"

  @Multiplication
  Scenario: Multiplication
    
    When I enter "10" as the first number
    And I enter "*" as the operation
    And I enter "2" as the second number
    Then the answer should be "20"
  @Squaring
  Scenario: Squaring
    
    When I enter "10" as the first number
    And I enter "^" as the operation
    And I enter "2" as the second number
    Then the answer should be "100"