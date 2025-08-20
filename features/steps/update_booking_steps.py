import requests
from behave import given, when, then
from requests.auth import HTTPBasicAuth
from datetime import datetime

API_BASE = "https://restful-booker.herokuapp.com/booking"
USERNAME = "admin"  
PASSWORD = "password123" 

# Updating an expired booking
@given("I have an expired booking with ID {booking_id}")
def step_have_expired_booking(context, booking_id):
    context.booking_id = booking_id
    response = requests.get(f"{API_BASE}/{booking_id}", auth=(USERNAME, PASSWORD))
    if response.status_code == 200:
        booking_data = response.json()
        check_out_date_str = booking_data['bookingdates']['checkout']
        check_out_date = datetime.strptime(check_out_date_str, "%Y-%m-%d")
        current_date = datetime.now()
        if check_out_date >= current_date:
            raise Exception(f"Booking {booking_id} is not expired yet.")
    else:
        raise Exception(f"Failed to retrieve booking: {response.status_code}")

@when("I update the booking with new details")
def step_update_expired_booking(context):
    booking_id = context.booking_id  
    update_data = {
        "firstname": "Sally",
        "lastname": "Engler",
        "totalprice": 222,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-11-11",
            "checkout": "2024-11-22"
        }
    }
    
    context.response = requests.put(f"{API_BASE}/{booking_id}", json=update_data, auth=HTTPBasicAuth(USERNAME, PASSWORD))


@then("the updated booking details should be returned")
def step_check_updated_booking_details(context):
    expected_details = {
        'firstname': 'Sally',
        'lastname': 'Engler',
        'totalprice': 222,
        'depositpaid': True,
        'bookingdates': {
            'checkin': '2024-11-11',
            'checkout': '2024-11-22'
        }
    }
    
    actual_details = context.response.json()

    actual_details.pop('additionalneeds', None)

    assert actual_details == expected_details, f"Expected booking details {expected_details}, but got {actual_details}"



# Do a partial update with not all parameters
@given("I have a booking with ID {booking_id}")
def step_have_booking(context, booking_id):
    context.booking_id = booking_id  

@when("I partially update the booking with new parameters")
def step_partial_update_booking(context):
    partial_update_data = {
        "lastname": "Johnson"  
    }
    
    context.response = requests.patch(f"{API_BASE}/{context.booking_id}", json=partial_update_data, auth=HTTPBasicAuth(USERNAME, PASSWORD))

@then("the updated booking details should reflect the changes")
def step_check_partial_update_booking_details(context):
    response_data = context.response.json()
    assert response_data['lastname'] == "Johnson"
