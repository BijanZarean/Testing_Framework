@regression
Feature: Search function
    As a user of the ecommerce website
    I want to use the search functionality
    So that I can find the product I want to buy

    Background:
        Given I am on the Home page
    
    @smoke
    Scenario:
        When I enter "iPhone" in the search field
        And click on the search button
        Then I should see a list of results