import pytest
import logging
from test_assyst.utils import common
from test_assyst import constants

logger = logging.getLogger('my_logger')


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
def test_fetch_appointment_data_with_valid_customer_id(customer_id,data, create_client, post_client_data,
                                                       get_appointment_data_with_customer_id):


    appointment_data = common.read_json("./jsons/create_client_contexts.json")
    client_contact_action = post_client_data(customer_id, appointment_data, 'contacts_client_action', True)
    client_contact_action_data = client_contact_action.json()
    common.check_reponse_message(client_contact_action_data, constants.add_client_success_message)
    logger.info("Client Details For Contact Client Action Added Successfully")

    get_appointment_data = get_appointment_data_with_customer_id(customer_id)
    appointment_data_response = get_appointment_data.json()
    common.check_reponse_message(appointment_data_response, constants.get_client_success_message)
    logger.info(appointment_data_response)
    logger.info("Client Details Appointment Details Fetch Successfully")

    common.compare_dicts(client_contact_action_data['data'], appointment_data_response['data'])
    logger.info("Fetch Client Appointment Details With Customer Id Test Passed!")


def test_fetch_fetch_appointment_data_with_invalid_customer_id(get_appointment_data_with_customer_id):
    get_client_data = get_appointment_data_with_customer_id('0006f028-ea52-4eec-94d8-e995e1c80ffc')
    get_client_response = get_client_data.json()
    common.check_reponse_message(get_client_response, constants.invalid_customer_id_message)

    assert get_client_response["isError"] is False
    logger.info("Fetch Customer Data With Invalid Customer ID Test Passed!")
