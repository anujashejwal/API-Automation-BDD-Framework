Feature: GitHub API validation

Scenario: Public repo check
  Given I hit public github repo API
  When I send GET request
  Then github response status code should be 200

  #Purpose: Test scenarios for the GitHub API