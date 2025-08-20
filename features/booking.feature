Feature: Booking Restful API

Scenario: Create a booking with valid parameters
    Given the booking API is available
    When I create a booking with valid parameters
    Then the response status code should be 200
    And the booking should be created with the correct details

Scenario: Create a booking with invalid parameters, should fail gracefully
    Given the booking API is available
    When I create a booking with invalid parameters
    Then the response status code should be 400
    And an error message should be returned

Scenario: Retrieve all booking IDs
    Given the booking API is available
    When I request all booking IDs
    Then the response status code should be 200
    And a list of booking IDs should be returned

Scenario: Retrieve booking IDs by first name
    Given the booking API is available
    When I request booking IDs filtered by first name "John"
    Then the response status code should be 200
    And a list of booking IDs for "John" should be returned


Scenario: Retrieve a booking by ID
    Given the booking API is available
    When I request a booking with ID 1
    Then the response status code should be 200
    And the booking details for ID 1 should be returned

Scenario: Update an expired booking
    Given the booking API is available
    And I have an expired booking with ID 1
    When I update the booking with new details
    Then the response status code should be 200
    And the updated booking details should be returned

Scenario: Partial update of a booking
    Given the booking API is available
    And I have a booking with ID 2
    When I partially update the booking with new parameters
    Then the response status code should be 200
    And the updated booking details should reflect the changes

Scenario: Delete an existing booking
    Given the booking API is available
    And I have a booking with ID 7
    When I delete the booking
    Then the response status code should be 201
    And the booking should no longer exist

Scenario: Attempt to delete a non-existing booking
    Given the booking API is available
    And there is no booking with ID 7
    When I attempt to delete the non-existing booking
    Then the response status code should be 405
    And an appropriate error message should be returned