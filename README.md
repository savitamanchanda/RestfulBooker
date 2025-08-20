# Booking API Integration Tests
[Welcome to Restful-Booker](https://restful-booker.herokuapp.com/)

---

## **TABLE OF CONTENT**

* [Project Overview](#project-overview)

* [Feature Tested](#features-tested)

* [Prerequisites](#prerequisites)

* [Installation Instructions](#installation-instructions)

---

## Project Overview

This project contains automated integration tests for the Booking Restful API. The tests are designed to ensure the quality and reliability of the API by validating various scenarios, including creating, retrieving, updating, and deleting bookings. The project uses the Behave framework for behavior-driven development (BDD) testing.

## Features Tested

### Scenarios

- **Create a booking with valid parameters**: Ensures that a booking can be successfully created and the details are correct.
  
- **Create a booking with invalid parameters**: Validates that the API handles invalid input gracefully by returning a proper error message and a 400 status code.
  
- **Retrieve all booking IDs**: Checks if all booking IDs can be retrieved successfully.
  
- **Retrieve booking IDs by first name**: Filters booking IDs based on the first name provided and checks if the correct IDs are returned.
  
- **Retrieve a booking by ID**: Verifies that booking details can be retrieved using a valid booking ID.
  
- **Update an expired booking**: Ensures that an expired booking can be updated successfully with new details.
  
- **Partial update of a booking**: Tests the ability to partially update a booking and verifies that the updated details are reflected correctly.
  
- **Delete an existing booking**: Confirms that an existing booking can be deleted successfully.
  
- **Attempt to delete a non-existing booking**: Tests the API's response when trying to delete a booking that does not exist.

## Prerequisites

- Python 3.x
- `pip` for installing dependencies


## Installation instructions

To run the tests, simply execute the following command in your terminal:
behave


