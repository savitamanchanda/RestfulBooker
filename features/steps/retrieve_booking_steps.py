import requests
from behave import given, when, then

API_BASE = "https://restful-booker.herokuapp.com/booking"

# Retrieve all booking IDs
@when("I request all booking IDs")
def step_request_all_booking_ids(context):
    context.response = requests.get(API_BASE)

@then("a list of booking IDs should be returned")
def step_check_list_of_booking_ids(context):
    response_data = context.response.json()
    assert isinstance(response_data, list)  
    assert len(response_data) > 0  

# Retrieve some booking IDs by query
@when('I request booking IDs filtered by first name "{firstname}"')
def step_request_booking_ids_by_firstname(context, firstname):
    params = {'firstname': firstname}
    context.response = requests.get(API_BASE, params=params)

@then('a list of booking IDs for "{firstname}" should be returned')
def step_check_filtered_booking_ids(context, firstname):
    response_data = context.response.json()
    assert isinstance(response_data, list)  
    assert len(response_data) > 0  

