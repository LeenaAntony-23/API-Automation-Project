import pytest
import logging
from test_assyst.utils import common
from test_assyst import constants

logger = logging.getLogger('my_logger')


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
def test_fetch_appointment_data_with_valid_appointment_id(customer_id,data, create_client, post_client_data,
                                                       get_appointment_data_with_appointment_id):


    appointment_data = common.read_json("./jsons/create_client_contexts.json")
    client_contact_action = post_client_data(customer_id, appointment_data, 'contacts_client_action', True)
    client_contact_action_data = client_contact_action.json()
    common.check_reponse_message(client_contact_action_data, constants.add_client_success_message)
    logger.info(client_contact_action_data)
    logger.info("Client Details For Contact Client Action Added Successfully")

    appointment_id = client_contact_action_data['data']['contacts_client_action']['appointment_id']
    get_appointment_data = get_appointment_data_with_appointment_id(appointment_id,customer_id)
    appointment_data_response = get_appointment_data.json()
    common.check_reponse_message(appointment_data_response, constants.get_client_appointment_message)
    logger.info("Client Details Appointment Details Fetch Successfully")

    #common.compare_dicts(client_contact_action_data['data'], appointment_data_response['data'])
    logger.info("Fetch Client Details Appointment Test Passed!")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
def test_fetch_fetch_appointment_data_with_invalid_customer_id(customer_id,data,get_appointment_data_with_appointment_id,create_client):

    get_client_data = get_appointment_data_with_appointment_id('e34960f1-ce23-4985-a5df-d497193be3ab', customer_id)
    get_client_response = get_client_data.json()
    common.check_reponse_message(get_client_response, constants.get_appointment_invalid_message)
    assert get_client_response['statusCode'] == 200, f"API call failed with StatusCode: {get_client_response['statusCode']}"
    assert get_client_response["isError"] is False
    logger.info("Fetch Customer Data With Invalid Customer ID Test Passed!")
