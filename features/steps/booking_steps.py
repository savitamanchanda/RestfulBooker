import requests
from behave import given, when, then

API_BASE = "https://restful-booker.herokuapp.com/booking"

@given("the booking API is available")
def step_given_booking_api_available(context):
    response = requests.get(API_BASE)
    assert response.status_code == 200

# Create a booking with valid parameters
@when("I create a booking with valid parameters")
def step_create_booking_valid(context):
    booking_data = {
        "firstname": "Damien",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-12-03",
            "checkout": "2024-12-13"
        }
    }
    context.response = requests.post(API_BASE, json=booking_data)

@then("the response status code should be {status_code}")
def step_check_status_code(context, status_code):
    assert context.response.status_code == int(status_code), f"Expected status code {status_code}, but got {context.response.status_code}"


@then("the booking should be created with the correct details")
def step_check_booking_details(context):
    response_data = context.response.json()  
    print(response_data)  
    booking_data = response_data.get('booking') 

    assert booking_data is not None, "Booking data is missing from the response."
    assert booking_data['firstname'] == "Damien", f"Expected 'Damien', got '{booking_data.get('firstname')}'"
    assert booking_data['lastname'] == "Brown", f"Expected 'Brown', got '{booking_data.get('lastname')}'"
    assert booking_data['totalprice'] == 111, f"Expected total price to be 111, got '{booking_data.get('totalprice')}'"


# Create a booking with invalid parameters
"""
This may be a bug as I was able to create a booking with invalid value for 
depositpaid and totalprice.
If I enter a number for any of the string fields, 
it should return a 400 error but crashes with a 500 error. 
"""
@when("I create a booking with invalid parameters")
def step_create_booking_invalid(context):
    invalid_booking_data = {
        "firstname": "",  
        "lastname": 9,   
        "totalprice": "free",  
        "depositpaid": "yes",  
        "bookingdates": {
            "checkin": "2024-10-01",
            "checkout": "2024-09-30" 
        }
    }

    context.response = requests.post(API_BASE, json=invalid_booking_data)

@then("an error message should be returned")
def step_check_error_message(context):
    response_data = context.response.json()

    assert "error" in response_data  
    assert response_data["error"] != "" 

