import pytest
import logging
from test_assyst.utils import common
from test_assyst import constants

logger = logging.getLogger('my_logger')


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/Client/test_data_contacts_client_action.csv"))
def test_update_appointment_data(customer_id,get_appointment_data_with_customer_id,data, field_values, create_client, post_client_data, patch_appointment_data):

    appointment_data = common.read_json("./jsons/create_client_contexts.json")
    client_contact_action = post_client_data(customer_id, appointment_data, 'contacts_client_action', True)
    client_contact_action_data = client_contact_action.json()
    logger.info(client_contact_action_data)
    common.check_reponse_message(client_contact_action_data, constants.add_client_success_message)
    logger.info("Client Details For Contact Client Action Appointment Added Successfully")

    appointment_id = client_contact_action_data['data']['contacts_client_action']['appointment_id']
    data = {field: field_values.get(field) for field in field_values.keys() if
            field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = data.get(list(data)[-1])
    data.popitem()
    data.popitem()
    patch_client_data = patch_appointment_data(customer_id, appointment_id, data, 'contacts_client_action', False)
    patch_client_data_response = patch_client_data.json()
    logger.info(patch_client_data_response)
    common.check_reponse_message(patch_client_data_response, expected_message)
    logger.info("Client Details For Contact Client Action Appointment Updated Successfully")

    logger.info("Update Data To Contact Client Action Appointment Test Passed!")
    get_appointment_data = get_appointment_data_with_customer_id(customer_id)
    appointment_data_response = get_appointment_data.json()
    common.check_reponse_message(appointment_data_response, constants.get_client_success_message)
    logger.info("Client Details Appointment Details Fetch Successfully")