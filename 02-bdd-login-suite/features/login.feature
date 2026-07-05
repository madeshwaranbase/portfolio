Feature: Login functionality
  As a user
  I want to log into EventHub
  So that I can access my dashboard

  @smoke
  Scenario: Successful login with valid credentials
    Given The user is on the login page
    When The user enters the username "madesh@sharklasers.com"
    And The user enters the password "Maddy@2003"
    And The user clicks on the login button
    Then The user should be redirected to the dashboard page