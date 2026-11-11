Feature: EventHub authentication
  As an EventHub customer
  I want to authenticate securely
  So that I can browse and book events

  @smoke
  Scenario: Login page displays credential fields
    Given I open the EventHub login page
    Then the email and password fields are visible

  @positive
  Scenario: Registered customer can log in
    Given I open the EventHub login page
    When I log in with the configured sandbox account
    Then I should see the authenticated navigation

  @negative
  Scenario: Invalid credentials are rejected
    Given I open the EventHub login page
    When I log in with invalid credentials
    Then I should not see the authenticated navigation
