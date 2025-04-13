# Created by Nicklas Carlsson at 2025-04-13
Feature: Create friend
#TODO: Here I ended up with more scenarios then I thought. Refactor and do scenario outline instead.
  Background:
    When I navigate to the URL "https://forverkliga.se/JavaScript/my-contacts/"
    And I click ny vän in the header

  Scenario: Create friend with typical input
    When I type Kalle in Namn field on the ny_vän page
    And I type test@test.com in e-post field on the ny_vän page
    Then the Spara button should be enabled

  Scenario: Create friend with åäö in name
    When I type name_åäö in Namn field on the ny_vän page
    And I type test@test.com in e-post field on the ny_vän page
    Then the Spara button should be enabled

  Scenario: Create friend with no name
    When I type test@test.com in e-post field on the ny_vän page
    Then the Spara button should be disabled

  Scenario: Create friend with no email
    When I type test@test.com in e-post field on the ny_vän page
    Then the Spara button should be disabled
