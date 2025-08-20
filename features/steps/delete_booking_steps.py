import requests
from behave import given, when, then
from requests.auth import HTTPBasicAuth

API_BASE = "https://restful-booker.herokuapp.com/booking"
USERNAME = "admin"  
PASSWORD = "password123" 

# Delete a booking
@when("I delete the booking")
def step_delete_booking(context):
    context.response = requests.delete(f"{API_BASE}/{context.booking_id}", auth=HTTPBasicAuth(USERNAME, PASSWORD))

@then("the booking should no longer exist")
def step_check_booking_no_longer_exists(context):
    response = requests.get(f"{API_BASE}/{context.booking_id}", auth=HTTPBasicAuth(USERNAME, PASSWORD))
    assert response.status_code == 404, "Expected the booking to be deleted, but it still exists"

# Delete a non existing booking, should fail gracefully
@given("there is no booking with ID {booking_id}")
def step_no_booking_exists(context, booking_id):
    context.booking_id = booking_id 
    response = requests.get(f"{API_BASE}/{booking_id}", auth=HTTPBasicAuth(USERNAME, PASSWORD))
    assert response.status_code == 404, f"Expected booking ID {booking_id} to not exist, but got {response.status_code}"

@when("I attempt to delete the non-existing booking")
def step_attempt_delete_non_existent_booking(context):
    context.response = requests.delete(f"{API_BASE}/{context.booking_id}", auth=HTTPBasicAuth(USERNAME, PASSWORD))

@then("an appropriate error message should be returned")
def step_check_error_message(context):
    assert context.response.status_code == 405, f"Expected status code 405 but got {context.response.status_code}"
    
    response_content = context.response.content.decode('utf-8').strip()
    expected_error_message = "Method Not Allowed"

    assert response_content == expected_error_message, f"Expected error message '{expected_error_message}', but got '{response_content}'"
