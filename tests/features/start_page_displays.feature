# Created by ncasv at 2025-04-08
Feature: Start page should display
  The start page should display.

  Scenario: The start page should display
    When I navigate to the URL "https://forverkliga.se/JavaScript/my-contacts/"
    Then the start page should display
