# Created by ncasv at 2025-04-08
Feature: Start page should display
  The start page should display.

  Scenario: The start page should display
    When I navigate to the URL "https://forverkliga.se/JavaScript/my-contacts/"
    Then the start page should display

  Scenario: The vän lista page should display
    When I navigate to the URL "https://forverkliga.se/JavaScript/my-contacts/"
    And I click vänlista in the header
    Then the sök namn object on the vänlista page should display

  Scenario: The Ny vän page should display
    When I navigate to the URL "https://forverkliga.se/JavaScript/my-contacts/"
    And I click ny vän in the header
    Then the namn object on the ny vän page should display
