import requests
from behave import when, then

API_BASE = "https://restful-booker.herokuapp.com/booking"

# Retrieving a single booking by ID
@when('I request a booking with ID {booking_id}')
def step_request_booking_by_id(context, booking_id):
    context.response = requests.get(f"{API_BASE}/{booking_id}") 

@then('the booking details for ID {booking_id} should be returned')
def step_check_booking_details_by_id(context, booking_id):
    response_data = context.response.json()
    assert 'firstname' in response_data, "Response does not contain 'firstname'"