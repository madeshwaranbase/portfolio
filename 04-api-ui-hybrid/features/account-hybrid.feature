Feature: Account creation via API verified through UI login
  As a QA engineer
  I want to create a user account through the public API
  So that I can confirm the same account is usable and reflected in the live UI

  Background:
    Given I have a randomly generated user account payload

  @hybrid @smoke
  Scenario: Account created via API logs in successfully through the UI
    When I create the account using the API
    Then the API should confirm the account was created
    When I open the login page
    And I log in with the created account's credentials
    Then the UI should show me logged in as the created account's name

  @hybrid @cleanup
  Scenario: Account deleted via API can no longer log in through the UI
    Given the account has already been created via the API
    When I delete the account using the API
    And I open the login page
    And I log in with the created account's credentials
    Then the UI should show an invalid login error
