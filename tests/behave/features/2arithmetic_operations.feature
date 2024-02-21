Feature: 2-Arithmetic operations on a web service

  Scenario Outline: Adding two numbers <a> and <b> - changed
    Given I have a web client
    When I request "add" with parameters "a" as <a> and "b" as <b>
    Then the response should be <result>

  Examples:
  | a   | b   | result  |
  | 10  | 10   | 25    |
  | 10  | 20   | 25    |
  | ten | five| Error: Please provide valid integer values for the 'a' and 'b' parameters. |

  Scenario Outline: Subtracting two numbers
    Given I have a web client
    When I request "sub" with parameters "a" as <a> and "b" as <b>
    Then the response should be <result>

  Examples:
  | a   | b   | result  |
  | 10  | 5   | 5    |
  | ten | five| Error: Please provide valid integer values for the 'a' and 'b' parameters. |
#
  Scenario Outline: Multiplying two numbers
    Given I have a web client
    When I request "mul" with parameters "a" as <a> and "b" as <b>
    Then the response should be <result>

    Examples:
  | a   | b   | result  |
  | 10  | 5   | 50    |
  | ten | five| Error: Please provide valid integer values for the 'a' and 'b' parameters. |
#
#
  Scenario Outline: Dividing two numbers
    Given I have a web client
    When I request "div" with parameters "a" as <a> and "b" as <b>
    Then the response should be <result>

  Examples:
    | a   | b   | result  |
    | 10  | 5   | 2.0    |
    | 6   | 3   | 2.0    |
    | ten | five| Error: Please provide valid integer values for the 'a' and 'b' parameters. |
