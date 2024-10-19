import pytest
import logging
from test_assyst.utils import common
from test_assyst import constants

logger = logging.getLogger('my_logger')

@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/Client/test_data_contacts_client_action.csv"))
def test_add_all_data_to_contacts_client_action(customer_id,data, field_values, create_client, post_client_data,
                                                get_client_data_with_customer_id,get_appointment_data_with_customer_id):

    values = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
              for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = values.get(list(values)[-2])
    values.popitem()
    values.popitem()
    client_contact_action = post_client_data(customer_id, values, 'contacts_client_action', False)
    client_contact_action_data = client_contact_action.json()
    common.check_reponse_message(client_contact_action_data, expected_message)
    logger.info("Client Details For Contact Client Action Added Successfully")

    logger.info("Add Contact Client Action Data Test Passed!")
    get_appointment_data = get_appointment_data_with_customer_id(customer_id)
    appointment_data_response = get_appointment_data.json()
    common.check_reponse_message(appointment_data_response, constants.get_client_success_message)
    logger.info("Client Details Appointment Details Fetch Successfully")